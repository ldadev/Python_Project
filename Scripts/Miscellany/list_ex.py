
# Suma los valores que le pertenecen a los nombres repetidos

nombres =['Andres','Julio','Andres','Julio']
numeros =[19,20,15,17]

personas = {}

for nombre,numero in zip(nombres,numeros):
	personas[nombre] = personas.get(nombre,0) + numero

print(personas)
