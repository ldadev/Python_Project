#Calculadora de números de cualquier tamaño de números

a = input('Ingresa números enteros a sumar de cualquier tamaño y signo>>')
l = a #copia del input para imprimir los signos, si el primer número de a es positivo
k = []#lista de signos
p = 0 # suma de los números positivos y negativos

"""
Si el usuario ingresa una lista de números
y el primer número es positivo se ejecuta la 
linea del 13 al 24.

Si el usuario ingresa una lista de números
y el primer número es negativo se ejecuta la 
linea del 32 al 44.
"""
if a[0] != '-':
	for i in range(1,len(a)): 
		if  not a[i].isdigit():
			a = a.replace(a[i],',') #sustitución de los signos por una coma
			k.append(i)#adición de cada indice de los signos en la variable k
	c = a.split(',')#agrupación de cada número en la lista c
	r = 0
	for t in k:
		r+=1
		p+=int(l[t] + c[r])
	e = p + int(c[0]) #suma de los números mas el primer número sin signo
	print(e)

else:
	for i in a:
		if  not i.isdigit():
			a = a.replace(i,',')
			k.append(i)
	c = a.split(',')#agrupación de cada número en la lista c
	r = 0
	j = -1
	for t in k:
		r+=1 #contador para indexar los numeros
		j+=1#contador para indexar los signos
		p+=int(k[j]+c[r])
	print(p)

