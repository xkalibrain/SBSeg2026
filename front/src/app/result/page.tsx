'use client'
import { useState, useEffect } from "react"
import { IoInformationCircleOutline } from "react-icons/io5"
import Image from "next/image"
import { useRouter, useSearchParams } from 'next/navigation'
import Link from 'next/link'
import SectionButton from "@/app/components/sectionButton"
import { RunAllScan } from "@/api/run_all_scan"
import IpSection from "@/app/components/ipSection"
import { ScanSection } from "@/app/components/scanSection"
import Hint from "@/app/components/hint"
import ReportButton from "@/app/components/reportButton"
import type { ScansAvailable, ScanState } from "@/types/scan"
import { CustomButton } from "../components/customButton"
import { MdOutlineConstruction, MdOutlinePsychology, MdPsychology, MdSearch } from "react-icons/md"
import { GradientSearchIcon } from "../components/icons/gradient-search"
import { Modal } from "../components/modal"

type Sections = "GeneralInfo" | "Directories" | "Services" | "Neighbors"
export type Section = {
    name: Sections
    title: string,
    scans: ScansAvailable[]
}
export const sections: Record<Sections, Section> = {
    GeneralInfo: {
        name: "GeneralInfo",
        title: "INFORMAÇÕES GERAIS",
        scans: ["whoIs", "banner"],
    },
    Directories: {
        name: "Directories",
        title: "DIRETÓRIOS E PÁGINAS SENSÍVEIS",
        scans: ["directoryScan"],
    },
    Services: {
        name: "Services",
        title: "SERVIÇOS E PORTAS DE REDE",
        scans: ["ports"],
    },
    Neighbors: {
        name: "Neighbors",
        title: "DOMÍNIOS VIZINHOS",
        scans: ["reverseDNS", "subDNS"],
    },
}

const defaultModuleState = {
    isLoading: true,
    result: "",
}

export default function ResultPage(){
    const searchParams = useSearchParams()
    const router = useRouter()

    const [isModalOpen, setIsModalOpen] = useState(false)
    const [section, setSection] = useState(sections.GeneralInfo)
    const [ip, setIp] = useState("")
    const [results, setResults] = useState<Record<ScansAvailable, ScanState>>({
        whatweb: { name: "whatweb", ...defaultModuleState},
        reverseDNS: { name: "reverseDNS", ...defaultModuleState},
        subDNS: { name: "subDNS", ...defaultModuleState},
        whoIs: { name: "whoIs", ...defaultModuleState},
        banner: { name: "banner", ...defaultModuleState},
        directoryScan: { name: "directoryScan", ...defaultModuleState},
        ports: { name: "ports", ...defaultModuleState},
    })

    const optionSelected = searchParams.get('option') as 'http' | 'https'
    const searchValue = searchParams.get('search')?.toLocaleLowerCase() ?? ""
    const isAllResultsLoaded = Object.values(results).every((result) => result.isLoading === false)

    function handleXkalibrain() {
        setIsModalOpen(true)
    }

    useEffect(() => {
        const fetchData = async () => {
            const {promises, ip} = await RunAllScan(searchValue!, optionSelected)
            if (promises) {
                setIp(ip)
                for (const key in promises) {
                    promises[key as ScansAvailable]
                        .then(async response => {
                            const responseText = response.ok ? await response.text() : "Falha ao executar esse módulo"
                            setResults((prev) => ({
                                ...prev,
                                [key]: {
                                    name: key,
                                    isLoading: false,
                                    result: responseText,
                                }
                            }))
                        })
                }
            }
        }

        fetchData()
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    return (
        <>
            <header className="flex flex-row gap-4 text-sm w-full">
                <Link href={{pathname: "/"}}>
                    <Image
                        src="/exekaliburr-icon.svg"
                        alt={""}
                        width={50}
                        height={24}
                        priority
                    />
                </Link>
                <div className="flex flex-row border border-white items-center rounded-md bg-slate-700 p-3 grow">
                    <div className="pr-5 border-r-2">
                        <p className="text-blue-500">{optionSelected}</p>
                    </div>
                    <IoInformationCircleOutline className="text-blue-500 ml-3" size={25}/>
                    <div className="ml-3 w-full">
                        <div className="text-gray-400 bg-slate-700 w-full">{searchValue}</div>
                    </div>
                </div>
                <CustomButton
                    variant="inverse"
                    text="NOVA CONSULTA"
                    className="[&:disabled_path]:fill-slate-400"
                    icon={<GradientSearchIcon />}
                    disabled={!isAllResultsLoaded}
                    onClick={() => router.push("/")}
                />
                <CustomButton
                    text="XKALIBRAIN"
                    icon={<MdOutlinePsychology size={25} className="scale-x-[-1]" />}
                    disabled={!isAllResultsLoaded}
                    onClick={handleXkalibrain}
                />
            </header>
            <div className="flex flex-col w-full h-full mt-10 gap-6">
                <div className="flex flex-row gap-4 overflow-x-auto">
                    {Object.values(sections).map((value) => (
                        <SectionButton
                            key={value.name}
                            section={value}
                            onSelect={setSection}
                            isCurrent={section.title == value.title}
                        />
                    ))}
                </div>
                <div className="flex gap-4 w-full">
                    <div className="bg-slate-900 divide-y divide-blue-500 p-10 rounded-md grow min-w-0">
                        <div className="flex flex-col gap-6">
                            <ReportButton search={searchValue} ip={ip} results={results} />
                            <IpSection
                                search={searchValue}
                                ip={ip}
                                whatweb_scan={results.whatweb}
                                render_whatweb={section.name === "GeneralInfo"}
                            />
                        </div>
                        {sections[section.name].scans.map((scan) => (
                            <ScanSection
                                key={scan}
                                scan={results[scan]}
                            />
                        ))}
                    </div>
                    <Hint section={section} />
                </div>
            </div>

            <Modal
                isOpen={isModalOpen}
                onClose={() => setIsModalOpen(false)}
            >
                <MdOutlineConstruction size={64} className="self-center" />
                <span>Esta funcionalidade está em desenvolvimento e será integrada em breve.</span>
            </Modal>
        </>
    )
}
