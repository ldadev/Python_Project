from random import randrange


class Dado:

	def __init__(self):
		self.valor = None  #self: este objeto...


	def lanzar(self):
		self.valor = randrange(1,7)


	# __repr__ reviza el valor del objeto y lo imprime
	def __repr__(self):
		return f'Dado: {self.valor}'

	#__str__ representación de un obj en string cuando se manda a imprimir

	def __str__(self):
		cara_dado = {1:"\n *\n",2:" *\n\n*",3:" *\n *\n *",4:"* *\n\n* *",5:"* *\n* *",6:"***\n\n***"}
		return cara_dado[self.valor]


#print(dado1)# Cuando se invoca print se llama al metodo __str__

num_lanz = int(input('Ingrese el número de lanzamientos: '))

dist = [0]*6

for _ in range(num_lanz):
	dado = Dado()
	dado.lanzar()
	dist[dado.valor - 1] = dist[dado.valor - 1] + 1


dist_prob = [val/num_lanz for val in dist]
print(dist_prob)






