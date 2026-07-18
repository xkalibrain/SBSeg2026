# Web xKaliBurr

Projeto para o Salão de Ferramentas do evento SBSeg2024

O Web xKaliBurr é uma ferramenta exploratória para sistemas web e tem como objetivo principal auxiliar os profissionais de segurança durante a realização da etapa de levantamento de informações em um pentest web atráves de uma plataforma mais amigável e intuitiva.

A ferramenta fornece informações valiosas como:
* Identificação de endereços IP, Serviço DNS e Sub-sistemas Integrados.
* Identificação e versionamento de serviço nas portas de rede.
* Diretório ocultos.

Veja mais detalhes de [Como xKaliBurr funciona](/docs/workflow.md).

## Estrutura do Projeto

A nossa ferramenta é composta por uma API e um Front-end web que se comunicam entre si.

A API serve como uma interface de rede para executar as ferramentas de pentest do kali linux.

O Front-end é uma ferramenta web que permite o usuário realizar ações de pentest através de uma interface gráfica para simplificar seu uso.

Por fim, utilizamos o docker para facilitar a execução da ferramenta.

Você pode conferir mais sobre a [API](api/README.md) e o [Front-end](front/README.md).

### Dependências

Para executar a ferramenta de forma simples, você precisa apenas ter o docker e o docker-compose instalados em sua máquina. Caso queria rodar a ferramenta sem o docker, você precisará instalar as dependências de cada projeto, que estão listadas em seus respectivos READMEs.

| Dependência    | Versão |
| -------------- | ------ |
| Docker         | 26.1.4 |
| Docker-Compose | 2.27.1 |

### Ambiente

A ferramenta foi desenvolvida e testada tanto no Windows 10 quanto no Ubuntu 20.04.2 LTS. Além disso, a ferramenta foi testada nos navegadores Google Chrome e Firefox.

Por fim, também configuramos imagens Docker para facilitar a execução da ferramenta em qualquer ambiente.

## Executando a ferramenta

Para executar a ferramenta, você precisa ter o Docker e o Docker Compose instalados em sua máquina. Além disso, caso queria rodar no windows é necessário ativar a feature "host networking" que está em beta.

Se você estiver no linux pode usar o nosso script de setup `./setup.sh` para facilitar sua instalação. Caso vá rodar localmente (recomendado) não precisa alterar nenhuma variável de ambiente padrão.
(Script testado no Ubuntu 22.04)

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

Após a execução do comando, a ferramenta estará disponível em `http://localhost:3000`.

## Usando a ferramenta

Para usar a ferramenta, basta acessar o endereço `http://localhost:3000`. A ferramenta é bem intuitiva e possui uma interface bem simples, basta preencher o campo com o endereço do site que deseja fazer o pentest e clicar no botão "Realizar Análise".

Após isso, você será redirecionado para a página de resultados, onde verá primeiro um estado de loading enquanto a ferramenta executa os comandos (pode levar um tempo considerável).

Após a análise ser concluida, você verá os resultados da análise separados em 4 abas: "Informações Gerais", "Diretórios e páginas sensíveis", "Serviços e portas de rede" e "Domínios vizinhos".

Por fim, você pode baixar o relatório com todos os resultados em um arquivo .txt no botão "Download da análise".
