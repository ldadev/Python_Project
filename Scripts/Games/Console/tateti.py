import os
import random
"""
w =[['si','sm','sd'],['mi','mm','md'],['ii','im','id']]


p = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


def juego():
	os.system("clear")	
	print("JUEGO ACTUAL")
	f = [print(str(x) + '\n') for x in p]
	print("COORDENADAS")
	g = [print(str(x) + '\n') for x in w]
	x = input("Ingrese la coordenada>>")
	
	n = -1
	for i in w:
		#Limita la ejecución del for de la linea 18 a solo tres veces
		while n < 2:
			n+=1 #Se obtiene el indice, al iterar en cada lista principal los indices 0,1,2
			m = -1
			for a in i:
				m+=1 #Se obtiene los indices de cada objeto interno, al iterar tres veces en cada lista anidada 
				if x == a:
					p[n][m] = 'O'
					
					#El pc empieza a jugar
					n = -1
					for j in p:
						while n < 2:
							n+=1
							m = -1

							for g in j:
								m+=1
								if not g =='O' and not g == 'X':
									n = -1
									for a in p:
										n+=1

										for h in a:
											s = a.count('O')
											if s == 2:
												p[n][m] = 'X'
												juego()
											else:
												juego()

							break							
			break 
			#Detengo la iteracion al cumplirse la condición interna y se devuelve al for principal.
			#Si no lo hago. cada lista anidada se itera tres veces

juego()
os.system("clear")
print("JUEGO FINAL")	
f = [print(str(x) + '\n') for x in p]

"""


w ={0:{0:'si',1:'sm',2:'sd'},1:{0:'mi',1:'mm',2:'md'},2:{0:'ii',1:'im',2:'id'}}
matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
os.system("clear")

def ingreso():
	juego = False
	jugada =input('Ingresa>>')
	for i in w.keys():
		for t in range(len(w.values())):
			while jugada != '':
				matriz[i][t] = matriz[i][t] + 'X'
				os.system("clear")#borra la impresión anterior en pantalla
				f = [print(str(x) + '\n') for x in matriz]#Entrega una
				ingreso()
ingreso()
