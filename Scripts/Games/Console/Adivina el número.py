#Copyright © 2008-2015 por Albert Sweigart


#Importamos el el modulo random mediante la orden import
import random

intentosRealizados = 0 # Creamos la variable global intentosRealizados, que almacenara los intentos del jugador.


#Capturamos el nombre del jugador en la variable miNombre por medio de la función input
print("¡Hola! ¿Cómo te llamas?") 
miNombre = input()

#Creamos y almacenamos en la variable número, por medio de la funcón randint, perteneciente al modulo random, un número
#aleatorio del 1 al 20, incluyendo los extremos. 
número = random.randint(1,20)

#Por medio de la función print, concatenamos el nombre del jugador con el saludo del pc.
print('Bueno, ' + miNombre + ', esto pensando en un número entre 1 y 20.' )


#Mediante el bucle while, analizamos el número ingresado por el jugador y lo comparamos mediante seis intentos
#usando la condicionales if.
while intentosRealizados < 6:
	print('Intenta adivinar.')
	estimación = input() #Almacenamos el intento del jugador
	estimación = int(estimación) #Convertimos en número entero la estimación del jugador, para poder compararla

	#en cada intento realizado, aumentamos en 1, la variable intentos realizados 
	intentosRealizados = intentosRealizados + 1 

	
	if estimación < número:
		print ('Tu estimación es muy baja.')

		#Por cada intento realizado en la comparacion , se resta
		# 6 a los intentos que se llevan  y se realiza una doble conversión de la variable.
		print('Te quedan ' + str(int(6-intentosRealizados))  + 'intentos')

	elif estimación > número:

		print ('Tu estimación es muy alta')
		#Por cada intento realizado en la comparacion , se resta
		# 6 a los intentos que se llevan y se realiza na doble conversión de la variable

		print('Te quedan ' + str(int(6-intentosRealizados)) + 'intentos') 

	elif estimación == número:

		#Se realiza la conversión de tipo entero de la variable número a cadena de texto
		#Para poder concatenar con texto los intentos realizados.

		número = str(número)
		intentosRealizados = str(intentosRealizados)
		print('¡Buen trabajo, ' + miNombre + ' !Has adivinado mi número en  ' + intentosRealizados + ' intentos')
		print('En número era ' + número)
		break #rompemos el bucle while, si el jugador adivina el número

		#Para terminar si el jugador pierde revelamos el número del pc
	else:
		número = int(número)
		if estimación != número:
			número = str(número)
			print('Pues no. El número que estaba pensando era ' + número)

