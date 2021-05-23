strs_1 =[10,40,30,20]
strs_2 = [1,-1,1,-1,1,-1]

"""
Teniendo N elementos de una lista.
Un punto espejo es aquel indice i,tal que (0 < i > N)
"""
def mirrow(strs):
	for i in range(1,len(strs) - 1):
		if (sum(strs[:i]) == (sum(strs[i:]))):
			print(i)
mirrow(strs_2)



