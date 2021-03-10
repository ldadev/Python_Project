
import pandas as pd
import matplotlib.pyplot as plt


estudiantes = [['1','f','t'],['2','f','t'],['4','m','t'],['5','m','t'],['6','m','t']]


"""
contador = 0
num_est = int(input('Ingresa la cantidad de estudiantes a registrar>>'))

while contador < num_est:
	contador+=1
	entrada = input('Ingresa seguido de una coma, (código,sexo(m/f),ocupación(t/e)>').lower().split(',')
	estudiantes.append(entrada)
"""

#pd.crosstab(tips.sex, tips.smoker)

df = pd.DataFrame(estudiantes)
df.columns = ['Código','Sexo','Ocupación']
freq = pd.crosstab(df.Sexo,df.Ocupación)

for a,b in freq:
	print(a,b)

"""
my_plot = plt.hist(freq)
plt.xlabel('Sexo')
plt.ylabel('Ocupación')
plt.show()
#print(freq)
"""