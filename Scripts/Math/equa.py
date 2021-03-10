
import re

equation = '-6-3x-8x'
char = re.findall('[x]|[-|+][x]|[-|+]\d+[x]|[-|+]\d+',equation)
print(char)


char_2 = re.findall('[-|+]\d+[x]',equation)
print(char_2)
 
texto = "551 889 302 105 012 817 894 206"
 
patron = "[0-9]{2}[13579]"
 
x = re.findall(patron, texto) #Devuelve un vector con los substrings de las ocurrencias
 
for i in x:
    print(i)