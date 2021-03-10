#Código Python: Genera un calendario de acuerdo al año anterior
#Desarrollando por David Martinez

from tabulate import tabulate# pip install tabulate
import os
import math


def mostrar_entrada():

	os.system('clear')# Limpiar pantalla en cada ejecución
	
	while True:

		# Menu con los indices de los meses
		print('-'*2,'MENU','-'*2)
		MESES = ['ENERO','FEBRERO','MARZO','ABRIL',
		'MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE',
		'OCTUBRE','NOVIEMBRE','DICIEMBRE']
		for a,b in enumerate(MESES,1):print(f'{a}:{b}')

		
		# Solicito al usuario un número, si hay un error vuelvo al bucle.
		try:
			entrada = input('Ingresa el año e indice del mes>>')
			año,mes = [int(x) for x in entrada.split(',')]

			if año > 0 and 0<mes <= 12:
				return año,MESES[mes-1]
			else:
				os.system('clear')
				print(f'La entrada {año},{mes} no es valida, intentalo de nuevo')
		except:
			os.system('clear')
			print(f'La entrada no es valida, intentalo de nuevo')

#Algoritmo de Zeller que ayuda a determinar el  primer dia del mes de enero de un año
def dia_n(Y):


    D = 31# Cantidad de días de diciembre
    M = 12 # Indice del mes de diciembre
    Y = Y - 1 # EL año ingresado menos 1
    
    #math.floor Redondea numeros a enteros
    dia_y = (D + math.floor((13 
    	* (M + 1)) / 5) 
    	+ Y + math.floor(Y / 4) 
    	- math.floor(Y / 100) 
    	+ math.floor(Y / 400)) % 7

    return dia_y + 1


def mes_n(mes_n,dia_k):

	RANGO_DIA = dia_k - 1
	semana_1 = [None for y in range(RANGO_DIA)]# None por indice de inicio
	c = RANGO_DIA - 1 
	for i in range(dia_k,8):
		c+=1
		semana_1.insert(c,(i + 1) - dia_k)# i+1 porque la semana_1 inicia en 1

	# Resto 9 para omitir los espacios vacios en la semana_1	
	mes = list(range(9 - dia_k,mes_n + 1))
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


	año,mes = mostrar_entrada()# El día final del año pasado,año nuevo
	dia = dia_n(año) 
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

		
		# Imprimo un mes y año especifico
		if mes == a:
			print('-'*30,'{:^5} DE {:^5}'.format(a,año),'-'*32)# {:^5} ancho de columna
			print(tabulate(semanas_n,headers=DIAS,tablefmt='fancy_grid',
				           numalign = 'center',stralign = 'center'))
			

mostrar_calendario()





