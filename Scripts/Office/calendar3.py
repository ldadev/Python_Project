#Código de Luis muñoz


def dia_mes(dia,mes,anio):
	#Retorna el día de un mes
	if mes in [1,2]:
		mes += 12
		anio -= 1

	q,m,Y = dia, mes, anio
	h = q + ((13 * (m + 1)) // 5) + Y + (Y //4) - (Y// 100) + (Y// 400) % 7

	return (h - 1) % 7


def num_dias_mes(mes,anio):
	 # Retorna el número de días de una fecha (mes/año)
	 if mes == 2:
	 	# Si el mes le corresponde a una año bisiesto, seran 29 días

	 	if anio % 4 == 0 and (anio % 100 != 0 or anio % anio % 400 == 0):
	 		return 29
	 	else:
	 		return 28

	 elif mes in [4,6,8,10]:
	 	return 30
	 else:
	 	return 31

def print_calendario(mes,calendario):
	#Imprime una lista de días (42) en el formato calendario mensual
	nombre_mes = {1:'ENERO',2:'FEBRERO',3:'MARZO',4:'ABRIL',
	              5:'MAYO',6:'JUNIO',7:'JULIO',8:'AGOSTO',
	              9:'SEPTIEMBRE',10:'OCTUBRE',11:'NOVIEMBRE',
	              12:'DICIEMBRE'}

	print(nombre_mes[mes])
	print("D  L  M  MI  J  V  S")
	for idx, dia in enumerate(calendario,start=1):
		print(f'{dia:2}',end=' ')
		if idx % 7 == 0:
			print()

def print_calendario_anual(anio,calendario_anual):
	nombre_mes = {0:'ENERO',1:'FEBRERO',2:'MARZO',3:'ABRIL',
	              4:'MAYO',5:'JUNIO',6:'JULIO',7:'AGOSTO',
	              8:'SEPTIEMBRE',9:'OCTUBRE',10:'NOVIEMBRE',
	              11:'DICIEMBRE'}

	print(f'{anio:^80}')
	print()

	for mes in range(0,12,3):
		print(f'{nombre_mes[mes]:30}',end='')
		print(f'{nombre_mes[mes + 1]:30}',end='')
		print(f'{nombre_mes[mes + 2]:30}')

		print(f"{' D  L  M  MI  J  V  S':30}",end='')
		print(f"{' D  L  M  MI  J  V  S':30}",end='')
		print(f"{' D  L  M  MI  J  V  S':30}")

		for i in range(0,42,7):
			print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}           ".format(
				*calendario_anual[mes][i:i+7]),end='')

			print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}           ".format(
				*calendario_anual[mes][i:i+7]),end='')

			print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}           ".format(
				*calendario_anual[mes][i:i+7]))

			print()


mes_valido = False
while not mes_valido:
	try:
		mes = int(input("Ingrese el mes [1-12]: "))
		if mes >= 1 and mes <= 12:
			mes_valido = True
		else:
			print('Error: el mes ingresado debe estar en el rango especificado')
	except ValueError:
		print("Error: El mes ingresado debe ser un enterio entre 1-12")

anio_valido = False
while not anio_valido:
	try:
		anio = int(input("Ingrese año [>=1900}: "))
		if anio >= 1900:
			anio_valido = True
		else:
			print('Error: el año ingresado debe estar en el rango especificado')
	except ValueError:
		print("Error: El año ingresado debe ser mayor o igual a 1900")


if anio_valido:
	calendario_anual = []
	for mes in range(1,13):
		calendario = [''] * 42
		idx = dia_mes(1,mes,anio)
		n_dias = num_dias_mes(mes,anio)
		calendario[idx:idx+n_dias] = range(1,n_dias+1)
		calendario_anual.append(calendario)
	print_calendario_anual(anio,calendario_anual)