# PokéIndex

Buscador de informações de Pokémon desenvolvido em Python para praticar consumo de APIs REST, leitura de JSON e estruturas de repetição.

**Status:** MVP funcional — versão de estudo, com melhorias planejadas.

## Funcionalidades implementadas

- Consulta de Pokémon pelo nome digitado no terminal.
- Requisição HTTP à [PokéAPI](https://pokeapi.co/docs/v2) com a biblioteca `requests`.
- Exibição do código de status HTTP da resposta.
- Exibição de nome, número na Pokédex, primeiro tipo, altura e peso.
- Exibição das seis estatísticas base por meio de um laço de repetição: HP, Attack, Defense, Special Attack, Special Defense e Speed.

> A altura e o peso são apresentados nas unidades originais da API (decímetros e hectogramas). Atualmente, apenas o primeiro tipo é exibido.

## Tecnologias

- Python
- Requests
- PokéAPI (API REST pública)
- JSON

## Como executar

É necessário ter Python 3.9+ e conexão com a internet.

```bash
git clone https://github.com/joaoggvianna/pokeindex.git
cd pokeindex
python -m pip install -r requirements.txt
python main.py
```

Em alguns sistemas, substitua `python` por `python3`. Digite o nome de um Pokémon quando solicitado.

## Estado atual e próximos passos

O fluxo principal de consulta e apresentação dos dados está implementado. Ainda não há tratamento completo de erros nem testes automatizados documentados.

- [x] Receber o nome de um Pokémon pelo terminal.
- [x] Consultar a PokéAPI.
- [x] Ler a resposta JSON.
- [x] Mostrar informações básicas.
- [x] Percorrer e mostrar as seis estatísticas base.
- [ ] Exibir todos os tipos de Pokémon.
- [ ] Converter altura para metros e peso para quilogramas.
- [ ] Normalizar a entrada do usuário (espaços e maiúsculas/minúsculas).
- [ ] Tratar Pokémon inexistente, falhas HTTP, timeout e problemas de conexão.
- [ ] Ajustar a montagem da URL para evitar barras duplicadas.
- [ ] Criar testes automatizados para os principais cenários.

## Objetivo de aprendizado

O projeto foi iniciado como exercício de programação manual em Python, com foco em compreender requisições HTTP, dicionários, listas e iteração sobre dados JSON. A documentação conta com assistência de IA, sem atribuir à IA a autoria da implementação original.

Este é um projeto educacional não oficial. Os dados são fornecidos pela [PokéAPI](https://pokeapi.co/).
