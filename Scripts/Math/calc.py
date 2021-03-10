
def entrada():

	while True:
		entrada = input('Ingresa dos números y el operador(+,-,*,/) separados por coma ó enter para salir>>') or exit()

		try:
			a,b,o = [i for i in entrada.split(',')]
			return float(a),float(b),o
		except:
			print('Entrada invalida. Intentalo de nuevo.')

def mostrar_calculadora():

	while True:
		a,b,o = entrada()
		try:
			operaciones = {
				'+':a + b,
				'-':a - b,
				'*':a * b,
				'/':a/b
				}
			print(f'Resultado: {operaciones[o]:,.2f}')		

		except(KeyError):print('Operador aritmetico invalido. Intentalo de nuevo.')
		except(ZeroDivisionError):print('No se puede dividir por 0. Intentalo de nuevo.')

mostrar_calculadora()



