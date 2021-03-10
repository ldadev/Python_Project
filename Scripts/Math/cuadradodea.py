"""-3.Realice un algoritmo
que lea un numero, calcule su cuadrado
y muestre el resultado por pantalla"""


a=0
def cua(a):
	a=input ("ingrese el numero>>")
	c=a**2
	float(c)
	print "El cuadrado del numero %.2f es:%.2f"%(a,c)
	e=0
	def control(e):
		e=raw_input("Ingrese la letra S para salir o C para continuar>>")
		for re in e:
			if re=="C":
				return cua(a)
			elif re=="S":
				print "Adios"
			else:
				return  control(e)
	control(e)


cua(a)