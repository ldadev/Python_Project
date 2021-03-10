#Calculadora de números de un digito
a = input('Ingresa números enteros a sumar de un solo digito con su signo>>')

p = 0 # suma de numeros negativos
u = 0 #suma de numeros positivos
d =-1

"""
Si el usuario ingresa una lista de números
y el primer número es positivo se ejecuta la 
linea del 14 al 23

Si el usuario ingresa una lista de números
y el primer número es negativo se ejecuta la 
linea del 29 al 39
"""

if a[0] != '-':
	for i in range(1,len(a)): 
		if a[i].isdigit():
			b = a[i-1]
			k = int(a[i])
			
			if b == '-':
				p+=k
			elif b:
				u+=k + int(a[0])
else:
	for i in a:
		d+=1
		if i.isdigit():
			b = a[d-1] #idexación de signos desde el 0
			k = int(a[d]) #indexación de numeros desde el 1
			
			if b == '-':
				p+=k
			elif b:
				u+=k

r = u - p #resultado final mediante el concepto de valor absoluto
if u > p:
	print(r)
else:
	print(r)


