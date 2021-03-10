
#Código Python: Genera un calendario de acuerdo al año anterior
#Desarrollando por David Martinez

from tabulate import tabulate# pip install tabulate
import os

def mostrar_entrada():

	os.system('clear')# Limpiar pantalla en cada ejecución
	while True:

		# Menu con los indices de los dias de la semana
		print('-'*2,'MENU','-'*2,'\n')
		DIAS = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
		for a,b in enumerate(DIAS,1):print(f'{a}:{b}')
		
		# Solicito al usuario un número, si hay un error vuelvo al bucle.
		try:
			entrada = input('Ingresa el año nuevo e indice del dia final del año pasado (2021,5)>>')
			año,dia = [int(x) for x in entrada.split(',')]
			
			if dia > 0 and dia <= 7  and año > 0:
				return dia + 1,año
			else:
				print(f'La entrada {año},{dia} no es valida, intentalo de nuevo')
		except:
			print(f'La entrada no es valida, intentalo de nuevo')


def mes_n(mes_n,dia_n):

	
	semana_1 = [None for y in range(int(dia_n) - 1)]# None por indice de inicio
	c = dia_n - 1
	for i in range(dia_n,8):
		c+=1
		semana_1.insert(c,(i + 1) - dia_n)# i+1 porque la semana_1 inicia en 1

	# Resto 9 para omitir los espacios vacios en la semana_1	
	mes = list(range(9 - dia_n,mes_n + 1))
	semanas = [semana_1]
	porciones = 0

	for i in range(1,6):
		porciones+=7
		semanas.insert(i,mes[porciones - 7:porciones])# Agrego las semanas a la lista

	# Si existe una semana vacia al final, se elimina.
	if semanas[-1] == []:semanas.pop();return semanas;
	else:
		return semanas

def mostrar_calendario():


	dia,año = mostrar_entrada()# El día final del año pasado,año nuevo 
	DIAS = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
	ENERO=MARZO=MAYO=JULIO=AGOSTO=OCTUBRE=DICIEMBRE = 31
	ABRIL=JUNIO=SEPTIEMBRE=NOVIEMBRE = 30

	
	if año % 2 == 0 and año % 4==0:FEBRERO = 29;# Años bisiestos y no bisiestos
	else:FEBRERO=28

	MESES = {'ENERO':ENERO,'FEBRERO':FEBRERO,'MARZO':MARZO,
	        'ABRIL':ABRIL,'MAYO':MAYO,'JUNIO':JUNIO,
	        'JULIO':JULIO,'AGOSTO':AGOSTO,'SEPTIEMBRE':SEPTIEMBRE,
	        'OCTUBRE':OCTUBRE,'NOVIEMBRE':NOVIEMBRE,'DICIEMBRE':DICIEMBRE
	        }

	primeros_dias = [dia]# Guardo los primeros dias de cada mes.	

	for a,b,c in zip(MESES.keys(),MESES.values(),primeros_dias):
		semanas_n = mes_n(b,c) 
		dia_p = len(semanas_n[-1]) + 1# semanas_n[-1]+1 Obtengo el primer día del mes sgt.
		primeros_dias.append(dia_p)
		print('\n','-'*30,'{:^5} DE {:^5}'.format(a,año),'-'*32)# {:^5} ancho de columna
		print(tabulate(semanas_n,headers = DIAS,tablefmt = 'fancy_grid',numalign = 'center'))	

mostrar_calendario()







