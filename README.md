# xKaliBrain

<p align="center">
  <img src="docs/images/xkalibrain_logo.png" width="220">
</p>

<p align="center">
  <strong>xKaliBrain: An Open-Weight LLM for Vulnerability Detection and Classification in Online Environments</strong>
</p>

---

## Resumo

Este repositório contém o artefato oficial do artigo:

> **xKaliBrain: Um Modelo LLM Open-Weight para Detecção e Classificação de Vulnerabilidades em Ambientes Online**, publicado no SBSeg 2026.

O xKaliBrain é um modelo de linguagem especializado em interpretação automática de relatórios técnicos de cibersegurança produzidos pelo Web xKaliBurr. O sistema realiza identificação de vulnerabilidades, classificação em categorias Macro, priorização baseada em OWASP Top 10 e atribuição de níveis de severidade utilizando o CVSS v3.1.

Este repositório disponibiliza todos os componentes necessários para reproduzir os principais experimentos descritos no artigo, incluindo:

- Código-fonte do Web xKaliBurr;
- Código-fonte do xKaliBrain;
- Relatórios utilizados nos experimentos;
- Prompts;
- Scripts de inferência;
- Scripts de benchmark;
- Exemplos de entrada e saída;
- Dataset utilizado na avaliação;
- Resultados obtidos durante os experimentos.

---

# Estrutura do README.md

Este README está organizado da seguinte forma:

1. Selos considerados;
2. Informações básicas;
3. Dependências;
4. Preocupações com segurança;
5. Instalação;
6. Teste mínimo;
7. Experimentos;
8. Estrutura do repositório;
9. Licença.

---

# Selos Considerados

Os selos considerados para avaliação do artefato são:

- Disponível;
- Funcional;
- Reproduzível;
- Sustentável.

---

# Informações Básicas

## Ambiente de execução

O artefato foi desenvolvido e validado utilizando:

| Componente | Versão |
|----------|--------|
| Ubuntu | 24.04 LTS |
| Python | 3.12 |
| Docker | 28+ |
| Docker Compose | 2+ |
| LM Studio | 0.4.19 |
| Git | 2.43+ |

## Requisitos mínimos de hardware

| Recurso | Mínimo |
|---------|--------|
| CPU | 4 núcleos |
| RAM | 8 GB |
| Disco | 10 GB livres |
| GPU | Opcional |

## Requisitos recomendados

| Recurso | Recomendado |
|---------|-------------|
| CPU | 8 núcleos |
| RAM | 16 GB |
| Disco | 20 GB livres |
| GPU | 8 GB VRAM |

---

# Dependências

## Web xKaliBurr

O Web xKaliBurr utiliza as seguintes ferramentas:

- Nmap;
- DNSRecon;
- Gobuster;
- Dirb;
- WhatWeb;
- Curl;
- Whois.

## xKaliBrain

Dependências Python:

- requests;
- pandas;
- tqdm;
- scikit-learn;
- numpy;
- matplotlib.

Instalação:

```bash
pip install -r requirements.txt
```

## Modelo LLM

Os experimentos do artigo foram realizados utilizando:

- Gemma-4-E2B;
- Gemma-4-26B-A4B;
- Qwen3.6-35B-A3B;
- GPT-OSS-120B;
- Mistral-7B-Instruct-v0.2.

Caso o avaliador deseje apenas validar a execução do artefato, qualquer modelo compatível com o LM Studio pode ser utilizado.

---

# Preocupações com Segurança

O Web xKaliBurr executa atividades de reconhecimento utilizando ferramentas tradicionais de pentest.

Recomenda-se:

- utilizar exclusivamente ambientes autorizados;
- não executar a ferramenta contra infraestruturas de terceiros;
- utilizar apenas os relatórios já disponibilizados no repositório para reprodução dos experimentos do artigo.

A reprodução completa dos resultados apresentados no artigo **não exige a execução de varreduras externas**, sendo suficiente utilizar os relatórios previamente coletados.

---

# Instalação

## Clonar o repositório

```bash
git clone https://github.com/xKaliBurr/xKaliBrain.git
cd xKaliBrain
```

---

## Instalar dependências Python

```bash
pip install -r requirements.txt
```

---

## Instalar Docker

Ubuntu:

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
```

---

## Iniciar o Web xKaliBurr

```bash
docker compose up -d
```

---

## Instalar LM Studio

Instale o LM Studio:

https://lmstudio.ai/

Carregue um modelo compatível e habilite o servidor local.

---

# Teste Mínimo

O objetivo deste teste é verificar se o ambiente foi instalado corretamente.

## Passo 1

Inicie o servidor local do LM Studio.

---

## Passo 2

Carregue um modelo.

---

## Passo 3

Execute:

```bash
python examples/minimal_test.py
```

---

## Resultado esperado

A saída deverá conter:

```text
MACRO 01
MACRO 03
CVSS: HIGH
```

ou resultado equivalente.

Tempo esperado:

- menos de 2 minutos.

---

# Experimentos

## Reivindicação #1 — Execução do xKaliBrain

Objetivo:

Demonstrar que o xKaliBrain consegue interpretar relatórios técnicos do Web xKaliBurr.

### Comando

```bash
python inference.py \
--input reports/example_report.txt
```

### Tempo esperado

2 minutos.

### Resultado esperado

- identificação das vulnerabilidades;
- classificação Macro;
- severidade CVSS.

---

## Reivindicação #2 — Reprodução do Benchmark

Objetivo:

Reproduzir os resultados do benchmark apresentados na Seção 5 do artigo.

### Comando

```bash
python benchmark/run_benchmark.py
```

### Tempo esperado

20–30 minutos.

### Resultado esperado

Geração automática de:

- Precision;
- Recall;
- F1-Score;
- Tempo médio de inferência.

---

## Reivindicação #3 — Pipeline Completo

Objetivo:

Executar o fluxo completo:

```text
Web xKaliBurr
        ↓
Relatório Técnico
        ↓
xKaliBrain
        ↓
Categorias Macro
        ↓
CVSS
        ↓
Relatório Final
```

### Comando

```bash
python pipeline.py
```

### Tempo esperado

5 minutos.

---

# Estrutura do Repositório

```text
xKaliBrain/
│
├── benchmark/
├── dataset/
├── docs/
├── examples/
├── inference/
├── models/
├── prompts/
├── reports/
├── results/
├── scripts/
├── web_xkaliburr/
├── requirements.txt
└── README.md
```

---

# Como Citar

```bibtex
@inproceedings{barros2026xkalibrain,
  title={xKaliBrain: Um Modelo LLM Open-Weight para Detecção e Classificação de Vulnerabilidades em Ambientes Online},
  author={Barros, Daniel Rezende and others},
  booktitle={Simpósio Brasileiro de Segurança da Informação e de Sistemas Computacionais},
  year={2026}
}
```

---

# LICENSE

Este projeto está licenciado sob os termos da licença MIT.

Consulte o arquivo:

```text
LICENSE
```

para mais detalhes.
