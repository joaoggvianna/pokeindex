import requests ##sempre fazer requisições com a biblioteca requests
import pprint #para os dados brutos ficarem fáceis de ler

url_base = "https://pokeapi.co/api/v2/"

def pegar_info_pokemon(nome):
    url = f"{url_base}/pokemon/{nome}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        poke_dados = response.json()
        print(f'Nome: {poke_dados["name"]}')
        print(f'Número na Pokédex: {poke_dados["id"]}')
        print(f'Tipos: {poke_dados["types"][0]["type"]["name"]}')        
        print(f'Altura: {poke_dados["height"]}')
        print(f'Peso: {poke_dados["weight"]}')
        print('STATUS BASE:')
        for stat in poke_dados["stats"]:
            atributo = stat["stat"]["name"]
            valor = stat["base_stat"]
            print(f'{atributo}: {valor}')
        #print(poke_dados.keys()) ## essas é a lista de chaves de todos os dados de qualquer pokemon


nome = input("Digite o nome do pokemon: ")
pegar_info_pokemon(nome)
