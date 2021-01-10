import PySimpleGUI as sg 
import get_data as pk

layout = [[sg.Text("Enter pokemon: ")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]
window = sg.Window('Pokedex',layout)
while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	pokeName = values['-INPUT-']
	sg.popup('Name:',pokeName,
		'Type: ', pk.getType(pokeName),
		'Weakness: ',pk.get_weakness(pokeName),
		'Weak against: ',pk.get_damage_pokemon(pokeName),
		'Abilities: ',pk.ability(pokeName)
		)

window.close()
