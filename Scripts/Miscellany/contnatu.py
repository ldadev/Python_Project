import re # Este módulo proporciona operaciones de coincidencia de expresiones regulares


"""

re.findall(pattern,string,flags = 0)

Devuelve todas las coincidencias no superpuestas de patrón en cadena, 
como una lista de cadenas. La cadena se escanea de izquierda a derecha
 y las coincidencias se devuelven en el orden en que se encuentran.

\D Coincide con cualquier carácter que no sea un dígito decimal. 
Esto es lo opuesto a \d. Si se usa el indicador ASCII esto se
 convierte en el equivalente a [^0-9].
"""
#-1+30-5
#1+30-2
entrada = input('Ingresa la suma>>')

numeros = re.findall('\d+',entrada)# Separo los números de las letras
print(numeros)

#for x in numeros:
	#suma+=int(x)# Sumo cada número x a suma
#print(f'La suma de los números naturales es:{suma}')
