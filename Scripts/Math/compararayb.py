"""
2)Solicitar al usuario que digite dos numeros (A y B)
compararlos, si A>B restarlos, de lo contrario, multiplicarlos.
"""

a=0
b=0
def numab(a,b):
	a=input ("ingrese el primer numero>>")
	b=input ("ingrese el segundo numero>>")
	r= a-b
	m= a*b
	float(r)
	float(m)
	if a>b:
		print "el primer numero,%.2f,es mayor que el segundo numero,%.2f, por lo tanto se efectua una resta cuyo resultado es:%.2f"%(a,b,r)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return numab(a,b)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)

	else:
		print "el segundo numero,%.2f, es mayor que el primer numero,%.2f, por lo tanto se efectua una multiplicacion cuyo resultado es:%.2f"%(b,a,m)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return numab(a,b)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)
numab(a,b)