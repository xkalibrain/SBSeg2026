# Web xKaliBurr

Projeto desenvolvido para o Salão de Ferramentas do Simpósio Brasileiro de Cibersegurança (SBSeg).

O Web xKaliBurr é uma ferramenta voltada à exploração de aplicações online, projetada para apoiar profissionais de segurança cibernética durante a fase de levantamento de informações (Information Gathering) em testes de invasão (Web Penetration Testing). Seu principal objetivo é automatizar a coleta de informações de segurança por meio de uma interface intuitiva e de fácil utilização, reduzindo o esforço operacional e auxiliando na identificação inicial de potenciais vulnerabilidades.

A ferramenta realiza a coleta automatizada de informações relevantes para a avaliação de segurança de aplicações web, incluindo:
* Identificação de endereços IP, registros DNS e componentes da infraestrutura de rede associados ao domínio analisado;
* Descoberta e versionamento de serviços expostos em portas de rede, incluindo servidores web e demais aplicações acessíveis;
* Enumeração de diretórios, arquivos e páginas ocultas, permitindo a identificação de recursos potencialmente sensíveis;
* Coleta de banners e cabeçalhos HTTP, auxiliando na identificação de tecnologias e configurações expostas;
* Mapeamento de tecnologias empregadas pela aplicação, como servidores web, CMSs, frameworks e bibliotecas;
* Enumeração de subdomínios e serviços relacionados, ampliando a visibilidade da superfície de ataque;
* Geração de um relatório técnico consolidado, contendo as evidências coletadas durante a fase de reconhecimento.

Veja mais detalhes de [Como xKaliBurr funciona](/docs/workflow.md).

## Estrutura do Projeto

O Web xKaliBurr foi desenvolvido seguindo uma arquitetura modular baseada em três componentes principais: API, Front-end Web e ambiente de execução em containers Docker.

A API atua como a camada de integração responsável por orquestrar a execução das ferramentas nativas de pentest disponíveis no Kali Linux (como Nmap, WhatWeb, DNSRecon, Gobuster, entre outras). Além de encapsular a lógica de execução, ela padroniza as respostas e disponibiliza os resultados por meio de serviços HTTP consumidos pelo front-end.

O Front-end Web fornece uma interface gráfica intuitiva que permite ao usuário executar as etapas de reconhecimento e levantamento de informações sem a necessidade de utilizar diretamente o terminal do sistema operacional. Dessa forma, tarefas tradicionalmente realizadas por linha de comando podem ser executadas de maneira mais simples, organizada e acessível.

Por fim, toda a aplicação é distribuída utilizando Docker, garantindo um ambiente de execução padronizado, isolado e de fácil implantação. Essa abordagem reduz problemas de compatibilidade entre sistemas, simplifica a instalação das dependências e facilita a replicação do ambiente em diferentes máquinas.

Você pode conferir mais sobre a [API](api/README.md) e o [Front-end](front/README.md).

## Arquitetura

                 ┌─────────────────────┐
                 │   Front-end Web     │
                 │ (Interface Gráfica) │
                 └──────────┬──────────┘
                            │ HTTP/REST
                            ▼
                 ┌─────────────────────┐
                 │        API          │
                 │ Orquestra Execução  │
                 └──────────┬──────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   Nmap               WhatWeb             DNSRecon
        ▼                   ▼                   ▼
      Gobuster          cURL              Outras Ferramentas
                            │
                            ▼
                  Relatório Consolidado

### Dependências

Para executar o Web xKaliBurr, recomenda-se a utilização do Docker e do Docker Compose, que automatizam a configuração do ambiente e simplificam o processo de implantação da ferramenta.

Caso prefira executar os componentes manualmente, será necessário instalar individualmente as dependências da API e do Front-end, conforme descrito nos respectivos arquivos README de cada projeto.

| Dependência    | Versão |
| -------------- | ------ |
| Docker         | 26.1.4 |
| Docker-Compose | 2.27.1 |

## Executando o Web xKaliBurr

Para executar o Web xKaliBurr, é necessário ter o Docker e o Docker Compose instalados na máquina.

* Windows: No Windows, é necessário habilitar a funcionalidade Host Networking (atualmente em fase Beta) nas configurações do Docker Desktop para que a comunicação entre os containers funcione corretamente.
Para executar a ferramenta, você precisa ter o Docker e o Docker Compose instalados em sua máquina. Além disso, caso queria rodar no windows é necessário ativar a feature "host networking" que está em beta.

* Linux: Para distribuições Linux, disponibilizamos um script de instalação que automatiza toda a configuração inicial: `./setup.sh` (Script testado no Ubuntu 22.04) para facilitar sua instalação. Caso vá rodar localmente (recomendado) não precisa alterar nenhuma variável de ambiente padrão.

Para fazer o setup manualmente, antes de executar a ferramenta você deve criar um arquivo `.env` nas pastas `./front/` e `./api/`, pode criá-lo apenas como uma cópia dos arquivos `.env.template` que já está configurado para rodar a ferramenta localmente.
<br> Além disso, com as variáveis devidamente configuradas você precisa ainda criar um outro arquivo `.env` na raiz do projeto com a porta da interface web configurada. Para simplificar, você pode apenas copiar o arquivo `./front/.env` na pasta raiz.

Por fim, para executar a ferramenta basta rodar o comando:

```bash
docker compose up
```

caso comando não seja reconhecido, use:

```bash
docker-compose up
```

Após a execução do comando, a ferramenta estará disponível em `http://localhost`.

## Usando a ferramenta

Na página inicial, informe o domínio ou endereço do sistema que deseja analisar e clique em **Realizar Análise** para iniciar o processo de reconhecimento.

A ferramenta executará automaticamente as etapas de coleta e análise utilizando os módulos do **Web xKaliBurr**. Durante esse processo, a interface exibirá uma tela de carregamento indicando o andamento da análise. Dependendo do alvo e das condições da rede, essa etapa pode levar alguns minutos para ser concluída.

Ao término da execução, os resultados serão organizados nas seguintes seções:

- **Informações Gerais** — Apresenta informações sobre o domínio analisado, infraestrutura de rede, tecnologias identificadas, cabeçalhos HTTP e demais dados coletados durante a fase de reconhecimento.

- **Diretórios e Páginas Sensíveis** — Exibe os diretórios, arquivos e páginas administrativas identificados durante a enumeração, destacando recursos potencialmente sensíveis.

- **Serviços e Portas de Rede** — Lista as portas abertas, serviços detectados, versões identificadas e possíveis indícios de vulnerabilidades relacionados à infraestrutura do alvo.

- **Domínios Vizinhos** — Apresenta informações sobre a infraestrutura DNS, subdomínios, registros associados e demais sistemas relacionados ao domínio analisado.

Além da visualização pela interface Web, é possível exportar todos os resultados da análise em um relatório no formato **`.txt`** por meio do botão **Download da Análise**.

> **Observação:** O Web xKaliBurr realiza técnicas de reconhecimento e enumeração utilizando ferramentas amplamente empregadas em testes de intrusão. Recomenda-se utilizar a ferramenta exclusivamente em ambientes cuja análise tenha sido previamente autorizada.


# xKaliBrain

O **xKaliBrain** é um modelo de linguagem (*Large Language Model - LLM*) especializado na interpretação automática de relatórios técnicos produzidos pelo **Web xKaliBurr**.

Enquanto o Web xKaliBurr é responsável pela coleta de informações e enumeração da superfície de ataque, o xKaliBrain atua como uma camada inteligente de interpretação, identificando vulnerabilidades, classificando evidências e estruturando automaticamente os resultados obtidos durante a fase de reconhecimento.

Atualmente o modelo é executado localmente através do **LM Studio**, preservando a privacidade dos dados analisados e dispensando o uso de serviços em nuvem.

## Como funciona

O fluxo de utilização do xKaliBrain é composto por quatro etapas:

1. O **Web xKaliBurr** realiza a coleta de informações do alvo e gera um relatório técnico bruto (`.txt`).

2. O **LM Studio** executa o modelo fine-tunado do xKaliBrain localmente.

3. O script `lmrequest.py` envia automaticamente o relatório para o modelo utilizando a API compatível com o padrão OpenAI disponibilizada pelo LM Studio.

4. O modelo interpreta todo o relatório e retorna uma saída estruturada em formato **JSON**, contendo as vulnerabilidades identificadas e suas respectivas classificações.

O fluxo completo pode ser representado da seguinte forma:

```text
Web xKaliBurr
        │
        ▼
 Relatório (.txt)
        │
        ▼
    LM Studio
 (xKaliBrain)
        │
        ▼
 lmrequest.py
        │
        ▼
 Resultado (.json)
```

## Taxonomia de Vulnerabilidades

O xKaliBrain foi treinado para interpretar relatórios de reconhecimento utilizando uma taxonomia composta por cinco categorias principais de vulnerabilidades.

| ID | Categoria |
|----|-----------|
| MACRO 01 | Information Disclosure |
| MACRO 02 | Directory Traversal |
| MACRO 03 | Outdated Software |
| MACRO 04 | Infrastructure Disclosure |
| MACRO 05 | Weak SSL/TLS Configuration |

Cada evidência encontrada no relatório é associada exclusivamente a uma dessas categorias.

## Formato da saída

Após a análise, o modelo retorna um objeto JSON contendo todas as evidências encontradas e suas respectivas classificações.

Exemplo:

```json
{
    "findings_list": [
        {
            "finding": "Server: Apache/2.4.49",
            "macro_id": "MACRO 03",
            "justification": "Versão potencialmente desatualizada do servidor web."
        },
        {
            "finding": "/admin - Status: 200",
            "macro_id": "MACRO 02",
            "justification": "Diretório administrativo acessível."
        }
    ]
}
```

## Execução

Após iniciar o LM Studio com o modelo do xKaliBrain carregado, basta executar:

```bash
python lmrequest.py
```

O script irá:

- localizar automaticamente todos os relatórios presentes na pasta `reports/`;
- enviar cada relatório ao xKaliBrain através da API do LM Studio;
- interpretar a resposta do modelo;
- validar o JSON retornado;
- salvar automaticamente os resultados na pasta `outputs/`.

Cada relatório processado gera um arquivo `.json` contendo as vulnerabilidades identificadas.

## Requisitos

Para utilizar o xKaliBrain são necessários:

- LM Studio instalado;
- modelo do xKaliBrain carregado no LM Studio;
- API do LM Studio habilitada (`localhost:1234`);
- Python 3.10+;
- biblioteca `requests`.

## Arquitetura

```text
                 +---------------------+
                 |   Web xKaliBurr     |
                 +---------------------+
                           │
                           │ Relatório (.txt)
                           ▼
                 +---------------------+
                 |      LM Studio      |
                 |   xKaliBrain (LLM)  |
                 +---------------------+
                           │
                 OpenAI Compatible API
                           │
                           ▼
                 +---------------------+
                 |    lmrequest.py     |
                 +---------------------+
                           │
                           ▼
                 +---------------------+
                 |   Resultado JSON    |
                 +---------------------+
```
