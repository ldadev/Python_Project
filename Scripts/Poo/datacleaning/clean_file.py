import re
from datetime import datetime,date
import pandas as pd
import numpy as np


class Clean_csv:

	def __init__(self,df = 'Dataframe vacio',unique_data = 'No hay datos unicos',column_data = 'Sin columnas.'):

		self.df = df
		self.unique_data = unique_data
		self.column_data = column_data 


	def df_create(self,data):
		
		"""
		Crear un dataframe, Asignado las filas y columnas.Por medio de un diccionario.
		datos = {'Nombre' : ['Juan', 'Laura', 'Pepe'],
    '             Edad': [42, 40, 37],
                 'Departamento': ['Comunicación', 'Administración', 'Ventas']
                 }
		"""
		self.df = pd.DataFrame(data)
	

	def csv_read(self,path):
		#Permite leer un csv

		self.df = pd.read_csv(path)

	def _df_show(self):

		return f'El dataframe es:\n-------------------------------------\n{self.df}'

	def _df_column_show(self,*args):

		for column in args:
			return f'La columna es:\n-------------------------------------\n{self.df[column]}'


	def csv_save(self,path):
		#Permite guardar un csv
		try:
			self.df.to_csv(path)
			print('Dataframe guardado con exito.')
		except Exception as e:
			return f'Error: {e}'


	def column_search(self):
		# Devuelve en una lista el snombre de las columnas de un dataframe
		self.column_data = self.df.columns
		return f'Columnas encontradas con exito '


	def items_count(self): 
		# Permite contar la cantidad total de registros de un dataframe
		return f'Total de registros: {len(self.df.index)}'


	def change_index(self,index:str):
		#Permite cambiar el indice prederminado por una especifico
		try:
			self.df = self.df.set_index(index)
			print(f'Indice {index} cambiado con exito.')
		except Exception as e:
			return f'Error: {e}'
	
	def convert_null_all(self,value,path):
		self.df = self.df.fillna(value) # Cambia los valores null por uno especifico en todo el dataframe

	def convert_value_multi(self,column:str,value_dict:dict):
		"""
		Convierte en varias columnas, un tipo de valor especifico.
		column --> df.column_name
		value_dict --> dict_date of type {'old_name':'new_name'.....}
		"""
		self.df[column] = self.df[column].map(value_dict,na_action=None)
		self.dataframe = df


	def convert_once_value(self,column_n:object,column:str,value):
		"""
		Convierte en una columna, un tipo de valor especifico
		column_n --> df.column_name
		column --> column_name
		value --> 0
		"""
		self.df.loc[column_n == 'nan',column] = value
		self.dataframe = df


	def convert_default_date(self,*args):
		# Convierte un string en fecha'
		try:
			for date in args:
				self.df[date] = pd.to_datetime(self.df[date])
		except Exception as e:
			return f'Error: {e}'
	
	def float_to_int(self,dict_n:dict,keys:list):
		# Permite convertir los valores float a entero en un diccionario
		try:
			dict_new = {}
			for item in keys:
				dict_new[item] = ['{:.0f}'.format(float(item_n)) for item_n in dict_n[item]]
			return dict_new
		except Exception as e:
			return f'Error: {e}'

	
	def convert_date(self,date:str):
		# Convertir fecha en formato Y-m-d  a formato d/m/Y
		try:
			data = datetime.strptime(date,"%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
			return data
		except Exception as e:
			print(f'Error: {e}')


	def unique_search(self,*args):
		#Busca en una conjunto de columnas los datos no repetidos
		try:
			dict_n = []
			for col in args:
				dict_n.append((col,[str(i) for i in self.df[col].unique()]))
			self.unique_data = dict(dict_n)
			return f'Valores unicos determinados con exito.'
		except Exception as e:
			return f'Error: {e}'

	
	def create_file(self,object_n:dict,name_file:str):
		#Crear y guardar un archivo en una ruta especifica
		try:
			with open('/home/david/Programacion/Python_projects/Scripts/files/' + name_file + '.txt','w') as f:
				f.writelines('\n{} = {}\n'.format(key,value) for key,value in object_n.items())
		except Exception as e:
			return f'Error: {e}'


	def convert_eu_to_mil(self,data):
		# Conversión de separadores americanos a separador de mil y coma decimal con dos cifras de precisión
		try:
			data = '{:,.2f}'.format(data).replace('.',',') # Colocamos precisión en el especificador de formato
			comma_num = data.count(',') # Contamos las comas
			data = re.sub('(,)','.',data,count = comma_num - 1,flags=0) # Sustitimos (comma_num - 1) veces la (,)
			return data
		except Exception as e:
			return f'Error: {e}'
	

csv = Clean_csv()
csv.csv_read('/home/david/Programacion/Django_projects/Uvclinical/datacleaning/Affiliates/source/affiliates.csv')
csv.change_index('afiliado_id')
csv.convert_default_date('fecha_afiliacion','fecha_nacimiento')
print(csv._df_column_show(['fecha_afiliacion','fecha_nacimiento']))
df = csv.df
print(csv.unique_search('plan','etnia','descripcion_estamento'))
print(csv.unique_data)
csv.create_file(csv.unique_data,'example')
print(csv.convert_eu_to_mil(101435.0))
#csv.csv_save('/home/david/Programacion/Python_projects/Scripts/Poo/datacleaning/affiliate_clean.csv')


