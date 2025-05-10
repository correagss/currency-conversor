# Conversor de Moedas

Este é um projeto simples e prático desenvolvido em **Python** com **FastAPI**, criado para realizar conversões entre moedas em tempo real. Ele consulta cotações diretamente da API externa [Alpha Vantage](https://www.alphavantage.co/), oferecendo precisão e atualização constante.

O sistema é estruturado com boas práticas de organização (rotas separadas, validações com Pydantic e lógica modularizada), servindo como um ótimo ponto de partida para quem está aprendendo **FastAPI**, integração com APIs externas e desenvolvimento de APIs REST.

Ideal para fins de estudo, testes com requisições assíncronas e aplicações que envolvem conversão de moedas.

##Funcionalidades

- Seleção de moeda de origem e destino.
- Atualização dinâmica das opções de moeda de destino com base na moeda de origem
selecionada.
- Exibição da taxa de câmbio atualizada entre as moedas selecionadas, obtida através da Alphavantage

## Tecnologias utilizadas

- Python
- [Alphavantage] (https://www.alphavantage.co/documentation/) (para obter as cotações)
- Insomnia (para testar a API)


## Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente:


### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/conversor-de-moedas.git
cd conversor-de-moedas


### 2. Instale as dependências

pip install -r requirements.txt

### 3. Execute o servidor FastAPI

uvicorn main:app --reload

### 4. Acesse a API no navegador

API: http://127.0.0.1:8000

Documentação Swagger: http://127.0.0.1:8000/docs
