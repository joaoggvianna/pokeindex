# PokéIndex

Buscador de Pokémon no terminal, desenvolvido em Python para praticar consumo de APIs REST, requisições HTTP e manipulação de dados JSON.

**Status:** MVP funcional, em evolução.

## Funcionalidades implementadas

- Consulta de Pokémon pelo nome informado pelo usuário.
- Busca de dados na [PokéAPI](https://pokeapi.co/docs/v2) utilizando `requests`.
- Exibição do nome e número na Pokédex Nacional.
- Exibição de todos os tipos, separados por vírgula.
- Conversão da altura para metros e do peso para quilogramas.
- Exibição das seis estatísticas base (HP, Attack, Defense, Special Attack, Special Defense e Speed).
- Mensagem explicativa quando a PokéAPI responde com HTTP 404 (Pokémon não encontrado).
- Organização da inicialização em uma função `main()`.

## Tecnologias

- Python
- Biblioteca `requests`
- PokéAPI (API REST pública)
- JSON

## Como executar

Tenha o Python instalado e uma conexão com a internet. No terminal:

```bash
git clone https://github.com/joaoggvianna/pokeindex.git
cd pokeindex
python -m pip install requests
python main.py
```

Em alguns sistemas, use `python3` no lugar de `python`.

O programa solicitará o nome de um Pokémon (por exemplo, `charizard`) e exibirá as informações retornadas pela API.

### Exemplo de saída

```text
Seja bem vindo ao POKÉINDEX!
Aqui você pode consultar as informações de qualquer Pokémon da Pokédex Nacional.
Digite o nome do pokemon: charizard
Nome: charizard
Número na Pokédex: 6
Tipos: fire, flying
Altura: 1.7m
Peso: 90.5kg
====STATUS BASE====
hp: 78
attack: 84
defense: 78
special-attack: 109
special-defense: 85
speed: 100
```

## Progresso

- [x] Consultar dados pela PokéAPI.
- [x] Exibir informações básicas e as seis estatísticas base.
- [x] Exibir todos os tipos em uma única linha.
- [x] Converter altura e peso para unidades usuais.
- [x] Exibir mensagem de erro para Pokémon não encontrado (HTTP 404).
- [x] Separar a inicialização na função `main()`.
- [ ] Normalizar a entrada (maiúsculas/minúsculas e espaços).
- [ ] Tratar falhas de conexão, timeout e outros erros HTTP.
- [ ] Permitir múltiplas consultas sem reiniciar o programa.
- [ ] Criar testes automatizados.

> O tratamento de erros ainda é parcial: o código verifica respostas 200 e 404, mas não captura exceções de rede nem apresenta mensagens específicas para outros códigos HTTP.

## Sobre o projeto

Este projeto foi iniciado como exercício prático de programação em Python, com implementação manual para consolidar conhecimentos de funções, listas, dicionários, laços de repetição, requisições HTTP e estruturas JSON. A documentação foi elaborada com apoio de IA.

Projeto educacional não oficial. Dados fornecidos pela [PokéAPI](https://pokeapi.co/).
