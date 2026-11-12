# POKÉINDEX - Programa para consultar as informações de qualquer Pokémon da Pokédex Nacional
# Projeto idealizado para aprendizado de conexão e consumo de APIs, utilizando a PokeAPI para
# desenvolvimento e consulta dos dados de cada Pokémon.
# O programa solicita ao usuário o nome da espécie e retorna as informações básicas do Pokémon
# como: nome, número na Pokédex, tipos, altura, peso e status base.
# importante:
# #print(poke_dados.keys()) ## essas é a lista de chaves de todos os dados de qualquer pokemon

import requests ##sempre fazer requisições com a biblioteca requests
import pprint #para ficar bonito e facil de ler conteúdo de dicionários e listas

url_base = "https://pokeapi.co/api/v2/"

def pegar_info_pokemon(nome):
    url = f"{url_base}pokemon/{nome}"
    response = requests.get(url)
    #print(response.status_code) - isso aqui serve apenas para teste, deixar no produto final é feio.
    if response.status_code == 200:
        poke_dados = response.json()
        lista_tipos = []
        print(f'Nome: {poke_dados["name"]}')
        print(f'Número na Pokédex: {poke_dados["id"]}')
        for tipo in poke_dados["types"]:
            lista_tipos.append(tipo['type']['name'])
        separador = ', '
        tipagem_final = separador.join(lista_tipos)
        print(f'Tipos: {tipagem_final}')
        print(f'Altura: {poke_dados["height"]/10}m')
        print(f'Peso: {poke_dados["weight"]/10}kg')
        print('====STATUS BASE====')
        for stat in poke_dados["stats"]:
            atributo = stat["stat"]["name"]
            valor = stat["base_stat"]
            print(f'{atributo}: {valor}')
    elif response.status_code == 404:
        print('ERRO: Pokémon não encontrado. Verifique se digitou o nome corretamente e tente novamente.')
def main():
    print('Seja bem vindo ao POKÉINDEX!')
    print('Aqui você pode consultar as informações de qualquer Pokémon da Pokédex Nacional.')
    nome = input("Digite o nome do pokemon: ")
    pegar_info_pokemon(nome)


main()
