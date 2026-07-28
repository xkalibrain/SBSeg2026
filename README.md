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

# Como o xKaliBrain Funciona

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

Atualmente o xKaliBrain oferece:

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

O xKaliBrain foi projetado em uma arquitetura modular composta por diferentes componentes independentes.

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

# Organização do Repositório

O repositório foi organizado de forma a facilitar tanto a utilização da plataforma quanto a reprodução dos experimentos científicos apresentados no artigo.

```text
xKaliBrain/
│
├── benchmark/          # Scripts para execução do benchmark
├── dataset/            # Conjunto de dados utilizado na pesquisa
├── docs/               # Documentação adicional
├── examples/           # Exemplos de utilização
├── inference/          # Scripts de inferência
├── models/             # Configurações dos modelos
├── prompts/            # Prompts utilizados pelo xKaliBrain
├── reports/            # Relatórios OSINT de exemplo
├── results/            # Resultados experimentais
├── scripts/            # Scripts auxiliares
├── web/                # Web xKaliBurr
├── README.md
├── requirements.txt
└── LICENSE
```

Cada um desses diretórios será detalhado nas próximas seções deste documento.

---

# Modelos Avaliados

O estudo experimental apresentado no artigo avaliou **15 Grandes Modelos de Linguagem Open-Weight**, abrangendo diferentes arquiteturas, tamanhos e famílias de modelos.

Os modelos pertencem às seguintes famílias:

- Gemma;
- Qwen;
- Llama;
- DeepSeek;
- Phi;
- GPT-OSS.

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

Essas ferramentas são executadas automaticamente pela plataforma Web xKaliBurr durante a geração dos relatórios utilizados posteriormente pelo xKaliBrain.

# Estrutura Geral do Projeto

Após a instalação, o repositório possui uma organização semelhante à apresentada abaixo.

```text
xKaliBrain/

├── benchmark/
│   ├── scripts/
│   ├── metrics/
│   └── results/
│
├── dataset/
│   ├── reports/
│   ├── labels/
│   └── metadata/
│
├── prompts/
│
├── inference/
│
├── models/
│
├── docs/
│
├── examples/
│
├── web/
│
├── requirements.txt
│
└── README.md
```

Cada diretório foi organizado para facilitar tanto a utilização da plataforma quanto a reprodução dos experimentos científicos.

---

# Instalação

## 1. Clonando o Repositório

Clone o repositório oficial.

```bash
git clone https://github.com/xKaliBurr/xKaliBrain.git
```

Entre no diretório.

```bash
cd xKaliBrain
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

O agente utiliza como entrada relatórios produzidos pelo Web xKaliBurr.

Caso deseje reproduzir integralmente o fluxo apresentado no artigo, execute também a instalação da plataforma.

Entre no diretório.

```bash
cd web
```

Inicie os containers.

```bash
docker compose up -d
```

Aguarde a inicialização completa.

Verifique:

```bash
docker ps
```

Todos os serviços deverão estar em execução.

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

## Testando a API

Com o LM Studio em execução, execute:

```bash
python examples/test_connection.py
```

Resultado esperado:

```text
Connection established.

Model loaded successfully.

Waiting for requests...
```

Caso ocorra erro de conexão, verifique:

- servidor iniciado;
- porta configurada;
- modelo carregado.

---

# Primeiro Teste

Antes de executar os experimentos completos, recomenda-se realizar um teste mínimo.

Utilize um dos relatórios disponibilizados em:

```text
reports/examples/
```

Execute:

```bash
python inference/run_inference.py \
--input reports/examples/example_report.txt
```

O processamento deverá durar apenas alguns segundos.

Ao término será produzido um relatório estruturado semelhante a:

```text
Vulnerabilidade Identificada

Software Desatualizado

Categoria Macro

MACRO 03

OWASP

A06

CVSS

HIGH

Recomendação

Atualizar componente para versão suportada.
```

Esse teste confirma que:

- o ambiente foi instalado corretamente;
- o LM Studio está operacional;
- o modelo carregado responde adequadamente;
- o pipeline de interpretação encontra-se funcional.

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

Esses relatórios constituem a entrada do xKaliBrain.

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

# Modelos Avaliados

Foram avaliados quinze Grandes Modelos de Linguagem pertencentes às seguintes famílias:

## Gemma

- Gemma 3
- Gemma 4

---

## Qwen

- Qwen 3
- Qwen 3 Coder

---

## Llama

- Llama 3
- Llama 3.1
- Llama 3.2

---

## DeepSeek

- DeepSeek R1
- DeepSeek V3

---

## Phi

- Phi-4

---

## GPT-OSS

- GPT-OSS


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

Os experimentos encontram-se organizados conforme a estrutura abaixo.

```text
benchmark/

├── models/
├── prompts/
├── reports/
├── outputs/
├── metrics/
├── scripts/
└── results/
```

Cada diretório possui uma finalidade específica.

| Diretório | Descrição |
|------------|-----------|
| models | Configurações dos modelos |
| prompts | Prompts utilizados |
| reports | Relatórios OSINT |
| outputs | Respostas produzidas |
| metrics | Resultados das métricas |
| scripts | Scripts de benchmark |
| results | Resultados finais |

---

# Reproduzindo os Experimentos

Após configurar corretamente o ambiente, a reprodução do benchmark pode ser realizada executando:

```bash
python benchmark/run_benchmark.py
```

O script executará automaticamente todos os modelos configurados.

Ao término serão produzidos:

- respostas individuais;
- métricas;
- arquivos CSV;
- tabelas comparativas;
- resultados agregados.

Todos os resultados serão armazenados em:

```text
benchmark/results/
```

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
