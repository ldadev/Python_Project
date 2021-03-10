class Calculadora:
	def ingreso(self):
		self.n=int(input('Ingrese un numero entero:'))

class op(Calculadora):

	def sumatoria(self):
		print()
		print("----------------SUMATORIA DE UN NUMERO---------------------")
		suma=0
		for i in range(self.n+1):
			suma=suma+i
		print('La sumatoria de {} es {}'.format(self.n,suma))

numero = op()
print(numero.ingreso())
print(numero.sumatoria())
