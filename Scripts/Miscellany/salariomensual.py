"""7.Calculo del salario mensual
de un empleado,
sabiendo que este se calcula
con base a las horas
trabajadas y
de acuerdo a un precio
especificado por hora."""

ht=0
pxh=5000
def hora(ht):
	print "Estimado usuario, el precio de la hora trabajada esta en 5000 pesos"
	ht=input ("ingrese el numero de horas trabajadas>> ")
	slrio=ht*5000
	print "Su salario de acuerdo a las %d horas trabajadas es de:%d pesos"%(ht,slrio)
	e=0
	def control(e):
		e=raw_input("Ingrese la letra S para salir o C para continuar>>")
		for re in e:
			if re=="C":
				return hora(ht)
			elif re=="S":
				print "Adios"
			else:
				return  control(e)
	control(e)

hora(ht)


