import requests ##sempre fazer requisições com a biblioteca requests
import pprint #para ficar bonito e facil de ler

url_base = "https://pokeapi.co/api/v2/"

def pegar_info_pokemon(nome):
    url = f"{url_base}/pokemon/{nome}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        poke_dados = response.json()
        pprint.pprint(f'Nome: {poke_dados["name"]}')
        pprint.pprint(f'Número na Pokédex: {poke_dados["id"]}')
        pprint.pprint(f'Tipos: {poke_dados["types"][0]["type"]["name"]}')        
        pprint.pprint(f'Altura: {poke_dados["height"]}')
        pprint.pprint(f'Peso: {poke_dados["weight"]}')
        #pprint.pprint(f'Stats: {poke_dados["stats"][0]["base_stat"]}') #so apareceu o primeiro stat, preciso ver como fazer para aparecer o nome do stat e o valor.
        #pprint.pprint(poke_dados.keys()) ## essas é a lista de chaves de todos os dados de qualquer pokemon


nome = input("Digite o nome do pokemon: ")
pegar_info_pokemon(nome)
