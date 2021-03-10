import os

game = True
os.system('clear')# Limpiar pantalla
while game:
	print('Bienvenido al juego calabozos y dragones')
	perfiles = {'clases':{1:'Mago',2:'Hechicero',3:'Guerrero',
	           4:'Barbaro',5:'Asesino',6:'Ladron'},
	           'razas':{7:'Humano',8:'Elfo',9:'Orco',
	            10:'Halfling',11:'Enano'}}

	#Menu de los perfiles
	print('{:^30}{:^10}'.format('CLASES','RAZAS'))
	for clave,perfil in zip(perfiles['clases'],perfiles['razas']):
		print('{:^10}{:^10}{:^10}{:^10}'
			.format(clave,perfiles['clases'][clave],
				    perfil,perfiles['razas'][perfil]))
	try:
		opt_clase,opt_raza = input('Selecciona la clase y la raza>>').split(',')
		clase = perfiles['clases'].get(int(opt_clase),'No hay clase')
		raza = perfiles['razas'].get(int(opt_raza),'No hay raza')
		print(f'Personaje elegido:{clase} {raza}')
		
		final_opt = input('¿Deseas continuar s/n?>>').lower()
		os.system('clear')# Limpiar pantalla	

		if final_opt == 'n':
			game = False
			print('¡Hasta luego!')
	except:
		print('Entrada incorrecta. Intentalo de nuevo.')



	

	         



