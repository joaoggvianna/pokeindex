# PokéIndex 🐉

Meu primeiro experimento consumindo uma API REST pública com Python, desenvolvido como exercício prático de aprendizado.

## O que faz nesta versão (v0.1)

- Solicita o nome de um Pokémon no terminal.
- Consulta a [PokéAPI](https://pokeapi.co/docs/v2).
- Exibe status HTTP, nome, número, primeiro tipo, altura e peso (nas unidades da API).

## Como executar

Requer Python 3.9+ e conexão com a internet.

```bash
python -m pip install -r requirements.txt
python main.py
```

Em alguns sistemas, use `python3` no lugar de `python`.

## Limitações atuais / próximos passos

- Exibir todos os tipos e as seis estatísticas, não apenas o primeiro tipo.
- Converter decímetros/hectogramas em metros/quilogramas.
- Tratar erros HTTP, nomes inexistentes, timeouts e falhas de conexão.
- Normalizar entrada e ajustar a montagem da URL.

## Aprendizado e autoria

O código inicial foi escrito manualmente como exercício de Python. Documentação e assistência de IA foram usadas para estudar requisições HTTP e navegação de estruturas JSON, não para gerar a implementação original.

Dados fornecidos pela [PokéAPI](https://pokeapi.co/). Este é um projeto de estudo não oficial.
