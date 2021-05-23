#!/usr/bin/python
import os
import time

#os.system('/home/david/Programacion/Python_projects/Scripts/commands/./example.py')

from subprocess import check_output

comando = '/home/david/Descargas/SQLiteStudio/./sqlitestudio'
check_output(comando,shell=True)
