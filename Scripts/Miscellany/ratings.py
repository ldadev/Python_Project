import os

os.system('clear')# Borro la consola al iniciar
calificaciones_mat = []
entrada = int(input('¡Hola! ¿Cuantas materias quieres ingresar?>>'))

def entrada_calificaciones():

	for i in range(1,entrada + 1):
		print(f'Ingrese la materia {i}>>')
		materia = input('>>')
		calific = input('Ingrese la calificación del primer y segundo parcial. Así (5,2)>>')
		a,b = [float(x) for x in calific.split(',')]# Convierto a float las calificaciones
		prom = (a + b)/2
		calificaciones_mat.append([materia,str(a),str(b),str(prom)]) # Guardo los valores a la lista calificacones_mat		
		os.system('clear')# Despues de cada iteracción, borra la pantalla
entrada_calificaciones()

#Funcion que da formato a las celdas
def celdas(s):
	print('+' + '-'*55 + '+')
	print(s)
	print('+' + '-'*55 + '+')


# Imprimo la cabecera y las calificaciones

celdas('|{:^14}{:^5}{:^1}{:^5}|'	
	.format('Materia ','Primer parcial  ',
	'Segundo parcial  ','Promedio'))

for i in calificaciones_mat:
	celdas('{:^14}{:^20}{:^10}{:^15}'.format(*i))# *i descomprimo las sublistas

