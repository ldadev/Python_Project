

matriz = [['','',''],['','',''],['','','']]
def gana():
	for i in range(len(matriz)):
		if matriz[i][i] == '':
			matriz[i][i] =  matriz[i][i] + 'o'
			print(matriz)



def suma_diagonal():
	suma_diagonal = 0
	for i in range(len(matriz)):
		suma_diagonal+=matriz[i][i] + matriz[i][i-1]
print(suma_diagonal)

entrada = input('Ingresa una posicion>>')

dic_m ={'si':matriz[0][0],'sm':matriz[0][1],'sd':matriz[0][2],'mi':matriz[1][0],'mm':matriz[1][1],
       'md':matriz[1][2],'ii':matriz[2][0],'im':matriz[2][1],'id':matriz[0][0],
       }


def mostrar_matriz():
	for a in range(3):
		for b in range(len(matriz)):
				print(matriz[a][b],end=" ")
		print()



def entradas():
	if entrada in dic_m:
		dic_m[entrada] = 'x'
	
entradas()
