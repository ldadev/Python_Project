# Convierte la primera letra en mayuscula de una palabra ó una frase
from utility import *

def fUpper():

	words = list(valid_string())# Validamos la entrada del usuario

	for index,letter in enumerate(words):

		if not letter == ' ':
			words[0] = words[0].upper()
		else:
			words[index + 1] = words[index + 1].upper()
	print(''.join(words)) 

fUpper()


def fupper_2():

	user_word = valid_string()
	return user_word.title()

print(fupper_2())
		




