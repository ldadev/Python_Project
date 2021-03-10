import re


"""
def captura_numeros():

	start = True
	while start:
		try:
			usuario = input("Ingresa la operacion de dos números>>")
			a,b = re.findall('\d+',usuario)# captura dos numeros de cuaquier cifra
			simbolos = re.findall('\D',usuario) # captura los simbolos

			if len(simbolos) < 2:
				return int(a),int(b),simbolos[0]
			else:
				return int(''.join([simbolos[0],a])),int(b),simbolos[1]
		except:
			print('Entrada invalida')

def operacion():

	a,b,operador = captura_numeros()
	try:
		operaciones = {'+':a+b,'-':a-b,'*':a*b,'/':a/b}
		print(f'El resultado de la operacion {operador}, es {operaciones[operador]}')
	except(ZeroDivisionError):
		print('No se puede dividir por 0')
operacion()
"""

a = '-3/8797'

#entrada = input('Ingresa la suma>>')

result = re.findall('\W\d+',a)

print(result)

