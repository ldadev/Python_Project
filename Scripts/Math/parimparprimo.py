def ParImparPrimo():
	    '''Pide al usuario que ingrese un número entero y determina en su rango
	    los números pares,impares y primos
        '''

	numeros= int(input('Ingrese el número>>:'))
	list_par = []
	list_impar = [] 
	list_primo = []
	a = 1
	b = 1
	dict_div = {a:b}  #Diccionario que contiene los divisores de cada número del rango  

	for c in range(numeros + 1):
		divisores = [d for d in range(1,c+1) if c%d == 0]
		dict_div[c] = divisores
		if len(divisores) == 2:
			list_primo.append(c)

	#Iteramos a través de las claves del diccionario
	for e in dict_div.keys():
		if e%2 == 0:
			list_par.append(e)
		else:
			list_impar.append(e)

	print('Pares:{0}\nImpares:{1}\nPrimos:{2}'.format(list_par,list_impar,list_primo))	






