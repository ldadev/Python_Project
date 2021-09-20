import sys

"""
--------------------
Por: David Martinez
--------------------

-------------------
ENCRIPTACIÓN CESAR
-------------------

En esta encriptación se puede usar la aritmetica modular. El Nuevo indice, letra encriptada. 
Se obtiene, teniendo en cuenta que el dividendo = divisor x cociente + residuo.

a) Si el residuo es menor al divisor. Entonces el residuo es igual al dividendo 
   al aplicar dividendo MOD divisor.

b) Si el dividendo  es mayor al divisor, entonces dividendo MOD divisor es igual al residuo.

------------------------
DESCRIPCIÓN DEL PROGRAMA
------------------------

------------------------------------
Parametros del metodo de cesar
------------------------------------

parametro_1 : path

El usuario ingresa la ruta del a encriptar o desencriptar

parametro_2:key

Escoge la clave a usar para encriptación.

parametro_3:opt

La opción correspondiente. 1 para encriptar o -1 para desencriptar

--------------------------------------
Descripción del metodo cesar
-------------------------------------

a)
   La función encry_decry retorna la linea de texto encriptado o desencriptado.
   y la función create_file retorna el texto completo encriptado o deencriptado.

b)

   En la variable trans_abc se usa el algoritmo basado en la aritmetica modular.
   para generar los nuevos indices de acuerdo a la clave y opción ingresada por el usuario.

   Usando el nombre de las variables en la función encry_decry  del programa, tenemos:

   Posicion de la nueva letra = (posicion de letra en symbol_main + key) MOD len(symbol_main)

c)
   Después el método maketrans () crea una tabla de mapeo y el método translate () devuelve 
   una cadena donde algunos caracteres especificados  se reemplazan con el carácter descrito 
   en un diccionario o en una tabla de mapeo.

"""

class File_operations:

	def __init__(self,path = '',file_name = 'text',text_lines = ['Hola mundo']):

		self.path = path
		self.__file_name = file_name + '.txt' 
		self.text_lines = text_lines
		self.file = None
		self.text_content = None


	@property
	def file_name(self):
		return self.__file_name

	@file_name.setter
	def file_name(self,val):

		if isinstance(val,str):
			self.__file_name = val
		else:
			print('El campo file_name debe ser una cadena de texto.')
	
		
	def create_file(self):

		self.file = open(self.path + self.file_name,'w')

	def read_file(self):

		with open(self.path + self.file_name,'r') as file:
			for text_line in file:
				self.text_lines.append(text_line)
		print(self.text_lines)

	def write_file(self):

		with open(self.path +  self.file_name,'w') as file:
			file.writelines(text_line for text_line in self.text_content)

class Encry_decry(File_operations):

	def __init(self,encry_text):
		super().__init__(self.text_lines)

	def cesar(self):

		flag = True

		while flag:
			try:
				key,opt = input('Ingresa la clave y 1 para encriptar o -1 para desencriptar. Ej: 3,1>>').split(',')
				key,opt = int(key),int(opt)
				symbol_main = list(chr(code) for code in range(32,256))
				trans_abc = [symbol_main[(symbol_main.index(letter) + opt*key) %len(symbol_main)] for letter in symbol_main]
				encry_text = []
				for text_line in self.text_lines:
					map_table = text_line.maketrans(''.join(symbol_main),''.join(trans_abc))
					encry_n = text_line.translate(map_table) 
					encry_text.append(encry_n)
				self.text_content =  encry_text
				flag = False
			except Exception as e:
				print(f'Opción incorrecta.')



"""
args = None
if len(sys.argv) == 4:
	args = sys.argv
else:
	args = ['script_name','','text','hola']

script_name,path,file_name,text_lines = args

encry_decry = Encry_decry(path,file_name,text_lines)

flag = True
while flag:
	try:
		option = input('Ingresa la opción correspondiente.')
		options = {'1':encry_decry.create_file(),'2':encry_decry.read_file(),'3':encry_decry.write_file(),'4':encry_decry.cesar()}
		print(option)
		flag = False
	except Exception as e:
		print(f'Opción incorrecta. Intentalo de nuevo. {e}')

"""



enter = 'BOOMMMLLFFFFXXWWWZZZUUUUV'


# Primera opción
counter_1 = {}
for letter in enter:
	counter_1[letter] = enter.count(letter)


# Segunda opción
counter_2 = {letter:enter.count(letter) for letter in enter}


# Tercera opción

from collections import Counter

counter_3 = Counter(enter)


















