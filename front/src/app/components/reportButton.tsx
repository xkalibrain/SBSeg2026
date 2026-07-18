import { CustomButton } from "./customButton"
import { MdOutlineFileDownload } from "react-icons/md"
import type { ScansAvailable, ScanState } from "@/types/scan"

const header =
` __          __  _            _  __     _ _ _                            ___    ___
 \\ \\        / / | |          | |/ /    | (_) |                          |__ \\  / _ \\
  \\ \\  /\\  / /__| |__   __  _| ' / __ _| |_| |__  _   _ _ __ _ __  __   __ ) || | | |
   \\ \\/  \\/ / _ \\ '_ \\  \\ \\/ /  < / _\` | | | '_ \\| | | | '__| '__| \\ \\ / // / | | | |
    \\  /\\  /  __/ |_) |  >  <| . \\ (_| | | | |_) | |_| | |  | |     \\ V // /_ | |_| |
     \\/  \\/ \\___|_.__/  /_/\\_\\_|\\_\\__,_|_|_|_.__/ \\__,_|_|  |_|      \\_/|____(_)___/

By round table team
`

type ReportButtonProps = {
    search: string
    ip: string
    results: Record<ScansAvailable, ScanState>
}


export default function ReportButton({ search, ip, results }: ReportButtonProps) {
    function getReportBody() {
        return `${header}
###########################################
###     Identificação de Endereço IP    ###
###########################################

Alias usado: ${search}
Endereço IP Descoberto: ${ip}

Outras Informações Relacionadas aos Endereçamentos IP do Alvo:
${results.whatweb.result}

############################################
###      Scanner de Portas de Redes      ###
############################################

${results.ports.result}

###################################
###   Varredura de Diretórios   ###
###################################

${results.directoryScan.result}

############################################
###     Informações Gerais do Domínio    ###
############################################

${results.whoIs.result}

#####################################################
###    Banner da Página HTML Inicial do Alvo      ###
#####################################################

${results.banner.result}

####################################
###     DNS Reverso do Domínio   ###
####################################

${results.reverseDNS.result}

############################################
###    Sub-DNS & Sistemas Integrados     ###
############################################

${results.subDNS.result}

Exploração Realizada em: ${new Date().toLocaleString()}
`
    }

    const isAllResultsLoaded = Object.values(results).every((result) => result.isLoading === false)

    function generateReport() {
        if (!isAllResultsLoaded) return

        const body = getReportBody()
        const file = new Blob([body], {type: 'text/plain'})
        const url = URL.createObjectURL(file)

        const link = document.createElement('a')
        link.href = url
        link.download = 'report.txt'

        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
    }

    return (
        <CustomButton
            onClick={generateReport}
            disabled={!isAllResultsLoaded}
            text="CLIQUE AQUI PARA FAZER O DOWNLOAD"
            icon={<MdOutlineFileDownload size={25} />}
            className="[&]:h-8"
        />
    )
}
