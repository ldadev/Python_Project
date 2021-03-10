"""1)calcular la suma de dos numeros
ingresados por el teclado
"""
a=0
b=0
def s(a,b)://
	a=input("Ingrese el primer numero>> ")
	b=input("Ingrese el segundo numero>> ")
	suma=a+b
	float(suma)
	print "la suma de %.2f y %.2f es:%.2f"%(a,b,suma)
	e=0
	def control(e):
		e=raw_input("Ingrese la letra S para salir o C para continuar>>")
		for re in e:
			if re=="C":
				return s(a,b)
			elif re=="S":
				print "Adios"
			else:
				return  control(e)
	control(e)

s(a,b)






