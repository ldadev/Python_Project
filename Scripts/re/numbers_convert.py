import re
from datetime import datetime,date
import pandas as pd
import numpy as np


class Clean_csv:

	def __init__(self,data,list_col):
		
		self.data = data
		self.list_col = list_col
		self.df = pd.DataFrame(self.data,columns = self.list_col)# Construcción de un dataframe
		self.dataframe = None

	#Cambiar todos los valores de una columna especifica. value_dict --> diccionario 
	def convert_value_multi(column,value_dict):
		self.df[column] = self.df[column].map(value_dict,na_action=None)

	# Convierte en una column especifica, un tipo de valor especifico
	def convert_once_value(self,column_n,column,value):
		self.df.loc[column_n == 'nan',column] = value
		self.dataframe = df

	def __str__(self):
		return f'Los valores convertidos son:\n{self.dataframe}'

csv = Clean_csv({'name':['michael','louis','jack','jasmine'],'city':['berlin','paris','roma','nan']},['name','city'])
df = csv.df
csv.convert_once_value(df.city,'city',0)
print(csv)


import locale

locale.setlocale(locale.LC_ALL,'en_US')
def convert(number):
	return locale.format_string("%f",number,grouping = True)
output = convert(1234567.232323)
print(output)

"""
"""
#Cambiar todos los valores de una columna especifica. 
#Recibe el nombre de la columna y un diccionario de los valores a cambiar
"""
def convert_value_multi(column,value_dict):
	df[column] = df[column].map(value_dict,na_action=None)
	return df

#print(convert_value_multi('city',{'nan':0}))

# Convierte en una column especifica, un tipo de valor especifico
def  convert_once_value(df_column,column = ''):
	df.loc[df_column == 'nan',column] = 0
	return df
"""
#print(convert_once_value(df.city,'city'))

"""
def clean_csv(index_n = ''):

	# Leer archivo csv
	open_path = '/home/david/Programacion/Django_projects/Uvclinical/datacleaning/Affiliates/source/affiliates.csv'
	end_path = '/home/david/Programacion/Django_projects/Uvclinical/datacleaning/Affiliates/clean/clean_affiliate.csv'
	df = pd.read_csv(path)

	# Buscar las columnas de df
	print(f'Columnas del df: {df.columns}')

	# Contar los registros  de un df
	print(f'Cantidad de registros: {len(df.index)}')

	# Cambiar el indice predeterminado por uno especifico
	df = df.set_index(index_n)
	# Guardar csv
	df.to_csv(end_path)


def convert_date():
	path = '/home/david/Programacion/Django_projects/Uvclinical/datacleaning/Affiliates/clean/clean_affiliate.csv'
	for date in dates:
		df[date] = pd.to_datetime(df[date])
		df.to_csv(path)


def unique_search():
	dict_n = []
	for col in columns:
		dict_n.append((col,[str(i) for i in df[col].unique()]))
	dict_n = dict(dict_n)
	return dict_n


def convert_null(value,path):
    # Cambia los valores null por uno especifico
    df = df.fillna(value)
    df.to_csv(path)


# Convertir float a entero
def float_to_int(dict_n,keys = []):

	dict_new = {}
	for item in keys:
		dict_new[item] = ['{:.0f}'.format(float(item_n)) for item_n in dict_n[item]]
	return dict_new

# Convertir fecha Y-m-d  a d/m/Y
def convert_date(value):

	try:
		data = datetime.strptime(value,"%Y-%m-%d").strftime("%d/%m/%Y")
		return data
	except Exception as e:
		print(f'Error: {e}')


# Guardar archivo  en una ruta especifica
def create_file(object_n,name_file = ''):
	with open('/home/david/Programacion/Python_projects/Scripts/re/texts/' + name_file + '.txt','w') as f:
		f.writelines(str(object_n))

create_file(float_to_int(col_affiliates,['dpto_residencia','mpio_residencia']),'col_affiliates')


# Conversión de separadores americanos a separador de mil y coma decimal con dos cifras de precisión
def convert_eu_to_mil(array):
	for index,value in enumerate(nums):
		# Colocamos precisión en el especificador de formato
	    nums[index] = '{:,.2f}'.format(value).replace('.',',')
	    #Contamos las comas
	    comma_num = nums[index].count(',')
	    #Sustitimos (comma_num - 1) veces la (,)
	    nums[index] = re.sub('(,)','.',nums[index],count = comma_num - 1,flags=0)

# output --> ['12.131,30', '2.136.789,20', '135.789.231,14']



"""



