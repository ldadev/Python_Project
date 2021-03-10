class Calculadora:
	def ingreso(self):
		self.n=int(input('Ingrese un numero entero:'))

class op(Calculadora):
	def multiplos(self):
		print()
		print("-------------------------------------TABLA DE MULTIPLOS-----------------------------------------")
		for c in range(1,self.n+1):
			print()
			for i in range(1,self.n+1):
				tablas=c*i
				print('\t   ',tablas,end="")


numero = op()
print(numero.ingreso())
print(numero.multiplos())
