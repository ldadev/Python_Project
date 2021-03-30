
matriz =[[1,2,3],
         [4,5,6]]
 


"""
 1 (0,0)
 2 (0,1)
 3 (0,2)
 4 (1,0)
 5 (1,1)
 6 (1,2)
 """
for row,submatriz in enumerate(matriz):
	for i,num in enumerate(submatriz):
		print((row,i),num)
