class Calculadora:
	def ingreso(self):
		self.n=int(input('Ingrese un numero entero:'))

class op(Calculadora):
	def fibo(self):
		print()
		print("----------------SECUENCIA FIBONACCI-----------------------")
		a,b=0,1
		fibo=[a,b]
		while b<self.n+1:
			a,b=b,a+b
			print(a,b)
			fibo.append(b)
		print('La secuencia fibonacci de {} es {}'.format(self.n,fibo))

numero = op()
print(numero.ingreso())
print(numero.fibo())
