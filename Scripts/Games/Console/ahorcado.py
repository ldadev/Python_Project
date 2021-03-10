
import os
import sys
import random


def controlsalida():
	dato = input("Si quieres continuar, presiona c, sino, presiona cualquier tecla para salir>>")
	os.system("clear");	juego() if dato == "c" else print("¡Hasta luego!");sys.exit() if dato == "x" else print("Opción invalida")

def juego():

	a,listadepalabras,letrascorrectas, letrasincorrectas,letrasrepetidas,palabrafinal = 5,["amongus"],[],[],[],""
	palabrasecreta = random.choice(listadepalabras) 
	print("Palabra: {}".format("_"*len(palabrasecreta)));print("Espacios:{}".format(len(palabrasecreta)))

	while 0 < a:
	
		todasletras = letrascorrectas + letrasincorrectas
		espaciosvacios = "_"*len(palabrasecreta)
		a = 5 - len(letrasincorrectas) 
		rondas = len(todasletras) + 1
		
		print("RONDA: {}".format(rondas),"\t");print("¡Adivina la letra!" + "\t")
		usuario = input("Ingresa una letra>>")
		x = lambda usuario : print("ya elegiste la letra {}. Intentalo de nuevo".format(usuario))

				
		if usuario in todasletras:
			os.system("clear")
			print(x(usuario));print("Palabras Repetidas: " + ",".join(letrasrepetidas));print("Letras adivinadas: {}".format(palabrafinal))
			
			if not usuario in letrasrepetidas:
				os.system("clear");print("ya elegiste la letra {}. Intentalo de nuevo".format(usuario))
				letrasrepetidas.append(usuario);print("Palabras Repetidas: " + ",".join(letrasrepetidas))
				print("Letras adivinadas: {}".format(palabrafinal));print("Espacios faltates:{}".format(len(palabrasecreta)- len(letrascorrectas)))
							
		else:

			if usuario in palabrasecreta:
				letrascorrectas.append(usuario)

				for i in range(len(palabrasecreta)):
					if palabrasecreta[i] in letrascorrectas:
						espaciosvacios = espaciosvacios[:i]+ palabrasecreta[i] + espaciosvacios[i+1:]
						os.system("clear")
						print("RONDA ANTERIOR: {}".format(rondas),"\t");print("Letras adivinadas: {}".format(espaciosvacios))
						print("Espacios faltates:{}".format(len(palabrasecreta)- len(letrascorrectas)));palabrafinal = "".join(espaciosvacios)

			else:
				os.system("clear");print("No es la palabra correcta, te quedan {} intentos".format(a))
				letrasincorrectas.append(usuario);print("Letras adivinadas: {}".format(palabrafinal))
				print("Espacios faltates:{}".format(len(palabrasecreta)- len(letrascorrectas)));print("Palabras Incorrectas: " + ",".join(letrasincorrectas))
				
			if espaciosvacios == palabrasecreta:
				print("Ganaste, la palabra secreta es {}".format(palabrasecreta));controlsalida()

			if a == 0:
				os.system("clear");print("Perdiste, la palabra secreta es {}".format(palabrasecreta));controlsalida()
juego()




