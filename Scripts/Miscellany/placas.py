import random
from itertools import *
#aei877

abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
      'N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#AAA --> 000-000 Y ZZZ --> 272727-999
#390
# ZRY865 --> 261925-865
user = 'ZRY865'

placas = list(combinations(abc,3))
lista = []
for index,value in enumerate(placas):
	if index < 999:
		p = random.choice(placas)
		lista.append(p)



a,b,c = [int(abc.index(i)) for i in user if i.isalpha()]
anti_num = {range(99,300):'Viejo',range(301,600):'Medio',range(601,999):'Nuevo'}


print(lista)


"""
for i in words:
	words = random.randint(100,999)
	numbers = random.randint(100,999)
	print(words,numbers)


"""

#261825 --> 26-18-25