"""4.Ingrese dos numeros por teclado
y realice con ellos las cuatro operaciones aritmeticas,
muestre por pantalla el resultado de cada uno indicando
a que operacion corresponde."""
a=0
b=0
def srmd(a,b):
	a=input ("ingrese el primer numero>> ")
	b=input ("ingrese el segundo numero>> ")
	float(a)
	float(b)
	if b==0:
		suma= a+b
		resta= a-b
		multi= a*b
		print "La suma de %.2f y %.2f es:%.2f"%(a,b,suma)
		print "La resta de %.2f y %.2f es:%.2f"%(a,b,resta)
		print "La multiplicacion de %.2f y %.2f es:%.2f"%(a,b,multi)
		print "La division entre %.2f y %.2f no se puede realizar,porque el divisor debe ser diferente de 0"%(a,b)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return srmd(a,b)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)
	else:
		suma= a+b
		resta= a-b
		multi= a*b
		div= a/b
		print "La suma de %.2f y %.2f es:%.2f"%(a,b,suma)
		print "La resta de %.2f y %.2f es:%.2f"%(a,b,resta)
		print "La multiplicacion de %.2f y %.2f es:%.2f"%(a,b,multi)
		print "La division de %.2f y %.2f es:%.2f"%(a,b,div)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return srmd(a,b)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)

		
srmd(a,b)