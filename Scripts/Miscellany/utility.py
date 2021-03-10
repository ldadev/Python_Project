import os


def clear_screen():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")


def exit_choices():

	choices=input('r:Reiniciar ó enter:salir>>').lower() or exit()
	if choices == 'r':return True


def valid_int():

	while True:
		number = input('Ingresa>>') or exit()
		try:
			if int(number) > 0:
				return int(number)
			else:
				clear_screen()
				print('Sólo números enteros positivos. Intentalo de nuevo.')
		except:
			clear_screen()
			print('Entrada invalida. Sólo números enteros.')

def valid_float():


	while True:
		number = input('Ingresa>>') or exit()
		try:
			if float(number) > 0:
				return float(number)
			else:
				clear_screen()

				print('Sólo números enteros positivos. Intentalo de nuevo.')

				print('Sólo números decimales positivos. Intentalo de nuevo.')

		except:
			clear_screen()
			print('Entrada invalida.Intentalo de nuevo.')

def valid_float_mix():

	while True:
		number = input('Ingresa>>') or exit()
		try:
			a,b = [float(i) for i in number.split(',')]
			if a > 0 and b > 0:
				return a,b
			else:
				clear_screen()
				print('Sólo números decimales positivos. Intentalo de nuevo.')
		except:
			clear_screen()
			print('Entrada invalida.Intentalo de nuevo.')


def valid_string():

	while True:
		user_enter = input('Ingresa ó enter para Salir>>') or exit()

		word_spaces = ''.join(user_enter.split())# Eliminamos los espacios en blanco para usar isalpha ()
		if  word_spaces.isalpha():
			clear_screen()
			return user_enter
		else:
			clear_screen()
			print('Sólo letras. Intentalo de nuevo.')
