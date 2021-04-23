from random import randrange
import time
class Estudiante:

	def __init__(self,nombre,apellido):
		self.nombre = nombre
		self.apellido = apellido
		self.codigo = self.__genera_codigo()
		self.email = self.__genera_email()



	def __genera_codigo(self):
		return str(time.localtime().tm_year) + str(randrange(1000,9999))

	def __genera_email(self):
		return self.nombre.split()[0].lower() + "." + self.apellido.split()[0].lower() + "@gmail.com"

	def nombre_completo(self):
		return f"{self.apellido}, {self.nombre}"

	def __repr__(self):
		return f"Estudiante(nombre={self.nombre}, apellido={self.apellido}, codigo={self.codigo}, email={self.email})"



class Est_Curso1(Estudiante):

	def __init__(self,nombre,apellido,codigo,email,nota1=0,nota2=0,nota3=0,nota4=0):
		super().__init__(nombre,apellido)
		self.nota1 = nota1
		self.nota2 = nota2
		self.nota3 = nota3
		self.nota4 = nota4

	def calc_promedio(self):
		return (self.nota1 + self.nota2 + self.nota3 + self.nota4)/4


	def __repr__(self):
		out = f"Estudiante(nombre={self.nombre_completo()}\n"
		out += f"          apellido={self.apellido}\n"
		out += f"          codigo={self.codigo}\n"
		out += f"          email={self.email}\n"
		out += f"          notas=[{self.nota1},{self.nota2},{self.nota3},{self.nota4}]\n"
		out += f"          promedio={self.calc_promedio()}"
		return out
alumno = Estudiante("Elvio Jesus", "Lado Ramos")
alumno.nombre_completo()
print(alumno.nombre_completo())

alumno2 = Est_Curso1("Elvio Jesus","Lado Ramos",10,12,7,14)
print(alumno2)
