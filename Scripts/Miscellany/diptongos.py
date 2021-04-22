#Diptongos crecientes	ua, ue, uo, ia, ie, io
#Diptongos decrecientes	ai, ei, oi, au, eu, ou
#Diptongos homogéneos	iu, ui


diptongos = 'ua','ue','uo','ia','ie','io','ai','ei','oi','au','eu','ou','iu','ui'

texto = """
Laura y aurora escucharon un aullido 
en la lejanía; quisieron saber de dónde venía,
pero sólo pudieron ver a un gaucho que pasaba por el lugar,
a quien le dijeron; si averiguáis quién causó el aullido 
le daremos una recompensa mi querido señor.
"""


def dip_1():

	conteo = [(i,texto.count(i)) for i in diptongos]
	print(conteo)


def dip_2():

	conteo = {i:texto.count(i) for i in diptongos}
	print(conteo)


conteo = map(lambda x:(x,texto.count(x)),diptongos)
#print(*conteo)

from collections import Counter
import re
print(Counter(re.findall(r'^\w[au]',texto)))