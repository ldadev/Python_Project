

from itertools import cycle

chars_1 = 'hola'
chars_2 = 'mundo'

char_ = ''
table = {'4':'a','3':'e','1':'i','0':'o','2':'u'}


def comb():


	for key,value in table.items():

		if value in chars_1 or value in chars_2:

			# Reemplazamos si se cumple la condición
			chars_1 = chars_1.replace(value,key).upper()
			chars_2 = chars_2.replace(value,key).lower()

	# Intercalamos chars_1 y chars_2 modificados
	for a,b in zip(cycle(chars_1),chars_2):
		char_+= ''.join((a,b))# Concatenamos las tuplas

	print(char_)




def comb_2():

	chars_1 = 'perros'
	chars_2 = 'mundo'

	char_ = ''
	table = {'4':'a','3':'e','1':'i','0':'o','2':'u'}

	for key,value in table.items():

		if value in chars_1 or value in chars_2:

			# Reemplazamos si se cumple la condición
			chars_1 = chars_1.replace(value,key).upper()
			chars_2 = chars_2.replace(value,key).lower()

	# Intercalamos chars_1 y chars_2 modificados
	for a,b in zip(chars_1,chars_2):
		char_+= ''.join((a,b))# Concatenamos las tuplas


	char_+= chars_2[-1] if len(chars_2) > len(chars_1) else chars_1[-1]

	print(char_)

comb_2()


