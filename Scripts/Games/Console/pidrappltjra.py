from colorama import init, Fore , Back, Style
import os
import sys
import random

def controlsalida():
	dato = input("Si quieres continuar, presiona c, sino, presiona x para salir>>")
	if dato == "c":
		partida()
	elif dato == "x":
		print("¡Hasta luego!")
		sys.exit()

def partida():

	init()
	os.system("clear")

	manos = {0:"PIEDRA",1:"PAPEL",2:"TIJERA"}

	Empate = [[0,0],[1,1],[2,2]]
	GanaUser = [[0,1],[1,2],[2,0]]
	GanaPc =[[0,2],[1,0],[2,1]]

	print(Fore.GREEN+"¡Bienvenido! Juguemos Piedra, Papel y Tijera"+Back.RESET + "\n")

	turnos=int(input("¿Cuantas veces quieres jugar?>>"))
	print(" ")
	os.system("clear")

	PcResultado = []
	UserResultado = [] 
	ronda = 0
	while 0<turnos:
		turnos = turnos - 1
		ronda = ronda +1

		print(Fore.WHITE +"--------"+ Back.RESET)
		print(Fore.BLUE + "RONDA {0}".format(ronda) + Back.RESET)
		print(Fore.WHITE +"--------"+ Back.RESET)

		print(Fore.GREEN + "PC: {0}".format(len(PcResultado)))
		print(Fore.GREEN + "USUARIO: {0}".format(len(UserResultado)))	
		
		print(Fore.WHITE + "---------------------" + Back.RESET )
		print(Fore.GREEN + "TURNOS RESTANTES: {} ".format(turnos) + Back.RESET )
		print(Fore.WHITE + "---------------------" + Back.RESET + "\n")


		print(Fore.YELLOW + "¿PIEDRA, PAPEL O TIJERA?" + Back.RESET + "\n")
		print(Fore.WHITE + "PIEDRA = 0, PAPEL = 1 , TIJERA = 2" + Back.RESET + "\n")
		DatoUser=int(input("INGRESA UNA OPCIÓN>>"))
		print(" ")
		os.system("clear")

		def juego():
			jugada =[[],[],[]]
			try:
				for i in range(turnos+1):
					
					user=DatoUser 
					pc= random.randrange(3)
					jugada[i]=[pc,user]

					print(Fore.WHITE + "-----------------------" + Back.RESET)
					print(Fore.BLUE + "RESULTADOS DE RONDA {0}".format(ronda) + Back.RESET)
					print(Fore.WHITE + "-----------------------" + Back.RESET + "\n")
					print(Fore.GREEN+"PC: {0}".format(manos[pc],manos[user])+Back.RESET)
					print(Fore.YELLOW+"TU: {0}".format(manos[user])+Back.RESET + "\n")
					style = [print(Fore.WHITE + "-"*20 + Back.RESET) for i in range(2)] 
					Pc = [print(Fore.BLUE + " PC GANO UN PUNTO" + Back.RESET ) for p in jugada if p in GanaPc] 
					User = [print(Fore.YELLOW + " GANASTE UN PUNTO" + Back.RESET) for u in jugada if u in GanaUser]
					empate = [print(Fore.WHITE + "QUEDARON EMPATADOS" + Back.RESET) for e in jugada if e in Empate]
					style = [print(Fore.WHITE + "-"*20 + Back.RESET) for i in range(2)]
					if bool(User) == True: UserResultado.append("True")
					if bool(Pc) == True: PcResultado.append("True")
					break
					
			except:
			    print(Fore.RED + "No escogiste una opcion valida, te quedan {0} turnos".format(turnos) + Back.RESET + "\n")
		juego()
		a = input("PRESIONE CUALQUIER TECLA PARA CONTINUAR>>")
		os.system("clear")
	print(Fore.WHITE + "-----------------" + Back.RESET)
	print(Fore.BLUE + "PUNTUACIÓN FINAL" + Back.RESET)
	print(Fore.WHITE + "-----------------" + Back.RESET + "\n")	
	print(Fore.GREEN + "PC: {0}".format(len(PcResultado)))
	print(Fore.GREEN + "USUARIO: {0}".format(len(UserResultado)) + "\n")	
	style = [print(Fore.WHITE + "-"*40 + Back.RESET) for i in range(2)]
	if len(PcResultado) > len(UserResultado):print(Fore.YELLOW + "EL GANADOR FUE PC, INTENTALO DE NUEVO" + Back.RESET) 
	if len(PcResultado) < len(UserResultado):print(Fore.BLUE+ "¡GANASTE, FELICITACIONES!" + Back.RESET) 
	if len(PcResultado) == len(UserResultado):print(Fore.WHITE+ "¡QUEDASTE EMPATADO CON EL PC!" + Back.RESET)
	style = [print(Fore.WHITE + "-"*40 + Back.RESET) for i in range(2)]
	controlsalida()

partida()

