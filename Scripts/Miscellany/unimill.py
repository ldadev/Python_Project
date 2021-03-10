def entrada():

	start = True

	while start:

		numero = input('Ingresa un numero entero>>')

		if len(numero) == 7:
			return numero
		else:
			print('Entrada invalida')


def mostrar_partes():

	numero = entrada()
	divisiones = {'u_millon':numero[-7],'u_millar':numero[-4],
	              'centenas':numero[-3],'decenas':numero[-2],
	              'unidades':numero[-1]
	              }

	for clave,valor in divisiones.items():
		print(f'Número de {clave}:{valor}')

	return numero


def convertir_romano():

	num = int(mostrar_partes())
	num_map = [(1000000,'M'),(500000,'D'),(100000,'C'),(50000,'L'),
	(10000,'X'),(5000,'V'),(1000, 'M'), (900, 'CM'), (500, 'D'),
	(400, 'CD'), (100, 'C'), (90, 'XC'),(50, 'L'), (40, 'XL'), 
	(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
	roman = ''
	while num > 0:
		for i, r in num_map:
			while num >= i:
				roman += r
				num -= i
	return roman

print(convertir_romano())