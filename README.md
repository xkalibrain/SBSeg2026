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

O artefato pode ser executado em diferentes configurações de hardware, dependendo da etapa que se deseja reproduzir. Os requisitos de memória diferem entre a execução básica da plataforma, o teste mínimo de inferência e a execução completa do benchmark. Para validar o funcionamento da pipeline de inferência utilizando o modelo `gemma-4-e2b`, recomenda-se a configuração:

## Configuração Mínima — Inferência com Modelo Compacto & Execução da Plataforma

| Componente | Requisito |
|------------|-----------|
| Sistema Operacional | Ubuntu 22.04+ ou Windows 11 (WSL2) |
| Python | 3.11 ou superior |
| Git | 2.40+ |
| Docker | 24+ |
| Docker Compose | 2+ |
| RAM | 16 GB |
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

---

## Configuração Utilizada nos Experimentos do Artigo

A execução completa do benchmark exige uma configuração mais robusta, uma vez que os experimentos envolvem modelos Open-Weight de diferentes tamanhos. Os resultados apresentados no artigo foram obtidos utilizando uma infraestrutura de alto desempenho, composta por:

| Componente              | Configuração                  |
| ----------------------- | ----------------------------- |
| GPU                     | NVIDIA RTX PRO 6000 Blackwell |
| VRAM                    | 96 GB GDDR7                   |
| Quantização dos modelos | Q4_K_M                        |

Essa configuração foi utilizada para permitir a execução dos diferentes modelos avaliados no benchmark sob condições experimentais padronizadas.


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

Esta seção descreve o procedimento necessário para reproduzir os experimentos apresentados no artigo, incluindo a configuração do ambiente Python, a execução do benchmark, a configuração do LLM Judge, o teste mínimo de funcionamento e a identificação dos arquivos de saída esperados.

Todos os recursos necessários para a reprodução estão concentrados no diretório `benchmark/`, incluindo:

```text
benchmark/
├── dataset/       # Dataset utilizado na avaliação
├── prompts/       # Prompts de inferência e avaliação
├── reports/       # Relatórios de entrada
├── scripts/       # Scripts auxiliares
├── main.py        # Ponto de entrada do benchmark
└── requirements.txt
```

## 1. Configuração do Ambiente Python

Recomenda-se utilizar um ambiente virtual Python isolado para evitar conflitos entre as dependências do benchmark e outras bibliotecas instaladas no sistema.

A partir da raiz do repositório:

```bash
cd benchmark
python3 -m venv .venv
```

Ative o ambiente virtual.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Depois, instale as dependências utilizadas pelo benchmark:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Verifique se o interpretador utilizado pertence ao ambiente virtual:

```bash
which python
```

No Windows:

```powershell
where python
```

O caminho apresentado deve apontar para `benchmark/.venv/`.

## 2. Configuração do LM Studio

Os experimentos utilizam o LM Studio como servidor local de inferência.

A versão utilizada nos experimentos é:

| Componente | Versão             |
| ---------- | ------------------ |
| LM Studio  | **0.4.19 Build 2** |

Após instalar o LM Studio:

1. abra o aplicativo;
2. acesse a aba **Developer**;
3. habilite o servidor local;
4. carregue o modelo que será utilizado;
5. mantenha o servidor REST ativo durante a execução.

A comunicação do benchmark com o LM Studio é realizada por meio da variável `MACHINE_URL`. O código utiliza a API compatível com OpenAI disponibilizada pelo LM Studio.

Por padrão, o endpoint local esperado é:

```text
http://127.0.0.1:1234/v1
```

Configure a variável de ambiente antes da execução:

### Linux / macOS

```bash
export MACHINE_URL="http://127.0.0.1:1234/v1"
```

### Windows PowerShell

```powershell
$env:MACHINE_URL="http://127.0.0.1:1234/v1"
```

A implementação dessa comunicação está disponível em `benchmark/scripts/utils.py`.

## 3. Teste Mínimo

Antes de reproduzir o benchmark completo, recomenda-se executar o teste mínimo disponibilizado no `benchmark/main.py`.

A configuração atual do arquivo `main.py` já está preparada para utilizar exclusivamente o modelo:

```python
lista_modelos = ["google/gemma-4-e2b"]
```

e executar também a etapa de avaliação:

```python
ONLY_INFERENCE = False
```

O modelo utilizado como LLM Judge é definido como:

```python
modelo_judge = "gpt-oss-120b"
```

Portanto, para realizar o teste mínimo, não é necessário modificar a lista de modelos. Basta executar:

```bash
cd benchmark
python main.py
```

### O que o teste mínimo executa?

O teste mínimo utiliza **um único modelo candidato**, `google/gemma-4-e2b`, sobre os relatórios disponibilizados em `benchmark/reports/`.

O arquivo `main.py` percorre a lista de modelos configurada e chama `inferencia_llms()` para cada modelo. A função de inferência, por sua vez, percorre os relatórios disponíveis no diretório `benchmark/reports/`, ignorando os arquivos que contêm `_inter` no nome.

Assim, "teste mínimo" refere-se à utilização de **um único modelo candidato**, e não à execução de apenas uma chamada de inferência. Essa configuração reduz o custo computacional em relação ao benchmark completo, mantendo todas as etapas necessárias para verificar o funcionamento da pipeline.

## 4. Parâmetros de Inferência

As inferências dos modelos candidatos utilizam a API compatível com OpenAI disponibilizada pelo LM Studio.

A configuração empregada pelo código é:

| Parâmetro   | Valor                              |
| ----------- | ---------------------------------- |
| Modelo      | Definido em `lista_modelos`        |
| Temperature | **0.0**                            |
| API         | OpenAI-compatible API              |
| Endpoint    | Definido por `MACHINE_URL`         |
| Entrada     | Relatórios em `benchmark/reports/` |

O prompt de sistema utilizado pelo modelo candidato está definido diretamente em:

```text
benchmark/scripts/executa_predicao_LLMs.py
```

O modelo recebe o relatório técnico como mensagem de usuário e deve produzir uma resposta estruturada em JSON.

## 5. Estrutura Esperada da Resposta do Modelo

A execução é considerada válida quando o modelo produz uma resposta que pode ser interpretada como um objeto JSON válido contendo a chave `findings_list`.

A estrutura esperada é:

```json
{
  "findings_list": [
    {
      "finding": "Short name of the finding",
      "macro_id": "MACRO 01",
      "justification": "Brief explanation based on the macro definition"
    }
  ]
}
```

Cada elemento de `findings_list` representa uma vulnerabilidade identificada pelo modelo.

Os campos esperados são:

| Campo           | Descrição                                  |
| --------------- | ------------------------------------------ |
| `finding`       | Nome ou descrição resumida do achado       |
| `macro_id`      | Categoria macro atribuída ao achado        |
| `justification` | Justificativa técnica para a classificação |

As cinco categorias possíveis são:

* `MACRO 01` — Information Disclosure;
* `MACRO 02` — Directory Traversal;
* `MACRO 03` — Outdated Software;
* `MACRO 04` — Infrastructure Disclosure;
* `MACRO 05` — Weak SSL/TLS Configuration.

O código valida a resposta utilizando `extract_json_from_llm_response()`. Caso a resposta não esteja inicialmente em JSON válido, o benchmark utiliza um prompt adicional para solicitar a correção do formato.

## 6. Arquivo de Saída da Inferência

Após a execução, as respostas são armazenadas no diretório:

```text
benchmark/models_predictions/
```

Para o teste mínimo com `google/gemma-4-e2b`, o arquivo esperado é:

```text
benchmark/models_predictions/results_google_gemma-4-e2b.json
```

O arquivo contém uma lista de resultados, com uma entrada para cada relatório processado.

A estrutura geral é:

```json
[
  {
    "target": "nome_do_relatorio.txt",
    "results": {
      "findings_list": [
        {
          "finding": "...",
          "macro_id": "MACRO 01",
          "justification": "..."
        }
      ]
    },
    "correct_format": true,
    "inference_time": 12.34,
    "prompt_tokens": 1234,
    "completion_tokens": 256,
    "total_tokens": 1490
  }
]
```

O avaliador pode, portanto, verificar objetivamente o sucesso da inferência confirmando:

1. a existência do arquivo `results_google_gemma-4-e2b.json`;
2. a existência de uma entrada para os relatórios processados;
3. a presença do campo `results.findings_list`;
4. a presença dos campos `finding`, `macro_id` e `justification`;
5. o valor `correct_format: true`.

## 7. LLM Judge

Quando `ONLY_INFERENCE = False`, a pipeline executa uma segunda etapa utilizando um LLM Judge para avaliar as vulnerabilidades produzidas pelo modelo candidato.

No experimento, o modelo utilizado como Judge é:

```text
gpt-oss-120b
```

A configuração está definida no arquivo:

```text
benchmark/main.py
```

por meio de:

```python
modelo_judge = "gpt-oss-120b"
```

O Judge recebe dois elementos principais:

1. a vulnerabilidade produzida pelo modelo candidato;
2. as vulnerabilidades correspondentes presentes no dataset ouro.

O prompt utilizado pelo experimento é:

```text
SYSTEM_PROMPT_AVALIADOR_CAND2
```

definido em:

```text
benchmark/prompts/prompts_judge.py
```

### Parâmetros do LLM Judge

| Parâmetro         | Configuração                      |
| ----------------- | --------------------------------- |
| Modelo            | `gpt-oss-120b`                    |
| Temperature       | **0.0**                           |
| Prompt de sistema | `SYSTEM_PROMPT_AVALIADOR_CAND2`   |
| Entrada           | Predição do modelo + dataset ouro |
| Formato esperado  | Dois objetos JSON                 |

O uso de `temperature = 0.0` busca reduzir a variabilidade das avaliações entre execuções.

### Estrutura esperada da resposta do Judge

O Judge deve retornar dois objetos JSON:

```json
{"veredito": "CORRETO"}
{"ids_ouro_correspondentes": [5]}
```

Quando a predição não possui correspondência no dataset ouro:

```json
{"veredito": "INCORRETO"}
{"ids_ouro_correspondentes": []}
```

O campo `veredito` indica se a vulnerabilidade predita corresponde a uma vulnerabilidade do dataset ouro.

O campo `ids_ouro_correspondentes` contém os identificadores das vulnerabilidades correspondentes no dataset ouro, com no máximo dois IDs.

Caso o Judge produza uma resposta fora do formato esperado, a implementação realiza uma segunda chamada ao mesmo modelo utilizando `SYSTEM_PROMPT_CORRIGE_JSON` para solicitar a correção da resposta.

## 8. Arquivos Produzidos pelo LLM Judge

As avaliações produzidas pelo Judge são armazenadas em:

```text
benchmark/judge_evaluations/
```

Para o modelo `google/gemma-4-e2b`, o arquivo esperado é:

```text
benchmark/judge_evaluations/automatic_evaluations_google_gemma-4-e2b.json
```

O arquivo contém as avaliações agrupadas por target e registra, entre outras informações:

```json
{
  "evaluation_metadata": {
    "modelo_preditor": "google/gemma-4-e2b",
    "modelo_judge": "gpt-oss-120b"
  },
  "rotulacao": "CORRETO",
  "ids_correspondentes": [5]
}
```

Além disso, o processo registra informações auxiliares em:

```text
benchmark/debug.log
```

## 9. Cálculo das Métricas

Após a execução do Judge, as métricas podem ser calculadas pelo script:

```text
benchmark/scripts/calcula_metrica_judge.py
```

O cálculo considera:

* True Positives (TP);
* False Positives (FP);
* False Negatives (FN);
* Precision;
* Recall;
* F1-Score.

As métricas são calculadas a partir das correspondências identificadas pelo LLM Judge entre as predições e o dataset ouro.

O resultado é salvo em:

```text
benchmark/metric_results/
```

Para o modelo `google/gemma-4-e2b`, o arquivo esperado é:

```text
benchmark/metric_results/prediction_metrics___preditor_google_gemma-4-e2b.json
```

A estrutura contém:

```json
{
  "dataset_size": 0,
  "predictions_size": 0,
  "TP": 0,
  "FP": 0,
  "FN": 0,
  "precision": 0.0,
  "recall": 0.0,
  "f1": 0.0
}
```

Os valores serão preenchidos de acordo com as predições e avaliações produzidas durante a execução.

## 10. Reprodução do Benchmark Completo

Depois de validar o teste mínimo, a lista de modelos em:

```text
benchmark/main.py
```

pode ser substituída pela lista completa dos modelos avaliados no artigo.

A execução integrada segue o fluxo:

```text
Relatórios
    │
    ▼
Modelo candidato
    │
    ▼
models_predictions/
    │
    ▼
LLM Judge
    │
    ▼
judge_evaluations/
    │
    ▼
Cálculo das métricas
    │
    ▼
metric_results/
    │
    ▼
Consolidação dos resultados
```

Para executar somente a etapa de inferência, utilize:

```python
ONLY_INFERENCE = True
```

Para executar inferência, avaliação pelo Judge e cálculo das métricas:

```python
ONLY_INFERENCE = False
```

## 11. Relação entre Scripts e Resultados

A seguinte tabela permite identificar diretamente qual componente deve ser utilizado para reproduzir cada etapa experimental.

| Etapa / Resultado                 | Arquivo                                      | Principal saída                                  |
| --------------------------------- | -------------------------------------------- | ------------------------------------------------ |
| Inferência dos modelos            | `benchmark/scripts/executa_predicao_LLMs.py` | `models_predictions/results_*.json`              |
| Avaliação pelo LLM Judge          | `benchmark/scripts/llm_avaliador.py`         | `judge_evaluations/automatic_evaluations_*.json` |
| Cálculo de Precision, Recall e F1 | `benchmark/scripts/calcula_metrica_judge.py` | `metric_results/prediction_metrics_*.json`       |
| Consolidação do benchmark         | `benchmark/scripts/analise_resultados.py`    | `resultados_benchmark.csv`                       |
| Processamento dos valores CVSS    | `benchmark/scripts/coleta_cvss_scores.py`    | Dados utilizados na análise CVSS                 |
| Orquestração completa             | `benchmark/main.py`                          | Execução integrada das etapas anteriores         |

## 12. Critérios de Sucesso do Teste Mínimo

O teste mínimo é considerado bem-sucedido quando o avaliador consegue verificar a execução completa da pipeline para o modelo `google/gemma-4-e2b`.

Os seguintes artefatos devem estar presentes:

```text
benchmark/
├── models_predictions/
│   └── results_google_gemma-4-e2b.json
│
├── judge_evaluations/
│   └── automatic_evaluations_google_gemma-4-e2b.json
│
├── metric_results/
│   └── prediction_metrics___preditor_google_gemma-4-e2b.json
│
└── debug.log
```

Além da existência dos arquivos, o avaliador deve verificar:

* `correct_format` igual a `true` nas predições;
* presença de `findings_list` nas respostas;
* presença dos campos `finding`, `macro_id` e `justification`;
* presença de `veredito` e `ids_ouro_correspondentes` nas avaliações do Judge;
* geração do arquivo de métricas contendo `precision`, `recall` e `f1`.

Esses critérios permitem verificar objetivamente que o modelo foi executado, que a resposta estruturada foi produzida, que a avaliação pelo Judge foi realizada e que as métricas foram calculadas.

## 13. Fluxo Recomendado para os Avaliadores

Para uma primeira validação do artefato, recomenda-se seguir esta sequência:

```text
1. Criar o ambiente virtual Python
        ↓
2. Instalar benchmark/requirements.txt
        ↓
3. Configurar o LM Studio 0.4.19 Build 2
        ↓
4. Carregar google/gemma-4-e2b
        ↓
5. Verificar MACHINE_URL
        ↓
6. Executar python main.py
        ↓
7. Verificar models_predictions/
        ↓
8. Verificar judge_evaluations/
        ↓
9. Verificar metric_results/
        ↓
10. Validar os campos JSON descritos nesta seção
```

Após a conclusão bem-sucedida do teste mínimo, o avaliador pode substituir `lista_modelos` no `main.py` pelos demais modelos do benchmark e executar a reprodução completa dos experimentos.

Os resultados podem apresentar pequenas variações em relação aos valores reportados no artigo devido a diferenças de hardware, runtime, versões dos modelos e características não determinísticas da inferência. Para minimizar essas diferenças, recomenda-se utilizar as mesmas versões do LM Studio, variantes dos modelos, quantização, prompts, dataset e configuração de temperatura descritas neste README.
