

def show_sum():

	flag = True
	suma = 0
	while flag:
		try:
			num = input('Ingresa los numeros a sumar o stop para salir>>').lower()
			if num == 'stop':
				flag = False
			else:
				suma+=int(num)
		except:
			print('Entrada invalida')
	return suma


def show_enter(*args):

	for i in args:
		suma = sum([int(i) for i in i.split(',')])
		print(suma) 
num = input('Ingrese>>')
show_enter(num)

