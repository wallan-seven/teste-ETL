# Projeto ETL – Conversão de KG para Sacos

## Descrição

Projeto simples de **ETL em Python** que lê dados de clientes a partir de um arquivo CSV, converte o saldo de **quilogramas (kg) para sacos** e gera um novo CSV com os dados tratados.

---

## Objetivo

* Ler dados de clientes em CSV
* Converter saldo de kg para sacos (1 saco = 60 kg)
* Gerar um novo arquivo CSV com os valores convertidos

---

## Regra de Conversão

* 1 saco = 60 kg

Cálculos:

* sacos = saldo_kg / 60
* sacos_inteiros = saldo_kg // 60
* resto_kg = saldo_kg % 60

---

## Tecnologias

* Python 3
* Pandas


## O que foi praticado

* Conceito de ETL (Extract, Transform, Load)
* Leitura e escrita de arquivos CSV
* Transformação de dados com Pandas
* Organização de código em funções



O projeto foi desenvolvido e utilizado apoio do CHATGPT para correções e ajustes em erros do código.

