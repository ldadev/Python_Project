start = True# bandera para iniciar el bucle
while start:

	entrada = input('Ingrese dos números, asi a,b o s/salir>>').lower()
	if entrada == 's':
		print('¡Hasta luego!')
		start = False# Termina el bucle
	else:
		try:
			a,b = entrada.split(',')
			a,b = int(a),int(b)
			if 0<a<=10 and 0<b<=10:
				cuadrado = lambda a,b: (a**2,b**2)# Guardamos en un tupla el resultado
				cubo = lambda a,b:(a**3,b**3)# Guardamos en un tupla el resultado
				print(f'Números     Cuadrados     Cubos')
				print(f'{(a,b)}   {cuadrado(a,b)}   {cubo(a,b)}')
			else:
				print('Solo 0<números<=10')

		except:# Si la entrada es invalida
			print('Entrada invalida.Intalo de nuevo')
