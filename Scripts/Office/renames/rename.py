
dir_path = '/home/david/Programacion/Python_projects/Scripts/Office/renames/files/'


import os
import re
from re import search



# Primera forma

def rename_1():

	for file in os.listdir(dir_path):
		new_name = re.sub('\d+','', file)
		num = re.findall('\d+',file)# Capture numbers
		os.rename(dir_path + file,dir_path + (str(*num)) + new_name)# *Descomprime la lista de números





# Segunda forma
def rename_2():
	
	for file in os.listdir(dir_path):
		result = search("^(.+?)(\d+)(\..+$)",file)
		if(result):
			newName = result.group(2) + result.group(1) + result.group(3)
			os.rename(dir_path + file,dir_path + newName)


