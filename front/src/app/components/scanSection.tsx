import { ScansAvailable, ScanState } from "@/types/scan"
import { Spinner } from "./spinner"

type SectionInfoProps = {
    scan: ScanState
}

type ScanProps = {
    title: string
}
const scansProps: Record<ScansAvailable, ScanProps> = {
    whatweb: {
        title: "",
    },
    reverseDNS: {
        title: "DNS Reverso do Domínio",
    },
    subDNS: {
        title: "Sub DNS do Domínio",
    },
    whoIs: {
        title: "Informações Gerais do Domínio",
    },
    banner: {
        title: "Banner da Página HTML Inicial do Alvo",
    },
    directoryScan: {
        title: "Varredura de Diretórios",
    },
    ports: {
        title: "Scanner de Portas de Rede",
    },
}

export function ScanSection({ scan }: SectionInfoProps) {
    return (
        <section className="pt-7 mb-7">
            <h2 className="text-blue-500 text-2xl font-bold mb-5">{scansProps[scan.name].title}</h2>
            {scan.isLoading ? <Spinner /> : (
                <>
                    <pre className="text-white overflow-x-auto">{scan.result}</pre>
                </>
            )}
        </section>
    )
}
