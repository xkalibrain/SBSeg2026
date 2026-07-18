import HintElement from "./hintElement"
import { MdLightbulb } from "react-icons/md"
import type { Section } from "@/app/result/page"

type HintProps = {
    section: Section
}

type HintBySectionProps = {
    title: string
    hints: string[]
}

const sectionsProps: Record<Section['name'], HintBySectionProps> = {
    GeneralInfo: {
        title: "O Web xKaliburr é capaz de capturar informações detalhadas sobre as configurações do domínio analisado, tais como os plugins ativos na página, tecnologias utilizadas pelo sistema, códigos HTML da página inicial, dados pessoais dos proprietários do domínio, entre muitas outras informações.",
        hints: [
            "Vulnerabilidades nos plugins detectados",
            "Existência de comentários comprometedores, deixados inadvertidamente pelos desenvolvedores nos códigos HTML da página analisada",
            "Vazamentos inadequados de e-mails corporativos, telefones, nomes de administradores e responsáveis pelo domínio. Essas informações podem ser utilizadas para ataques de Phishing e Engenharia Social.",
        ],
    },
    Directories: {
        title: "O Web xKaliburr é capaz de realizar varreduras nas árvores de subdiretórios do alvo analisado. Esta abordagem é interessante do ponto de vista de um agente malicioso, pois amplia a superfície de ataques que podem ser direcionados ao site-alvo.",
        hints: [
            "Páginas administrativas, como painéis de login de funcionários ou utilizadores internos do sistema. Essas páginas podem ser vítimas de ataques de Força Bruta e sucessivas tentativas de conexão",
            "Diretórios de serviços internos. Páginas que, por alguma razão, precisam ter comunicação direta com o back-end da aplicação. Mesmo que não possuam nenhum link direto com as páginas públicas utilizadas pelos usuários comuns, é possível detectar esse tipo de página caso medidas adequadas de proteção não tenham sido devidamente configuradas",
            "Qualquer página que possua campo de entrada de dados expostos aos usuários. É extremamente importante sempre aplicar o princípio da Confiança Zero. Portanto, campos de busca, painéis de cadastro ou qualquer tecnologia semelhante que apresente esse input de dados precisam urgentemente estar devidamente protegidos e sanitizados.",
        ],
    },
    Services: {
        title: "O Web xKaliburr é capaz de realizar comunicações com as portas de rede existentes na infraestrutura do domínio explorado. Dessa forma, é possível obter informações valiosas sobre as configurações daquela hospedagem, possibilitando a aplicação de diversas abordagens ofensivas ao alvo analisado.",
        hints: [
            "Configurações inadequadas das portas de rede. Aplicando o princípio do Privilégio Mínimo, desabilitando a ativação de portas desnecessárias para reduzir as superfícies de ataque dos invasores",
            "Verifique se os serviços operantes em suas portas de rede estão atualizados e protegidos. Uma das maneiras mais simples de realizar ataques a domínios inseguros na internet é utilizando Exploits em tecnologias desatualizadas presentes em algum site",
            "Procure camuflar suas portas de rede. Uma abordagem comum é a utilização de \"Portas Altas\". Por exemplo, utilizar a porta 4343 no lugar da porta 443 que é destinada por padrão à comunicação de serviços HTTPS, esta é um alvo comum entre todos os atacantes. Se sua aplicação utiliza essa configuração, considere modificar o serviço para outra porta incomum, conhecida apenas pelos funcionários internos do sistema.",
        ],
    },
    Neighbors: {
        title: "O Web xKaliBurr possibilita a varredura das hospedagens e sub-sistemas presentes no mesmo intervalo de endereçamento IP do alvo analisado. Dessa forma, é possível identificar outros potenciais alvos de ataques, ampliando a superfície de ataque disponível para um invasor. Em caso de sucesso na aplicação de qualquer vetor de ataque, o invasor pode realizar uma operação conhecida como \"Movimentação Lateral\". Assim, partindo de um domínio vulnerável na vizinhança do alvo principal, ele é capaz de causar impactos significativos no objetivo das explorações.",
        hints: [],
    }
}

export default function Hint({ section }: HintProps) {
    const props = sectionsProps[section.name]

    return (
        <section className="flex flex-col w-64 h-fit shrink-0 sticky text-xs top-4 border border-white bg-gradient-to-r from-cyan-500 to-purple-700 rounded-md text-white p-5">
            <div className="flex flex-row justify-start">
                <MdLightbulb className="text-yellow-500 mr-1" size={25}/>
                <h2 className="text-base">{"DICAS DE SEGURANÇA"}</h2>
            </div>
            <p className="py-3 text-white">{props.title}</p>
            {props.hints.length > 0 && (
                <>
                    <p className="w-full p-3 bg-yellow-500 rounded-md text-center text-black font-bold">
                        ESTEJA ATENTO
                    </p>
                    <ul className="flex flex-col gap-3 mt-3">
                        {props.hints.map((hint, index) => (
                            <HintElement key={index} text={hint} />
                        ))}
                    </ul>
                </>
            )}
        </section>
    )
}
