
"""
class Calculadora:
	def ingreso(self):
		self.n=int(input('Ingrese un numero entero:'))

class op(Calculadora):
	def factorial(self):
		print()
		print("----------------FACTORIAL DE UN NUMERO CUALQUIERA de la nueva rama-----------------------")
		factorial=1
		for i in range(1,self.n+1):
			factorial=factorial*i
		print('El factorial de {} es {}'.format(self.n,factorial))
"""


#Por recursividad

def factorial(x):
	if x == 1:
		return x
	else:
		return x*factorial(x-1)


#For loop
def factorial_2(x):

	if x == 1:
		factorial = 1
		for i in range(x,x + 1):
			factorial*=i
		print(factorial)


#Libreria reduce
from functools import reduce
factorial = reduce(lambda x,y:x*y,range(1,5))
print(factorial(5))

#Con lambda
factorial = lambda x:x*factorial(x - 1) if x > 0 else 1
print(factorial(5)) 