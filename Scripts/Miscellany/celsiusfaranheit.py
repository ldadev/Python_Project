from utility import *
"""8. Diseñe un algoritmo que convierta el valor de una temperatura
dada en grados Celsius a grados Fahrenheit."""

def mostrar_convertidor():

	flag = True
	while flag:
		
		clear_screen()
		print('CONVERTIDOR DE GRADOS CELSIUS A FAHRENHEIT\n')
		print('INSTRUCCIONES\n-Ingrese el numero de grados celsius\nr:Reiniciar ó enter:Salir\n')
		num_celcius=float_valid()
		num_fhre=num_celcius*1.8
		print(f'Los grados {num_celcius:,.2f} celsius equivalen a {num_fhre:,.2f} grados Fahrenheit')
		flag = False

mostrar_convertidor()


