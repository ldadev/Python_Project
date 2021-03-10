from collections import Counter
import re
import matplotlib.pyplot as plt


with open('file.txt') as file:

	# quitamos los \n, espacios en blanco y signos de puntuación
	lista = re.sub(r'[^\w]',"",file.read())

	#El método maketrans () devuelve una tabla de mapeo que se puede usar con el método 
	#translate () para reemplazar los caracteres especificados. 
	trans = lista.maketrans('áéíóúü','aeiouu')

	#Remplazamos y convertimos a minusculas
	sin_acentos = lista.translate(trans).lower()
	
	# Contamos y ordenamos de forma descendente en en una lista de tuplas
	conteo = Counter(sin_acentos)

	# Grafico de barras
	plt.bar(range(len(conteo)), list(conteo.values()), align='center',color=['indianred','tab:cyan',
		                                                                   'tab:red','tab:green',
		                                                                   'tab:grey','tab:brown'])
	plt.xticks(range(len(conteo)), list(sorted(conteo.keys())))
	plt.title('Conteo de caracteres alfanúmericos')
	plt.xlabel('Caracteres alfanúmericos')
	plt.ylabel('Frecuencias')
	ax = plt.axes()

	# Etiquetas de las barras
	for clave,valor in enumerate(conteo.values()):
		ax.text(clave, valor + 1, valor, ha='center', va='bottom')

	plt.show()