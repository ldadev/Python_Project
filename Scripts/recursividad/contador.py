def contar_rec(elem,accumulador = 0):

	"""
	Contador de numeros. con función recursiva.
	"""

	if elem == 0:
		return accumulador # Caso base
	else:
		accumulador += elem
		return contar_rec(elem - 1,accumulador)

print(contar_rec(4),contar_rec.__globals__)



"""
elem = 0 + acumulador = 4 --> 4 acumulador
(4 - 1,4)
elem = 3  + acumulador = 4--> 7 acumulador
(3 -1,7)
elem = 2 + acumulador = 7 -->  9 acumulador
(2-1,7)
elem = 1 + acumulador = 9 -- > 10 acumulador
(1 - 1,10) -->10 acumulador

"""



"""
- - - - -
-       -
-       -
-       -
-       -
- - - - -

"""
print(((('- '*5) + ' '*20 + ('- '*5))  + '\n')*5)
print(((('- '*5) + ' '*20 + ('- '*5))  + '\n')*5)
print(((('- '*5) + ' '*20 + ('- '*5))  + '\n')*5)
print(((('- '*5) + ' '*20 + ('- '*5))  + '\n')*5)


print('\n'.join([''.join([('someonemissin'[(x-y)%13]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

