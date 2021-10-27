# Plataforma de consulta de cashback dos revendedores

## Sumário

1. [Resumo](#resumo)
1. [Documentação das APIs](#documentação-das-apis)
1. [Instalação](#instalação)
1. [Início Rápido](#início-rápido)

## Resumo

Este repositório possui o código do backend da consulta de cashback dos revendedores

## Documentação das APIs

- Production: https://reseller-cashback.herokuapp.com/doc/swagger/

## Instalação

### Pré-requisitos da Instalação

* Pré-requisitos necessários do [Sistema](docs/setup/pre-requisitos.md)
* Instalação do [ambiente de desenvolvimento](docs/setup/environment.md)
* Configuração das [variáveis de ambiente do projeto](docs/setup/configuracoes.md)

### Instalação do projeto

1. `make dependencies` : instalar as deps Python usando poetry
2. `make docker-dependencies`: sobe container com os serviços necessários

### Execução dos testes
Para conferir a instalação precisa executar todos os [testes](docs/setup/testes.md)

## Início Rápido

Todas as tarefas estão concentradas no `Makefile`, para uma primeira visão: `make help`.

### Usando o ambiente

Durante o desenvolvimento os seguintes comando são usados:

- `make check-code`: Formata o código de acordo com o isort e black e também roda o flake8 e mypy
- `make checks`: Executa o check-code e também executa checagens de segurança
- `make tests`: Roda os testes unitários
- `make tests-matching k="<expression>"`: Roda os testes utilizando o parâmetro `-k` do pytest (filtra os testes por nome do teste, da classe ou do arquivo. Mais informações em `poetry run pytest -h | grep '\-k EXPRESSION' -A 13`.)
