"""9.Desarrolle un algoritmo que permita leer dos numeros y
ordenarlos de menor a mayor, si es el caso."""



a=0
b=0
def ayb(a,b):
	a=input ("ingrese  el primer numero a evaluar>> ")
	b=input ("ingrese  el segundo numero a evaluar>> ")
	float(a)
	float(b)
	if a>b :
		print "El orden de menor a mayor es %.2f,%.2f"%(b,a)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return ayb(a,b)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)
		
	else:
		print "El orden de menor a mayor es %.2f,%.2f"%(a,b)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return ayb(a,b)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)
		

ayb(a,b)
