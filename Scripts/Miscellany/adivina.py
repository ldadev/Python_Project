from utility import *
import random
import os


flag = True
while flag:

	clear_screen()
	print('¿PUEDES ADIVINAR EL NÚMERO?\n')
	print('INSTRUCCIONES\n*Intenta un número del 1 al 10\n*r:reiniciar ó enter para salir')

	numero = random.randrange(1,10)
	intentos = 6

	while intentos > 0:
		intentos -= 1

		entrada = int_valid()
		if entrada == True:break

		if entrada == numero:
			print(f'¡Ganaste! El número es el {numero}\n')
			break
			flag = False
		elif entrada > numero:
			print(f'intenta un número menor. Te quedan {intentos} turnos\n')
		else:
			print(f'intenta un número mayor.Te quedan {intentos} turnos\n')

	if intentos < 2:flag = exit_choices()


	
	