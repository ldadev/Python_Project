

#Conjetura de collatz

"""
Todo numero positivo si se aplican estas reglas terrminaran en el ciclo 4,2,1
3x + 1
Numeros granizo, porque suben y bajan como granizo en una nube de tormenta
"""
import matplotlib.pyplot as plt
import numpy as np

numero = int(input('Ingresa un numero>>'))

"""
numeros = []
def collat(numero):

	numeros.append(numero)
	if numero > 1:
		if numero%2 != 0:
			numero = (numero*3) + 1
			collat(numero)
		else:
			numero = numero/2
			collat(numero)
			
collat(numero)
"""


numeros = []
pares = []
impares = []
def collat(numero):

	if numero > 1:
		if numero%2 != 0:
			numero = (numero*3) + 1
			impares.append(numero)
			collat(numero)
		else:
			numero = numero/2
			pares.append(numero)
			collat(numero)
			
collat(numero)


fig,ax = plt.subplots()
g1 = ax.plot(pares,label = "Pares")
g2 = ax.plot(impares,label = "Impares")
plt.xticks(g2)
ax.legend(["Pares","Impares"],loc = "lower right")
plt.show()


"""
y = np.array(numeros)

fig,ax = plt.subplots()
ax.set_aspect(0.5)
plt.plot(y,c = '#4CAF50')
plt.title('Números de la conjetura de collat')
plt.xlabel('Resultado')  
plt.ylabel('Números')


plt.show()
"""