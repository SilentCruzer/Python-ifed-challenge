import pokebase as pb 
import requests,json

def getType(name):
	"""
	Returns the type of the input pokemon

	Parameters:
	------------
	name : str

	Returns:
	-----------
	list of all types of the input pokemon
	"""
	type_response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(name))
	text = json.loads(type_response.text)
	type_name = []
	for item in text['types']:
		type_name.append(item['type']['name'])
	return type_name

def getType_url(name):
	"""
	Returns the api url of the input pokemon types.

	Parameters:
	------------
	name : str

	Returns:
	-----------
	list of all url for types
	"""
	type_response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(name))
	text = json.loads(type_response.text)
	type_url = []
	for item in text['types']:
		type_url.append(item['type']['url'])
	return type_url

def get_weakness(name):
	"""
	Returns the types that the input pokemon is weak against.

	Parameters:
	------------
	name : str

	Returns:
	-----------
	list of all the types the input pokemon is weak against
	"""
	urls = getType_url(name)
	weak_types = []
	for link in urls:
		affect_res = requests.get(link)
		affect_json = json.loads(affect_res.text)
		for values in affect_json['damage_relations']['double_damage_from']:
			weakness = values['name']
			weak_types.append(weakness)
	return weak_types

def get_damage_pokemon(name):
	"""
	Returns the name of the pokemons that the input pokemon is weak against

	Parameters:
	------------
	name : str

	Returns:
	-----------
	list of the names of pokemon the input pokemon is weak against
	"""
	types = get_weakness(name)
	pokemons  = []
	for type in types:
		count = 0
		strong_response = requests.get('https://pokeapi.co/api/v2/type/{}/'.format(type))
		strong_json = json.loads(strong_response.text)
		for data in strong_json['pokemon']:
			pokemons.append(data['pokemon']['name'])
			count+=1
			if count >= 5:
				break
	return pokemons

def ability(name):
	"""
	Returns the abilities of the input pokemon

	Parameters:
	------------
	name : str

	Returns:
	-----------
	list of all the abilities of input pokemon
	"""
	res = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(name))
	data = json.loads(res.text)
	abilities = []
	for values in data['abilities']:
		abilities.append(values['ability']['name'])
	return abilities

