from functools import reduce

def calc_mix(numeros,operador):

	try:
		operaciones = {
				'+':reduce(lambda acumulador=0, elemento=0: acumulador + elemento, numeros),
				'-':reduce(lambda acumulador=0, elemento=0: acumulador - elemento, numeros),
				'*':reduce(lambda acumulador=0, elemento=0: acumulador * elemento, numeros),
				'/':reduce(lambda acumulador=0, elemento=0: acumulador / elemento, numeros)
				}
		print(f'Resultado: {operaciones[operador]:,.2f}')
	
	except(KeyError):print('Operador aritmetico invalido. Intentalo de nuevo.')
	except(ZeroDivisionError):print('No se puede dividir por 0. Intentalo de nuevo.')


calc_mix([3,4,5,9],'/')
