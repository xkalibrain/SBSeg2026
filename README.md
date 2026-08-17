<div align="center">

### Uma Abordagem Baseada em LLMs Open-Weight para Detecção e Classificação de Vulnerabilidades em Relatórios OSINT

</div>

---

Esta pesquisa foi desenvolvida para facilitar a interpretação de relatórios técnicos produzidos durante atividades de **Open Source Intelligence (OSINT)** utilizando **Grandes Modelos de Linguagem Open-Weight (Large Language Models - LLMs)**.

O projeto foi concebido para auxiliar especialistas em cibersegurança durante processos de **Attack Surface Assessment**, **Vulnerability Assessment** e análise de superfícies de ataque, reduzindo significativamente o esforço necessário para interpretar grandes volumes de evidências coletadas por ferramentas tradicionais de reconhecimento.

Ao invés de simplesmente resumir relatórios, o agente é capaz de interpreta tecnicamente as evidências encontradas, identifica possíveis vulnerabilidades, correlaciona essas informações com metodologias consolidadas da área de segurança e produz uma análise estruturada capaz de auxiliar a tomada de decisão durante avaliações de segurança.

---

# Motivação

Ferramentas de reconhecimento como **Nmap**, **WhatWeb**, **Gobuster**, **DIRB**, **DNSRecon**, **cURL** e **Whois** são amplamente utilizadas durante avaliações de segurança por produzirem informações detalhadas sobre serviços expostos, tecnologias empregadas, versões de software, diretórios públicos, configurações SSL/TLS, registros DNS e diversos outros elementos da superfície de ataque.

Embora extremamente úteis, essas ferramentas geram relatórios técnicos extensos, frequentemente contendo centenas de linhas de informações que precisam ser analisadas manualmente por especialistas.

Esse processo apresenta diversos desafios:

- elevado consumo de tempo;
- necessidade de conhecimento técnico especializado;
- dificuldade para correlacionar evidências provenientes de diferentes ferramentas;
- priorização manual das vulnerabilidades identificadas;
- possibilidade de inconsistências durante a interpretação dos resultados.

Com o avanço recente dos Grandes Modelos de Linguagem, tornou-se possível utilizar técnicas de Inteligência Artificial para auxiliar esse processo. Entretanto, modelos generalistas apresentam limitações importantes quando aplicados diretamente ao domínio da cibersegurança, como geração de respostas inconsistentes, dificuldades na interpretação de evidências técnicas e pouca padronização na classificação das vulnerabilidades.

O projeto foi desenvolvido justamente para reduzir essas limitações, empregando uma estratégia de interpretação baseada em conhecimento especializado, engenharia de prompts e integração com metodologias consolidadas da área de segurança.

---

# Contexto Científico

O desenvolvimento do projeto faz parte da pesquisa apresentada no artigo:

> **Uma Abordagem Baseada em LLMs Open-Weight para Detecção e Classificação de Vulnerabilidades em Relatórios OSINT**

aceito para publicação no:

**Simpósio Brasileiro de Segurança da Informação e de Sistemas Computacionais (SBSeg 2026).**

A pesquisa investiga a utilização de Grandes Modelos de Linguagem Open-Weight para interpretação automatizada de relatórios produzidos pela plataforma **Web xKaliBurr**, buscando reduzir o esforço manual necessário durante avaliações de segurança sem substituir a análise realizada por especialistas.

Diferentemente de scanners tradicionais, o objetivo não é executar testes de exploração ou detectar automaticamente novas vulnerabilidades, mas interpretar evidências previamente coletadas durante a fase de reconhecimento e transformá-las em informações estruturadas que apoiem a análise técnica.

---

# Selos Considerados

Este artefato é submetido para avaliação considerando os quatro selos previstos pelo processo de avaliação de artefatos do **SBSeg 2026**:

* **Artefatos Disponíveis (SeloD)**;
* **Artefatos Funcionais (SeloF)**;
* **Artefatos Sustentáveis (SeloS)**;
* **Experimentos Reprodutíveis (SeloR)**.

O repositório disponibiliza o código-fonte, a documentação, os scripts de execução, os dados anonimizados, os prompts, os relatórios anonimizados e os recursos necessários para a execução do benchmark. A organização desses componentes foi estruturada de forma a permitir tanto a utilização do artefato quanto a reprodução dos experimentos apresentados no artigo.

As instruções de instalação, configuração, execução e reprodução dos experimentos estão documentadas ao longo deste README, incluindo a configuração do ambiente, a utilização do LM Studio, a execução do Web xKaliBurr e a execução da pipeline de benchmark. A estrutura do diretório `benchmark` concentra os principais recursos necessários à reprodução dos experimentos.


# Preocupações com Segurança

A execução do artefato envolve componentes destinados à análise de superfícies de ataque e à interpretação de relatórios produzidos durante atividades de reconhecimento. Por esse motivo, alguns cuidados devem ser observados durante a execução pelos avaliadores.

O **agente LLM não realiza, por si só, testes de exploração ou ataques contra sistemas externos**. Seu funcionamento principal consiste na interpretação de relatórios técnicos previamente produzidos pelo Web xKaliBurr, transformando as evidências coletadas em informações estruturadas sobre possíveis vulnerabilidades.

Entretanto, a reprodução integral do fluxo experimental pode envolver a execução do **Web xKaliBurr**, que utiliza ferramentas de reconhecimento como **Nmap, Gobuster, DIRB, WhatWeb, DNSRecon, cURL e Whois** para coletar informações sobre aplicações e infraestruturas. Essas ferramentas são executadas automaticamente pela plataforma durante a geração dos relatórios utilizados nos experimentos.

Dessa forma, recomenda-se que os avaliadores adotem as seguintes medidas de segurança:

* executar o artefato preferencialmente em uma **máquina virtual, ambiente isolado ou infraestrutura destinada exclusivamente aos experimentos**;
* não executar atividades de reconhecimento contra sistemas, aplicações ou infraestruturas para as quais não exista autorização explícita;
* utilizar, sempre que possível, os **relatórios anonimizados disponibilizados no diretório `benchmark/reports/`**, evitando a necessidade de realizar novas atividades de reconhecimento;
* manter os serviços executados pelo Docker restritos ao ambiente local do avaliador;
* não disponibilizar publicamente as portas ou serviços utilizados pelo ambiente experimental;
* utilizar apenas modelos e arquivos de entrada obtidos de fontes confiáveis;
* evitar o carregamento de informações sensíveis ou credenciais reais nos prompts e arquivos utilizados durante os experimentos.

Para a reprodução dos experimentos apresentados no artigo, **não é necessário realizar novas explorações sobre sistemas externos**, uma vez que o repositório disponibiliza o conjunto de dados anonimizado e os relatórios de entrada utilizados pelo benchmark. Esses recursos preservam as características necessárias para a reprodução dos experimentos sem expor informações sensíveis.

O uso do **LM Studio** também deve ser realizado localmente, mantendo o servidor de inferência acessível apenas pelo ambiente de execução do avaliador. O servidor REST deve permanecer ativo durante a execução do experimento.


# Estrutura do Repositório

O repositório foi organizado de forma modular, separando os componentes necessários para a execução da plataforma, a realização das inferências e a reprodução dos experimentos científicos apresentados no artigo.

```text
xKaliBrain/
│
├── api/                # Recursos Web xKaliBurr
├── benchmark/          # Scripts e recursos para execução do benchmark
│   ├── dataset/        # Dataset utilizado nos experimentos
│   ├── prompts/        # Prompts de inferência e avaliação
│   ├── reports/        # Relatórios de entrada anonimizados
│   ├── scripts/        # Scripts auxiliares de processamento e avaliação
│   ├── main.py         # Orquestrador da pipeline experimental
│   └── requirements.txt# Dependências do benchmark
├── dataset/            # Conjunto de dados utilizado na pesquisa
├── docs/               # Documentação adicional
├── front/              # Recursos Web xKaliBurr
├── inference/          # Scripts de inferência
├── nginx/              # Recursos Web xKaliBurr
├── README.md           # Documentação principal
├── requirements.txt    # Dependências Python
├── run.sh              # Script de inicialização
└── LICENSE             # Licença do projeto
```

A estrutura do diretório `benchmark` concentra os componentes diretamente relacionados à reprodução dos experimentos. O diretório `dataset` contém o conjunto de dados anonimizado, `prompts` contém os prompts utilizados nas etapas de inferência e avaliação, `reports` contém os relatórios de entrada e `scripts` reúne os scripts auxiliares responsáveis pelo processamento dos resultados e cálculo das métricas. O arquivo `main.py` atua como ponto de entrada e orquestrador da pipeline experimental.

Essa organização permite que os avaliadores identifiquem facilmente os componentes necessários para cada etapa do experimento e possibilita a utilização independente dos recursos de inferência, avaliação e processamento.


# Reivindicações

## Reivindicação #01: Disponibilidade do Artefato — SeloD

O código-fonte, a documentação, os scripts de execução, os prompts, os dados anonimizados, os relatórios de entrada e os demais recursos necessários para a execução do artefato encontram-se disponíveis no repositório oficial do projeto.

O README apresenta instruções para instalação, configuração do ambiente, execução do Web xKaliBurr, configuração do LM Studio e reprodução dos experimentos. Além disso, os principais componentes necessários ao benchmark encontram-se organizados no diretório `benchmark`, incluindo dataset, prompts, relatórios, scripts e o programa principal de execução.

Dessa forma, o artefato disponibiliza os componentes necessários para que os avaliadores tenham acesso ao material utilizado no desenvolvimento e na avaliação experimental apresentada no artigo, atendendo aos requisitos do selo **Artefatos Disponíveis (SeloD)**.

## Reivindicação #02: Organização e Sustentabilidade do Artefato — SeloS

O repositório foi estruturado de maneira modular, separando os componentes responsáveis pela aplicação, inferência, benchmark, processamento dos resultados e documentação.

No contexto dos experimentos, o diretório `benchmark` possui uma organização específica para separar dataset, prompts, relatórios, scripts auxiliares e o programa responsável pela execução da pipeline. Essa estrutura facilita a identificação dos componentes e permite modificar ou substituir modelos, prompts e etapas de processamento sem exigir alterações em toda a arquitetura do projeto.

Além disso, o projeto documenta os requisitos de hardware e software, as dependências Python, as etapas de instalação, a configuração do LM Studio e o fluxo completo de execução.

A modularização dos componentes e a documentação disponibilizada contribuem para a manutenção, extensão e reutilização do artefato em trabalhos futuros, atendendo aos requisitos do selo **Artefatos Sustentáveis (SeloS)**.

## Reivindicação #03: Funcionamento da Pipeline de Benchmark — SeloF

O arquivo `benchmark/main.py` atua como ponto de entrada e orquestrador da pipeline experimental, coordenando as etapas de inferência das vulnerabilidades e avaliação das respostas produzidas pelos modelos de linguagem.

Durante a execução, os modelos recebem os relatórios e prompts definidos no benchmark e produzem as respectivas respostas. Quando habilitada a etapa de avaliação, as respostas também podem ser processadas pelo **LLM Judge**, conforme as configurações descritas na documentação do experimento.

Ao final da execução, são produzidos os resultados das inferências, avaliações realizadas pelo LLM Judge, métricas de desempenho e arquivos consolidados em formato CSV. Esses arquivos constituem os resultados intermediários utilizados nas análises experimentais apresentadas no artigo.

A execução bem-sucedida dessa pipeline demonstra o funcionamento dos principais componentes do artefato e permite aos avaliadores verificar diretamente sua funcionalidade, atendendo aos requisitos do selo **Artefatos Funcionais (SeloF)**.

## Reivindicação #04: Reprodução dos Resultados do Benchmark — SeloR

A reprodução dos resultados apresentados no artigo é realizada por meio da execução da pipeline experimental disponibilizada no diretório `benchmark`.

O processo inicia-se com a execução do arquivo `main.py`, responsável por coordenar as etapas de inferência e avaliação dos modelos. Para a reprodução integral dos experimentos, a documentação recomenda configurar os modelos participantes do benchmark, utilizar `ONLY_INFERENCE=False` e utilizar o modelo `gpt-oss-120b` como **LLM Judge**, conforme empregado nos experimentos apresentados no artigo.

Durante a execução, são produzidos os resultados individuais dos modelos, as avaliações realizadas pelo LLM Judge e as métricas utilizadas no benchmark. Os scripts auxiliares disponíveis no diretório `scripts/` podem então ser utilizados para consolidar os resultados, processar as informações obtidas e gerar os arquivos necessários às análises quantitativas.

O benchmark utiliza o mesmo conjunto de relatórios, prompts e critérios de avaliação para os diferentes modelos, permitindo a comparação padronizada entre as arquiteturas avaliadas.

Ao término do processo, são disponibilizados resultados em formatos como CSV, relatórios em Markdown, métricas consolidadas e logs de execução. Esses arquivos permitem verificar a conclusão do experimento e comparar os resultados obtidos com as análises apresentadas no artigo.

Dessa forma, a execução da pipeline disponibilizada permite reproduzir as principais etapas experimentais e obter os dados necessários à validação das métricas e resultados quantitativos reportados no trabalho, atendendo aos requisitos do selo **Experimentos Reprodutíveis (SeloR)**.

# LICENSE

Este projeto é disponibilizado sob a licença **Apache License 2.0**.

```text
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
```

# Como o Projeto Funciona

A arquitetura do projeto foi desenvolvida para transformar grandes relatórios OSINT em análises técnicas estruturadas.

O fluxo completo de processamento é ilustrado abaixo.

```text
                Aplicação Web
                      │
                      ▼
              Web xKaliBurr
         (Coleta de Informações)
                      │
                      ▼
          Relatório Técnico (.txt)
                      │
                      ▼
         Construção do Prompt
                      │
                      ▼
       Grande Modelo de Linguagem
          (LLM Open-Weight)
                      │
                      ▼
       Interpretação das Evidências
                      │
                      ▼
       Classificação em Categorias
                Macro
                      │
                      ▼
      Correlação com OWASP Top 10
                      │
                      ▼
      Priorização utilizando CVSS
                      │
                      ▼
          Relatório Final
```

Todo esse processo foi desenvolvido para reduzir a necessidade de interpretação manual, mantendo consistência durante a classificação das vulnerabilidades identificadas.

---

# Principais Características

Atualmente o Agente oferece:

- Interpretação automatizada de relatórios OSINT;
- Compatibilidade com Grandes Modelos de Linguagem Open-Weight;
- Engenharia de *Prompt* especializada para cibersegurança;
- Correlação automática entre evidências técnicas;
- Classificação das vulnerabilidades utilizando cinco Categorias Macro;
- Integração com a OWASP Top 10:2025;
- Priorização baseada no CVSS v3.1;
- Geração padronizada de relatórios técnicos;
- Benchmark comparativo entre diferentes LLMs;
- Ambiente reproduzível para pesquisas em Inteligência Artificial aplicada à cibersegurança.

---

# Objetivos do Projeto

O desenvolvimento foi guiado pelos seguintes objetivos:

- automatizar a interpretação de relatórios produzidos por ferramentas OSINT;
- reduzir o esforço manual necessário durante avaliações de segurança;
- produzir análises mais consistentes entre diferentes especialistas;
- integrar metodologias consolidadas de classificação e priorização de vulnerabilidades;
- investigar o potencial de Grandes Modelos de Linguagem Open-Weight em aplicações de cibersegurança;
- disponibilizar uma plataforma aberta para pesquisa e reprodução de experimentos científicos.

O projeto possui caráter acadêmico e experimental, sendo destinado ao apoio à tomada de decisão por profissionais de segurança, não substituindo a análise realizada por especialistas.

---

# Arquitetura Geral

O LLM de apoio foi projetado em uma arquitetura modular composta por diferentes componentes independentes.

```text
                    Agente

                         │

     ┌───────────────────┼───────────────────┐

     ▼                   ▼                   ▼

 Web xKaliBurr      Prompt Builder      Modelos LLM

     │                   │                   │

     └───────────────────┼───────────────────┘

                         ▼

             Motor de Interpretação

                         ▼

           Classificação das Evidências

                         ▼

          OWASP Top 10 + CVSS v3.1

                         ▼

             Relatório Estruturado
```

Essa arquitetura permite substituir facilmente modelos de linguagem, modificar estratégias de interpretação e incorporar novas metodologias de classificação sem alterar o restante da plataforma.

---


# Requisitos do Sistema

O projeto foi desenvolvido para ser executado em ambientes Linux, podendo também ser utilizado em Windows por meio do Windows Subsystem for Linux (WSL2) ou utilizando a tecnologia Docker.

Embora o projeto seja compatível com diferentes configurações de hardware, a utilização de modelos de linguagem maiores exige maior capacidade computacional.

## Configuração Mínima

| Componente | Requisito |
|------------|-----------|
| Sistema Operacional | Ubuntu 22.04+ ou Windows 11 (WSL2) |
| Python | 3.11 ou superior |
| Git | 2.40+ |
| Docker | 24+ |
| Docker Compose | 2+ |
| RAM | 8 GB |
| Espaço em Disco | 15 GB |
| GPU | Opcional |

---

## Configuração Recomendada

| Componente | Recomendado |
|------------|-------------|
| Sistema Operacional | Ubuntu 24.04 LTS |
| Python | 3.12 |
| RAM | 32 GB |
| CPU | 8 núcleos ou superior |
| GPU | NVIDIA ou Intel ARC compatível com aceleração para LLMs |
| Espaço em Disco | 40 GB |

O benchmark apresentado no artigo foi executado utilizando modelos Open-Weight de diferentes tamanhos. Modelos compactos podem ser executados apenas em CPU, enquanto modelos maiores apresentam melhor desempenho quando executados utilizando aceleração por GPU.

---

## Dependências do Web xKaliBurr

Durante a coleta de informações são utilizadas ferramentas tradicionais de reconhecimento de infraestrutura.

Entre elas:

- Nmap
- Gobuster
- DIRB
- WhatWeb
- DNSRecon
- cURL
- Whois

Essas ferramentas são executadas automaticamente pela plataforma Web xKaliBurr durante a geração dos relatórios utilizados posteriormente pelo LLM de interpretação.


---

# Instalação

## 1. Clonando o Repositório

Clone o repositório oficial.

```bash
git clone https://github.com/xkalibrain/SBSeg2026.git
```

Entre no diretório.

```bash
cd SBSeg2026
```

---

## 2. Atualizando o Sistema

Ubuntu:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 3. Instalando Python

Caso necessário:

```bash
sudo apt install python3 python3-pip -y
```

Verifique a instalação.

```bash
python3 --version
```

---

## 4. Instalando Docker

Ubuntu:

```bash
sudo apt install docker.io docker-compose -y
```

Habilite o serviço.

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

Verifique:

```bash
docker --version
```

---

## 5. Instalando as Dependências Python

Execute:

```bash
pip install -r requirements.txt
```

Ao término da instalação todas as bibliotecas necessárias estarão disponíveis.

---

# Instalando o Web xKaliBurr

O Agente utiliza como entrada relatórios produzidos pela plataforma **Web xKaliBurr**.

Caso deseje reproduzir integralmente o fluxo experimental apresentado no artigo, é necessário instalar e executar também o Web xKaliBurr.

Entre no diretório do projeto:

```bash
cd SBSeg2026
```

Conceda permissão de execução ao script de inicialização (caso necessário):

```bash
chmod +x run.sh
```

Execute o script principal:

```bash
./run.sh
```

O script irá:

- iniciar automaticamente os containers Docker necessários;
- configurar o ambiente da aplicação;
- inicializar os serviços do Web xKaliBurr;
- disponibilizar a interface Web para utilização em seu [local host](http://localhost/).

Aguarde a conclusão da inicialização.

Para verificar se todos os containers estão em execução, utilize:

```bash
docker ps
```

A saída deverá listar todos os serviços do Web xKaliBurr com o status **Up**.

Após essa etapa, a plataforma estará pronta para realizar explorações OSINT e gerar os relatórios utilizados pelo Agente durante a etapa de interpretação.

---

# Configurando o Modelo de Linguagem

O agente foi desenvolvido para trabalhar com modelos Open-Weight executados localmente.

Durante os experimentos utilizou-se o **LM Studio** como servidor de inferência.

## Instalando o LM Studio

Faça o download da versão mais recente diretamente no site oficial.

Após a instalação:

1. abra o LM Studio;
2. faça login (opcional);
3. acesse a aba **Developer**;
4. habilite o servidor local;
5. carregue um modelo compatível.

O servidor REST deverá permanecer ativo durante toda a execução do experimento.

---

# Fluxo Completo de Execução

Após a instalação, o fluxo de utilização do projeto torna-se bastante simples.

```text
Aplicação Web

        │

        ▼

Web xKaliBurr

        │

        ▼

Relatório OSINT

        │

        ▼

Agente

        │

        ▼

Prompt Especializado

        │

        ▼

LLM Open-Weight

        │

        ▼

Interpretação

        │

        ▼

Categorias Macro

        │

        ▼

OWASP Top 10

        │

        ▼

CVSS

        │

        ▼

Relatório Final
```

# Metodologia Experimental

O agente foi desenvolvido como uma plataforma de pesquisa para investigar a utilização de Grandes Modelos de Linguagem (*Large Language Models* - LLMs) na interpretação automatizada de relatórios técnicos produzidos durante atividades de reconhecimento (*Open Source Intelligence* - OSINT).

A metodologia experimental adotada foi estruturada em três etapas principais:

1. Construção de um conjunto de dados representativo;
2. Modelagem do conhecimento técnico para interpretação das evidências;
3. Benchmark comparativo entre diferentes modelos Open-Weight.

Essa organização permitiu avaliar, de forma padronizada, a capacidade dos modelos em identificar, classificar e priorizar vulnerabilidades presentes em aplicações Web reais.

---

# Construção do Dataset

Um dos principais diferenciais desta pesquisa foi a utilização de um conjunto de dados próprio, desenvolvido especificamente para o domínio de análise de vulnerabilidades.

Ao invés de utilizar bases sintéticas ou conjuntos públicos previamente anotados, optou-se pela construção de um dataset composto por relatórios reais produzidos pela plataforma Web xKaliBurr.

Durante essa etapa foram executadas explorações controladas em aplicações Web pertencentes a uma instituição federal de ensino, respeitando todas as restrições éticas e operacionais definidas para o projeto.

Cada exploração gerou um relatório técnico contendo centenas de linhas de informações provenientes de diferentes ferramentas OSINT.

Entre as informações coletadas encontram-se:

- portas abertas;
- banners de serviços;
- cabeçalhos HTTP;
- certificados SSL/TLS;
- diretórios públicos;
- versões de softwares;
- tecnologias identificadas;
- informações DNS;
- metadados da infraestrutura.

Esses relatórios constituem a entrada do LLM de apoio.

---

# Processo de Rotulação

Após a geração dos relatórios, foi realizada uma etapa de rotulação manual.

Especialistas analisaram cada evidência presente nos documentos e identificaram as vulnerabilidades correspondentes.

Durante esse processo foram atribuídos:

- descrição técnica da vulnerabilidade;
- justificativa da classificação;
- Categoria Macro;
- categoria correspondente na OWASP Top 10:2025;
- severidade segundo o CVSS v3.1.

Esse processo resultou em um conjunto de dados supervisionado utilizado tanto para desenvolvimento quanto para avaliação dos modelos.

---

# Categorias Macro

Durante o desenvolvimento do projeto observou-se que metodologias amplamente utilizadas, como a OWASP Top 10 e o CVSS, possuem objetivos distintos.

Enquanto a OWASP organiza famílias de vulnerabilidades, o CVSS estabelece métricas quantitativas para priorização.

Entretanto, nenhuma dessas metodologias oferece uma estrutura intermediária destinada à interpretação de evidências produzidas durante atividades de reconhecimento.

Para suprir essa necessidade, foram propostas cinco Categorias Macro.

Essas categorias funcionam como uma camada intermediária entre:

- evidências técnicas;
- classificação da vulnerabilidade;
- priorização da criticidade.

As categorias possuem caráter operacional e foram desenvolvidas especificamente para interpretação de relatórios OSINT.

---

## MACRO 01

### Divulgação de Informações

Agrupa evidências relacionadas à exposição indevida de informações técnicas capazes de auxiliar etapas posteriores de exploração.

Exemplos:

- banners;
- versões;
- cabeçalhos HTTP;
- mensagens de erro;
- arquivos públicos.

---

## MACRO 02

### Diretórios e Recursos Expostos

Agrupa evidências relacionadas à descoberta de diretórios, arquivos e recursos acessíveis externamente.

Exemplos:

- diretórios administrativos;
- arquivos de backup;
- páginas de autenticação;
- endpoints públicos.

---

## MACRO 03

### Softwares Desatualizados

Relaciona componentes cuja versão identificada apresenta vulnerabilidades conhecidas ou encontra-se fora do ciclo de suporte.

Exemplos:

- Apache;
- Nginx;
- PHP;
- OpenSSH;
- bibliotecas Web.

---

## MACRO 04

### Infraestrutura Exposta

Relaciona informações referentes à infraestrutura tecnológica identificada durante o reconhecimento.

Exemplos:

- serviços;
- protocolos;
- servidores;
- DNS;
- certificados.

---

## MACRO 05

### Configuração Fraca de SSL/TLS

Relaciona problemas encontrados durante a avaliação da camada criptográfica.

Exemplos:

- protocolos inseguros;
- cifras fracas;
- certificados expirados;
- configurações inadequadas.

---

# Benchmark dos Modelos

Uma das principais contribuições do trabalho consiste na avaliação comparativa entre diferentes Grandes Modelos de Linguagem Open-Weight.

Os experimentos buscaram responder à seguinte questão de pesquisa:

> Qual família de modelos apresenta melhor desempenho na interpretação automatizada de relatórios OSINT?

Para responder essa questão foi desenvolvido um benchmark padronizado.

Todos os modelos receberam exatamente:

- o mesmo prompt;
- o mesmo conjunto de relatórios;
- os mesmos critérios de avaliação;
- o mesmo formato de saída esperado.

Dessa forma foi possível comparar diretamente o desempenho entre arquiteturas distintas.

---

# Configuração Experimental

Para garantir a reprodutibilidade dos experimentos apresentados, esta seção especifica as versões das principais ferramentas, a configuração de hardware e as variantes exatas dos modelos utilizadas durante o benchmark.

## LM Studio

Durante os experimentos, o LM Studio foi utilizado como servidor local de inferência para disponibilizar os modelos Open-Weight por meio de uma API compatível com o padrão utilizado pela pipeline experimental.

A versão utilizada nos experimentos foi:

| Componente | Versão utilizada     |
| ---------- | -------------------- |
| LM Studio  | **0.4.19 (Build 2)** |

Para reproduzir os experimentos, recomenda-se utilizar exatamente essa versão do LM Studio, evitando a substituição automática pela versão mais recente, uma vez que alterações entre versões podem modificar o comportamento do servidor de inferência, dos runtimes ou da compatibilidade com determinados modelos.

Após a instalação, o servidor local deve ser habilitado na aba **Developer** do LM Studio e permanecer ativo durante a execução do benchmark.

## Hardware Experimental

Os experimentos do benchmark foram executados utilizando:

| Componente              | Configuração                  |
| ----------------------- | ----------------------------- |
| GPU                     | NVIDIA RTX PRO 6000 Blackwell |
| VRAM                    | 96 GB GDDR7                   |
| Quantização dos modelos | Q4_K_M                        |

A utilização da mesma configuração de hardware não é obrigatória para executar o artefato, mas diferenças de hardware podem afetar principalmente o tempo de inferência e o comportamento de alocação de memória.

# Modelos Avaliados

O benchmark apresentado no artigo avaliou **15 Grandes Modelos de Linguagem (LLMs) Open-Weight**, pertencentes às famílias Qwen, Gemma, Llama, DeepSeek e Phi.

Para eliminar ambiguidades de versão e variante, a tabela abaixo apresenta os identificadores específicos utilizados no experimento. Todos os modelos foram executados utilizando a quantização **Q4_K_M**.

|  # | Modelo                             | Tamanho | Quantização |
| -: | ---------------------------------- | ------: | ----------- |
|  1 | **Qwen3.6-35B-A3B**                |     35B | Q4_K_M      |
|  2 | **Gemma-4-26B-A4B**                |     26B | Q4_K_M      |
|  3 | **Qwen3.6-27B**                    |     27B | Q4_K_M      |
|  4 | **Llama-4-Scout-17B-16E-Instruct** |    109B | Q4_K_M      |
|  5 | **Gemma-4-E2B**                    |    5.1B | Q4_K_M      |
|  6 | **Llama-3.3-70B-Instruct**         |     70B | Q4_K_M      |
|  7 | **DeepSeek-R1-Distill-Llama-70B**  |     70B | Q4_K_M      |
|  8 | **DeepSeek-R1-Distill-Qwen-14B**   |     14B | Q4_K_M      |
|  9 | **DeepSeek-R1-Distill-Qwen-32B**   |     32B | Q4_K_M      |
| 10 | **Phi-4**                          |     14B | Q4_K_M      |
| 11 | **Meta-Llama-3.1-8B-Instruct**     |      8B | Q4_K_M      |
| 12 | **DeepSeek-R1-Distill-Llama-8B**   |      8B | Q4_K_M      |
| 13 | **Llama-3.2-3B-Instruct**          |      3B | Q4_K_M      |
| 14 | **Phi-4-Mini-Instruct**            |    3.8B | Q4_K_M      |
| 15 | **DeepSeek-R1-Distill-Qwen-7B**    |      7B | Q4_K_M      |

O benchmark foi realizado utilizando o mesmo conjunto de relatórios, prompts e critérios de avaliação para todos os modelos. Dessa forma, as diferenças observadas nos resultados estão associadas às características dos modelos e de suas respectivas inferências, mantendo as demais condições experimentais padronizadas.



# Métricas Avaliadas

Todos os modelos foram avaliados utilizando métricas clássicas de classificação.

As principais métricas incluem:

- Precisão (*Precision*);
- Revocação (*Recall*);
- F1-Score;
- Tempo médio de inferência;
- Consistência das respostas;
- Capacidade de classificação das Categorias Macro;
- Correlação com OWASP Top 10;
- Correlação com CVSS.

Essas métricas permitem avaliar não apenas a quantidade de vulnerabilidades identificadas, mas também a qualidade das respostas produzidas pelos modelos.

---

# Organização dos Experimentos

Todos os recursos necessários para a reprodução dos experimentos apresentados no artigo encontram-se organizados no diretório `benchmark`, conforme a estrutura abaixo.

```text
benchmark/

├── dataset/
├── prompts/
├── reports/
├── scripts/
├── main.py
└── requirements.txt
```

Cada componente possui uma responsabilidade específica durante a execução do benchmark.

| Arquivo/Diretório | Descrição |
|-------------------|-----------|
| `dataset/` | Conjunto de dados anonimizado utilizado durante os experimentos, preservando as características necessárias para a reprodução do benchmark sem expor informações sensíveis. |
| `prompts/` | Prompts utilizados nas etapas de inferência e avaliação dos modelos de linguagem. |
| `reports/` | Relatórios de entrada utilizados pelo benchmark, derivados das análises realizadas pelo Web xKaliBurr e devidamente anonimizados. |
| `scripts/` | Scripts auxiliares responsáveis pelas etapas de inferência, avaliação, processamento dos resultados e cálculo das métricas utilizadas no artigo. |
| `main.py` | Script principal que coordena a execução da *pipeline* experimental do benchmark. |
| `requirements.txt` | Lista das dependências Python necessárias para executar o benchmark sem a utilização de contêineres Docker. |

---

# Reproduzindo os Experimentos

Após concluir a instalação do ambiente, configurar o LM Studio e carregar os modelos de linguagem desejados, acesse o diretório `benchmark` e execute a *pipeline* principal do benchmark:

```bash
python main.py
```

O arquivo `main.py` atua como orquestrador da *pipeline* experimental, coordenando automaticamente a execução das etapas de inferência das vulnerabilidades e da avaliação das respostas produzidas pelos modelos de linguagem.

Para reproduzir integralmente os experimentos apresentados no artigo, recomenda-se:

- configurar a lista de modelos de linguagem que participarão do benchmark;
- definir o parâmetro `ONLY_INFERENCE=False`, habilitando também a etapa de avaliação;
- utilizar o modelo `gpt-oss-120b` como *LLM Judge*, conforme empregado nos experimentos do artigo.

Após a conclusão da execução, os scripts auxiliares presentes no diretório `scripts/` podem ser utilizados para consolidar os resultados produzidos, calcular as métricas do benchmark e gerar os arquivos utilizados nas análises apresentadas no artigo.

Ao término do processo, serão produzidos automaticamente:

- respostas geradas por cada modelo de linguagem;
- avaliações realizadas pelo *LLM Judge*;
- métricas de desempenho;
- arquivos consolidados em formato CSV;
- resultados quantitativos utilizados nas tabelas e análises do artigo.

Os arquivos produzidos durante a execução são armazenados automaticamente nos diretórios `outputs/`, `metrics/` e `results/`, permitindo a reprodução completa do benchmark e a validação dos resultados apresentados neste trabalho.

---


# Teste Mínimo

Após concluir a instalação do ambiente, recomenda-se realizar um teste mínimo para verificar o funcionamento correto do artefato antes de iniciar a execução completa do benchmark.

Antes da execução, certifique-se de que:

1. o **LM Studio** esteja instalado e em execução;
2. o servidor local do LM Studio esteja habilitado;
3. um modelo de linguagem compatível esteja carregado;
4. o servidor REST do LM Studio esteja disponível para receber as requisições do benchmark.

O projeto utiliza o LM Studio como servidor local de inferência para os modelos Open-Weight.

Para o teste mínimo, recomenda-se utilizar o modelo **`gemma-4-e2b`**, devido ao seu menor custo computacional e à sua capacidade de ser executado em configurações de hardware mais modestas.

A partir do diretório `benchmark`, execute:

```bash
cd benchmark
python main.py
```

O arquivo `main.py` atua como orquestrador da pipeline experimental, coordenando as etapas de inferência e avaliação das respostas produzidas pelos modelos de linguagem.

Para o teste mínimo, recomenda-se executar inicialmente apenas uma inferência, utilizando o modelo `gemma-4-e2b`, antes de iniciar a execução completa do benchmark.

A execução será considerada bem-sucedida caso o modelo processe o relatório de entrada e produza uma resposta estruturada sem ocorrência de erros de comunicação com o servidor local do LM Studio.

Após a validação do funcionamento básico, o avaliador poderá prosseguir para a execução completa do benchmark utilizando os modelos e configurações descritos nas seções seguintes.

---

# Tempo Estimado

O tempo necessário depende do modelo utilizado.

| Modelo | Tempo Médio |
|----------|------------|
| Compactos | 1–5 minutos |
| Médios | 5–20 minutos |
| Grandes | 20–60 minutos |

Os tempos acima consideram execução local utilizando aceleração por GPU.

Execuções exclusivamente em CPU podem demandar tempos significativamente maiores.

---

# Recursos Computacionais

Durante a execução do benchmark recomenda-se:

- mínimo de 16 GB de RAM;
- aproximadamente 20 GB livres em disco;
- conexão estável para download inicial dos modelos;
- GPU opcional, porém recomendada.

---

# Validação dos Resultados

Ao término da execução, verifique se foram gerados:

- arquivos CSV;
- relatórios em Markdown;
- métricas consolidadas;
- logs de execução.

Esses artefatos confirmam que o benchmark foi concluído corretamente.

---
