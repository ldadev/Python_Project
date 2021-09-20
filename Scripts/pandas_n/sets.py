import pandas as pd

df = pd.read_excel('fileset.xlsx')

try:
	df['resultado'] = [set(c1) - set(c2) for c1,c2 in zip(df['conjuntos1'],df['conjuntos2'])]
except:
	print()
	
print(df.head())
