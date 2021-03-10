import os, sys

def clean():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")



def exit_py():

	salida =input('¿Desea consultar de nuevo el menu? s/n>>')
	if salida == 'n':
		return sys.exit()


