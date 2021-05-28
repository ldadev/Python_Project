"""
1) Puede usar \n para el salto de linea.

2) En la linea 8. El metodo string 
divide una cadena en una lista.
Puede especificar el separador, el separador predeterminado es cualquier 
espacio en blanco.string.split(separator, maxsplit) 

3) Y en la linea tres. Se invierte mediante slice. O puede ussar la funcón reverse().
"""

texto = 'La mariposa revolotea\ncomo si desesperara\nen este mundo'.split('\n')
texto2 = ''
for i in texto:
	texto2+=i[::-1] + '\n'
print(texto2)

