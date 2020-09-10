import requests

def test_pokemon():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url =  "https://pokeapi.co/api/v2/pokemon/ditto"

    resposta = requests.get(url,headers=headers)
    result = resposta.json()

    if resposta.status_code == 200:
        pokemon_id = result['id']
        pokemon_name = result['name']
        pokemon_types = result['types']
        pokemon_index = pokemon_types[0]
        pokemon_type = pokemon_index['type']
        pokemon_type_name =pokemon_type['name']

        assert pokemon_id == 132 and pokemon_name == 'ditto' and pokemon_type_name == 'normal'
    else:
        assert False