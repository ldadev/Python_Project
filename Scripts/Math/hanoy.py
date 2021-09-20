import random
game = [[3,2,1],[0,0,0],[0,0,0]]

#Menor numero


# a) Buscar en cada arreglo el número menor, si el arreglo es mayor a 1
# Tomar el numero menor encontrado y
# guardarlo en un arreglo de tamaño menor a 3, de tal forma que a su derecha halla un numero menor a el y a
# la izquierda un numero mayor a el


num = []

def get_min():

	for i in range(len(game)):
		n = min(game[i])
		num.append(n)
		return n,i
			
def add_min():
	num_min,i = get_min()
	if num_min:
		# Eliminar el numero minimo del array
		game[i].pop(game[i].index(num_min))

add_min()
def save_min():

	for i in range(1,len(game)):
		if sum(game[i]) < 6:
			game[i]+=num
			break
save_min()
add_min()
save_min()
print(game)

# a>b>c
# [8,7,3]

# Numero 8
# []
# 7
#Numero 7
#8
#3
#Numero 3
#7
#[]
def comp_num(lista):
    for index in range(len(lista)):
    	print(sum(lista[index-1:]) < sum(lista[index]))



[[3,2,1],[0,0,0],[0,0,0]]
[[3,2,0],[0,0,0],[1,0,0]]
[[3,0,0],[2,0,0],[1,0,0]]
[[3,0,0],[2,1,0],[0,0,0]]
[[0,0,0],[2,1,0],[3,0,0]]
[[1,0,0],[2,0,0],[3,0,0]]
[[1,0,0],[0,0,0],[3,2,0]]
[[0,0,0],[0,0,0],[3,2,1]]

