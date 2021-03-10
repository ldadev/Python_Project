"""10.	Calcule el salario de un empleado,
teniendo en cuenta que debe conocer el numero de horas trabajadas
y el valor de la hora.Si el empleado laboro mas de 40 horas,
calcule el valor de la hora
adicional al doble de la ordinaria.
Imprima el resultado por pantalla."""



htr=0
vho=0
def sextr(htr,vho):
	htr= input("ingrese el numero de horas trabajadas>> ")
	vho= input("ingrese el valor de la hora trabajada>>") 
	sa_1= htr*vho
	sa_2= (40*vho)+((htr-40)*vho*2)
	if htr>40:
		print "Su salario de acuerdo a sus horas trabajadas es de %d pesos"%(sa_2)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return sextr(htr,vho)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)	
		
	else:
		print "Su salario deacuerdo a sus horas trabajadas es de %d pesos"%(sa_1)
		e=0
		def control(e):
			e=raw_input("Ingrese la letra S para salir o C para continuar>>")
			for re in e:
				if re=="C":
					return sextr(htr,vho)
				elif re=="S":
					print "Adios"
				else:
					return  control(e)
		control(e)	
sextr(htr,vho)
