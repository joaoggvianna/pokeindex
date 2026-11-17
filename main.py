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
    try:
        response = requests.get(url, timeout = 5) #timeout é um parâmetro que mede o tempo de resposta da API, se passar desse tempo, o programa retorna um erro.
        #print(response.status_code) - isso aqui serve apenas para teste, deixar no produto final é feio.
        if response.status_code == 200:
            poke_dados = response.json()
            nome_formatado = poke_dados["name"].replace('-', ' ').title() #a api usa hifen e nao o espaco, .title é para deixar a primeira letra maiuscula
            lista_tipos = []
            habilidades = []
            print('====INFORMAÇÕES DO POKÉMON====')
            print(f'Nome: {nome_formatado}')
            print(f'Número na Pokédex: {poke_dados["id"]}')
            for habilidade in poke_dados["abilities"]:
                habilidades.append(habilidade["ability"]["name"].title())
            print(f'Habilidade: {", ".join(habilidades)}')
            separador = ', '
            for tipo in poke_dados["types"]:
                lista_tipos.append(tipo["type"]["name"])
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
        elif response.status_code == 500:
            print('ERRO: Problema interno no servidor da PokeAPI. Tente novamente mais tarde.')
        elif response.status_code == 503:
            print('ERRO: A API está temporariamente indisponível. Tente novamente mais tarde.')
    except requests.exceptions.Timeout:
        print('O tempo de resposta da API excedeu o limite. Tente novamente mais tarde.')
    except requests.exceptions.ConnectionError:
        print("ERRO: A conexão com a API falhou. Verifique a sua conexão com a internet e tente novamente.")
        
def main():
    print('Seja bem vindo ao POKÉINDEX!')
    print('Aqui você pode consultar as informações de qualquer Pokémon da Pokédex Nacional.')
    nome = input("Digite o nome do pokemon: ").strip().lower()
    pegar_info_pokemon(nome)


main()