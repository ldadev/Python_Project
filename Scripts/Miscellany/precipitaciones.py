from utility import *



def mostrar_precipitaciones():

	list_precipitaciones = []
	FLAG = True# Bandera para controlar el bucle
	while FLAG:

		print('¿Cuantas precipitaciones ingresara?\n')
		num_precipitaciones = valid_int()
		c = 0
		while num_precipitaciones > 0:

			num_precipitaciones-=1
			c+=1
			print(f'Ingrese la precipitacion(mm) {c} ó enter:Salir\n')
			precipitaciones = valid_float()
			list_precipitaciones.append(precipitaciones)		

			if num_precipitaciones <1 and len(list_precipitaciones) > 0:
				print('{0}\nMayor:{1}\nMenor:{2}\nTotal:{3}'.
				format('PRECIPITACIONES',max(list_precipitaciones),
				min(list_precipitaciones),sum(list_precipitaciones)))
				break
		flag = False
		
mostrar_precipitaciones()




