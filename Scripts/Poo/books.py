#Primera forma
class Libro:

	def __init__(self):
		self.libro = "Harry potter y la piedra filosofal"

	def __repr__(self):
		return f'El libro {self.libro} no se encuentra disponible'


libro_n = Libro()

print(libro_n)


#Segunda forma
class Libro:

	def __init__(self,libro):
		self.libro = libro

	def __repr__(self):
		return f'El libro {self.libro} no se encuentra disponible'


libro_n = Libro("Harry potter y la piedra filosofal")
print(libro_n)