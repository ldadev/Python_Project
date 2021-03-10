"""5.	Realice un algoritmo que determine cuantos segundos
hay en N horas."""

n=0
def conh(n):
	n=input ("ingrese el numero de horas a convertir>>")
	if n<0:
		print "Las horas deben ser mayores a cero"
		return conh(n)
	else:
		con=n*3600
		print "En %d horas hay %d segundos"%(n,con)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return conh(n)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)
	
conh(n)



