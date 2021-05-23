import numpy as np

matriz_1 = [[0,0,9],[0,1,9],[1,0,9],[1,1,9]]

# Sin numpy
for row in matriz_1:
	for col in row:
		if col > 1:
			matriz_1[matriz_1.index(row)][row.index(col)] = 1
		else:
			matriz_1[matriz_1.index(row)][row.index(col)] = 0

print(matriz_1)

#Con numpy
matriz_1 = np.array([[0,0,9],[0,1,9],[1,0,9],[1,1,9]])
matriz_2 = np.where(matriz_1>1,1,(np.where(matriz_1<1,0,matriz_1)))
print(matriz_2)

