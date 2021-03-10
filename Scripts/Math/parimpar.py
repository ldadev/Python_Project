"""6.Desarrolle un algoritmo
que permita leer un valor cualquiera N y escriba si dicho
numero es par o impar."""

N=0
def parimpar(N):
	N=input ("ingrese  el numero a evaluar>> ")
	if N==0 :
		print "El numero ingresado debe ser diferentes de cero"
		e=raw_input("Ingrese la letra s para salir o c para continuar>>")
		if e=="c":
			return parimpar(N)
		elif e=="s":
			print "adios"
	else:
		if N%2==0:
			print "El numero %d es par"%(N)
		else:
			print "El numero %d es impar"%(N)
			e=0
			def control(e):
				e=raw_input("Ingrese la letra S para salir o C para continuar>>")
				for re in e:
					if re=="C":
						return parimpar(N)
					elif re=="S":
						print "adios"
					else:
						return  control(e)
			control(e)
parimpar(N)

