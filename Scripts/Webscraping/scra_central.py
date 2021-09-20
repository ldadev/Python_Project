#!/usr/bin/env python

from utility import *
import json

from collections import OrderedDict


"""

def mostrar_menu():

	while True:
		try:
			clean()# LImpieza de pantalla
			import pandas as pd
			import requests
			from bs4 import BeautifulSoup
			from tabulate import tabulate

		except ModuleNotFoundError as e:
			print('Faltan modulos por instalar. Ejecute pip install -r requirements.txt:',e,sys.exc_info()[0])
			break

		try:
			res = requests.get("http://vicebienestar.univalle.edu.co/restaurante-universitario")
			soup = BeautifulSoup(res.content,'html')
			table = soup.find_all('table')[0]
			headers = [head.text for head in table.find_all("th")]
			table_data = [[cell.text for cell in row("td")] for row in table.find_all("tr")]
			print(dict(table_data[1:-1]))
			#table = soup.find_all('table')[0]
			#df = pd.read_html(str(table))
			
			#print(tabulate(df[0].head(),headers='keys',stralign ='center',tablefmt = 'fancy_grid',showindex=False))
			exit_py()# Salida del script
		except IndexError as e:
			print('No se encontraron los recursos:',e,sys.exc_info()[0])
			break
		
			
	
if __name__ == '__main__':
    mostrar_menu()
"""


import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("http://vicebienestar.univalle.edu.co/restaurante-universitario")
soup = BeautifulSoup(res.content,'html')
table = soup.find_all('table')[0]
headers = [head.text for head in table.find_all("th")]
table_data = [[cell.text for cell in row("td")] for row in table.find_all("tr")]

alimentos = []
for item in table_data[1:-1]:
	alimentos.append([item[0],item[1:]])


print(json.dumps(dict(alimentos)))

