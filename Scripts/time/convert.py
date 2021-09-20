
from datetime import datetime 
def convert_date(date):
		# Convertir fecha en formato Y-m-d  a formato d/m/Y
		try:
			data = datetime.strptime(date,"%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")
			return data
		except Exception as e:
			print(f'Error: {e}')

print(convert_date('2021-04-03 00:00:00'))