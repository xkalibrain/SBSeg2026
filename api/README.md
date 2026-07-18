# API

A nossa API foi desenvolvida para fornecer uma interface de comunicação para utilizar as ferramentas escolhidas do kali linux por meio de requisições HTTP.

## Dependências

A API foi desenvolvida utilizando a linguagem Python e o framework Flask.

| Dependência  | Versão |
| -----------  | ------ |
| Python       | 3.11.9 |
| Flask        | 3.0.3  |
| Flask-Cors   | 4.0.1  |
| blinker      | 1.7.0  |
| click        | 8.1.7  |
| itsdangerous | 2.1.2  |
| Jinja2       | 3.1.3  |
| MarkupSafe   | 2.1.5  |
| Werkzeug     | 3.0.2  |

## Executando a API

Para executar apenas a API utilizando **Docker**, basta executar o comando abaixo:

```bash
docker compose up api
```

Caso não deseje utilizar o Docker, você pode executar a API utilizando o Python. Para isso, você deve instalar as dependências do projeto e executar o arquivo `app.py`:

```bash
pip install -r requirements.txt
python app.py
```

Após executar o comando acima, a API estará disponível em `http://localhost:5001`

## Endpoints

Aqui estão listados os endpoints disponíveis na API e como utilizá-los.

Todas as respostas da API são retornadas no formato text/plain.

### GET /ip

Identificar e retornar o dendereço de ip relacionado a um domínio.

Recebe como parâmetro:
- host: string


### GET /whatweb

Retorna informações gerais sobre o site como tecnologias utilizadas, cabeçalhos, etc.

Recebe como parâmetro:
- url: string


### GET /reverse_dns

Retorna informações sobre o DNS reverso do domínio relacionado a um ip, bem como outros ips relacionados.

Recebe como parâmetro:
- ip: string


### GET /sub_dns

Retorna informações sobre subdomínios e sistemas integrados de um domínio.

Recebe como parâmetro:
- host: string


### GET /whois

Retorna informações sobre o domínio relacionado a um ip, bem como informações de contato.

Recebe como parâmetro:
- ip: string


### GET /banner

Retorna todas as informações da resposta de um site, incluindo cabeçalhos, cookies, certificados, etc.

Recebe como parâmetro:
- url: string


### GET /directory_scan

Realiza um scan em um domínio em busca de diretórios e arquivos ocultos.

Recebe como parâmetro:
- ip: string


### GET /ports

Realiza um scan em um domínio em busca de portas abertas.

Recebe como parâmetro:
- ip: string
