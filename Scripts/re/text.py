import re

# Extracción de correos electronicos
s = 'Una nota de csev@umich.edu a cwen@iupui.edu sobre una reunión @ 2PM'
lst = re.findall(r'\S+@\S+', s)



# resolver ecuacion de primer grado
#2x + 5 - 3x + 9x = 3x -9 + 10 -5x
#ecuacion = 2x+5-3x+9x-3x+9-10+5x

"""
grupo_1 = re.sub('\s','',ecuacion)
grupos = [re.findall(r'[-|+]\d+\b',grupo_1)] + [re.findall(r'[-|+]\d+',''.join(re.findall(r'[-|+]\d+x',grupo_1)))]
op_co = sum([int(i) for i in grupos[0]])
op_lit = sum([int(i) for i in grupos[1]])

resultado = '+' + str(op_lit)+ 'x' + '+' + str(op_co) if op_lit or op_co > 0 else '-' + str(op_lit) + 'x' + '-' + str(op_co)
print(resultado)
"""



"""

statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w+]+)@([\w\.-]+)', statement)
if statement:
  print("Email address:", match.group()) # The whole matched text
  print("Username:", match.group(1)) # The username (group 1)
  print("Host:", match.group(2)) # The host (group 2)
"""