
def entrada():

	numero = 0
	try:
		while numero not in range(1,6):
			numero = int(input('Inserta un número del 1 al 5>>'))
		return numero
	except (TypeError,ValueError) as e:
		print("Entrada invalida ",e)
		entrada()# Si se produce una excepción, se vuelve a llamar a la función

def vocales():
	numero = entrada()# Retorna la opción ingresada por el usuario en la función entrada
	vocales = {1:'a',2:'e',3:'i',4:'o',5:'u'}
	if numero in vocales.keys():
		print(f'El número {numero} corresponde a la vocal {vocales[numero]}')
vocales()