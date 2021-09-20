# Determinante e inversa de una matriz

import random
import numpy as np

def create_matriz_2(rows,columns):

	matriz = [ [random.randint(1,6) for col in range(columns)] for row in range(rows)]
	return matriz


"""
[[1,0],
 [0,1]]
"""

# Con ceros --> m[0][1] and m[1][0] 
# Sin ceros --> m[0][0] and m[1][1]

# Seleccionar la columna 2 --> matriz[:,1]
# Seleccionar ambas columnas --> matrix[:,:1]

# Seleccionar la fila 2 --> matrix[1,:]

matriz = np.array([[3,4],
	               [2,-1]])

#mat_iden = np.array([[1,0],[1,0]])



#mat_iden = np.identity(2)# Matriz indentidad 2 x 2
#mat_concat = np.concatenate((matriz,mat_iden),axis = 1)



#suma = (abs(a)*(b)) + a # Esquinas con 0
#mult = a / a # Esquinas con 1
#mult_1 = (-1)*matriz[0,:]# Esquinas con 1

n = 2
diag_1 = [i/i for i in matriz[0,:]]# Unos
diag_2 = sum([matriz[i][n - i - 1] for i in range(n)]) # Ceros
print(diag_1)
