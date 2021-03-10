import re



text = 'las aeromozas le quitaron 45x3 el avión al capitan 45/12'


entrada = '-3x53+8'
numeros = re.findall('\d*\,?\d+[+-x/]\d*\,?\d+|[-|+]\d*\,?\d+[+-x/]\d*\,?\d+',entrada)

print(numeros)

"""
def operacion():

	total = 0
	for i in numeros:
		operador = re.findall('[-|+|x|/]',i)
		a,b = re.findall('[-|+]\d+|\d+',i)

		a,b,operador = round(float(a),2),round(float(b),2),operador[1]
		try:
			operaciones = {'+':a+b,'-':a+b,'x':a*b,'/':a/b}
			total+=operaciones[operador]
		except(ZeroDivisionError):
			print('No se puede dividir por 0')
	print(f'El resultado de las operaciones, es {total}')

operacion()
"""
def trans_adn():

	cadena = 'acgttgcaaaccggtt'
	tabla = {'t':'a','a':'t','g':'c','c':'g'}

	cad_comp = [tabla[i] for i in cadena if i in tabla]
	print(cad_comp)


def trans_adn():

	import string 

	cadena = 'acgttgcaaaccggtt'


	#El método maketrans () devuelve una tabla de mapeo que se puede usar con el método 
	#translate () para reemplazar los caracteres especificados. 
	print(cadena.translate(cadena.maketrans('tagc', 'atcg')))



def clasficar_frases():

	texts = 'las aeromozas le quitaron el avión al capitan'

	vowels = ['a','e','i','o','u']
	str_1,str_2,str_3 = [],[],[]

	for word in texts.split():
		if word[0] in vowels:
			str_1.append(word)
		else:
			str_2.append(word)

		if len(word) > 4:
			str_3.append(word)
	print(str_1,'\n',str_2,'\n',str_3,'\n')



def clasificar_letras_1():

	text = 'Hola mundo como esta'
	print(set(''.join(text.split())))

	import re

	frase = input('Ingrese una frase>>')

	# quitamos los espacios en blanco y lo convertimos en conjunto con set()
	letras = set(re.sub(r"\s+", "",frase))
	vocales = set('aeiou')


	# intesercción entre los elementos comunes de vocales y letras
	vocales = vocales & letras

	# Diferencia:Contiene los elementos de letras que no pertenecen a vocales
	consonantes = letras - vocales
	print(vocales,consonantes)



def clasificar_letras__2():


	frase = input('Ingrese una frase>>')

	# quitamos los espacios en blanco y lo convertimos en conjunto con set()
	letras = set(''.join(frase.split()))
	vocales = set('aeiou')


	# intesercción entre los elementos comunes de vocales y letras
	vocales = vocales & letras

	# Diferencia:Contiene los elementos de letras que no pertenecen a vocales
	consonantes = letras - vocales
	print(vocales,consonantes)

