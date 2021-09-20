import random


arreglo = [5,40,11,34,10,23,50]
arreglo_ordenado= ['']*len(arreglo)


indice_par = 0
indice_inpar = 1
for numero in arreglo:
	if numero % 2 == 0:
		indice_par+=2
		arreglo_ordenado.insert(indice_par,numero)
	else:
		indice_inpar+=2
		arreglo_ordenado.insert(indice_inpar,numero)


# (1,1),(1,2),(1,3),(1,4),(1,5),(1,6)

import itertools

x = [2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]
z = [0,1,2,3,4,5,6,7,8,9]

for a,b,c in itertools.zip_longest(y,z,x):
	print(a,b,c)


def success(n):
	s = ['c','s']
	sucesos = ['']*len(s)**n

	for  a in range(len(s)**n):
		for b in range(1,n + 1):
			sucesos[a] = str(sucesos[a]) + str(random.choice(s))
	print(sucesos)

