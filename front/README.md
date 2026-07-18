# Front

O nosso front-end é uma ferramenta web que permite ao usuário, de forma simples e intuitiva, passar um alvo para ser analisado, bastando apenas informar a url do mesmo.
Após a analise, as informações serão apresentadas de forma clara, trazendo dicas para uma melhor compreensão do que é mostrado.

## Dependências

O front foi criado usando a linguagem Typescript e o framework Nextjs.

Para a execução do Nextjs:

Nodejs - 20.11.0

Dependencias do next:

| Dependência        | Versão |
| ------------------ | ------ |
| next               | 14.2.3 |
| react              | 18     |
| react-dom          | 18     |
| react-icons        | 5.2.1  |
| typescript         | 5      |
| eslint             | 8      |
| eslint-config-next | 14.2.3 |
| postcss            | 8      |
| tailwindcss        | 3.4.1  |

## Executando o Front

Para executar o front, você primeiro deve copiar o arquivo .env.template com o nome .env.local, para carregar as variáveis de ambiente no front. Ele já está configurado para se comunicar com a API localmente.

Depois, basta rodar o comando:

```bash
docker compose up front
```

Caso se queira executar o front sem o docker, inicialmente seíra necessário fazer a instalação das dependência usando o comando:

```bash
npm install
```

Após isso, caso se queira testar em um ambiente de desenvolvimento:

```bash
npm run dev
```

Já para um ambiente de produção:

```bash
npm run build

npm run star
```

Após isso o front ficara disponível em
`http://localhost:3000`

Dito isso, sem a api, tentar fazer uma analise resultará em um erro.