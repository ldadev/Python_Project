from utility import *

"""11.	Disene un algoritmo
para convertir metros a pies y pulgadas,
teniendo en cuenta que:
1 metro=39.37 pulgadas y 1 pie=12 pulgadas """

def show_mts_converter():
	
	clear_screen()
	flag = True
	while flag:
		print("ingrese el numero de metros a convertir ó enter para Salir")
		num_mts = valid_float()
		num_inch = num_mts*39.37
		num_ft = num_inch/12.0
		print(f'{num_mts} metros equivalen a {num_inch:,.2f} pulgadas y {num_ft:,.2f} pies')

show_mts_converter()















