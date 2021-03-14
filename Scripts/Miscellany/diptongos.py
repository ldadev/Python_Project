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

conteo = [(i,texto.count(i)) for i in diptongos]
print(conteo)