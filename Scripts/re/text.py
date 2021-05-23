import re

# Extracción de correos electronicos
s = 'Una nota de csev@umich.edu a cwen@iupui.edu sobre una reunión @ 2PM'
lst = re.findall(r'\S+@\S+', s)



# resolver ecuacion de primer grado
#2x + 5 - 3x + 9x = 3x -9 + 10 -5x
ecuacion = '2x+5-3x+9x-4x+9-10+11x'


def conver_1():

	grupo_1 = re.sub('\s','',ecuacion)
	grupos = [re.findall(r'[-|+]\d+\b',grupo_1)] + [re.findall(r'[-|+]\d+',''.join(re.findall(r'[-|+]\d+x',grupo_1)))]
	op_co = sum([int(i) for i in grupos[0]])
	op_lit = sum([int(i) for i in grupos[1]])
	print(grupos)
	resultado = '+' + str(op_lit)+ 'x' + '+' + str(op_co) if op_lit or op_co > 0 else '-' + str(op_lit) + 'x' + '-' + str(op_co)
	print(resultado)

"""
statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w+]+)@([\w\.-]+)', statement)
if statement:
  print("Email address:", match.group()) # The whole matched text
  print("Username:", match.group(1)) # The username (group 1)
  print("Host:", match.group(2)) # The host (group 2)
"""

def equation():

	import re

"""

re.findall(pattern, string, flags=0)
 
Retorna todas las coincidencias no superpuestas del pattern («patrón») en la string («cadena»), como una lista de cadenas. La cadena es examinada de izquierda a derecha, y las coincidencias son retornadas en el orden en que fueron encontradas. Si uno o más grupos están presentes en el patrón, retorna una lista de grupos; esta será una lista de tuplas si el patrón tiene más de un grupo. Las coincidencias vacías se incluyen en el resultado.

\
señala una secuencia especial

+
Hace que la RE resultante coincida con 1 o más repeticiones de la RE precedente.

\w

Para los patrones de Unicode (str):
Coincide con los caracteres de palabras de Unicode; esto incluye la mayoría de los caracteres que pueden formar parte de una palabra en cualquier idioma, así como los números y el guión bajo. Si se usa el indicador ASCII, sólo coincide con [a-zA-Z0-9_].

^
Circunflejo para la negación de un patrón.

\d

Para los patrones de Unicode (str): Coincide con cualquier 
dígito decimal de Unicode (es decir, cualquier carácter de la 
categoría de caracteres de Unicode

[]

Se utiliza para indicar un conjunto de caracteres. En un conjunto

...

Coincide con cualquier expresión regular 
que esté dentro de los corchetes.

A|B

Donde A y B pueden ser RE arbitrarias, 
crea una expresión regular que coincidirá con A ó B.
"""

equation = '3*x**2+5*x+9-3**2'
example = re.findall('^[\w..\d+]|[-+]\d+',equation)
print(example)