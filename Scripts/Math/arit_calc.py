# -2+5*7/2

from functools import reduce

sumandos = [-2]
factores = [100,2,2]

producto = reduce(lambda acumulador=0, elemento=0: acumulador - elemento, factores)
print(producto)

"""
import string
s = 'I have 6 * (2+3) apples'
symbols = '^*()/+-'
formula = [(x,s.index(x)) for x in s if x in string.digits+symbols]
print(formula)
result = eval(''.join(x[0] for x in formula), {'__builtins__':None})
print(result)
s = s[:formula[0][1]] + str(result) + s[formula[-1][1]+1:]
print(s)
"""
"""
import string

simbolos = '^*()/+-'

mensaje = '''Faltan ((40**2)/400)-1 dias aproximadamente para empezar 
a ver Forrest Gump y asi,recibir el año nuevo con el teniente Dan.'''

numeros = [i for i in mensaje if i in string.digits+simbolos]
dia = int(eval(''.join(numeros)))
print(dia,'días')

"""