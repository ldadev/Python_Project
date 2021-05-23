def contador(user,min,max):
		
	if min<=user<=max:
		return f'El número {user} esta entre {min} y {max}'
	else:
		return f'El número {user} no esta entre {min} y {max}'

print(contador(10,3,50))