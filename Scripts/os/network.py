

#(0,E97AA872),(1,00AFEA55),(2,0983A872),(3,AAFBFF55)
#(0,00AFEA55),(1,E97AA872),(3,AAFBFF55),(2,0983A872)

charhex = 'E97AA87200AFEA550983A872AAFBFF55'


def  hex_1():

	# Segmentacion de charhex en grupos de 8
	hexpart = [charhex[i:i + 8] for i in range(0,len(charhex),8)]

	# Intercambio de indices
	new_char = [] 
	for i,hexs in enumerate(hexpart):
		if i%2 == 0:
			new_char.insert(i + 1,hexs)
		else:
			new_char.insert(i - 1,hexs)

	print(''.join(new_char))# Union de los grupos de 8



troce = list(map(charhex[0:8],charhex))

print(troce)

