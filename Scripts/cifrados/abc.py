
import random

def valid_enter():

	flag = True
	while flag:
		try:
			user,num_account = input('Ingresa un usuario y numero de cuentas a generar>>(user,4)>>').split(',')
			if int(num_account) > 0:
				return user,int(num_account)
			else:
				print('Número de cuenta mayor a 0. Intenta de nuevo')
		except(ValueError) as e:
			print(f'Entrada invalida. Error {e}')

def generate_mail():

	user,num_account = valid_enter()
	mails = []
	counter = 0
	while num_account > counter:
		num_account-=1
		dominio = '@mail.com.ar'
		abc = list(map(chr,range(97,123)))
		word = random.choice(abc)
		num = random.randrange(100) 
		mails.append([user + word + str(num) + dominio])

	for index,account in enumerate(mails,1):
		print(index,*account)

print(generate_mail())

def cesar(chars,step=0):

	new_char = ''
	for char in chars:
		index = ((ord(char.upper()) - ord('A')) + step) % 27
		new_char+= chr(index + ord('A'))

	print(new_char)

cesar('Hola mundo',3)
