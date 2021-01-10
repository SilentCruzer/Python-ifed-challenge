import pokebase as pb 
import requests,json

def ability(name):
	res = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(name))
	data = json.loads(res.text)
	abilities = []
	for values in data['abilities']:
		abilities.append(values['ability']['name'])
	return abilities
