
from math import sin,cos,radians
"""
Escriba una clase que modele un proyectil lanzado con una velocidad inicial y un angulo de inclinación
que retorne las diferentes propiedades del movimiento y la trayectoria balistica
(altura máxima, alcance máximo,tiempo de vuelo). Utilice decoradores para el control de las propiedades
del objeto.
"""

class Proyectil:
	def __init__(self,vel=60,ang=45):
		self.vel = vel
		self.ang = ang
		self.g = 9.81


	# getter Enmascaramiento de la propiedad vel para que sea privada
	@property
	def vel(self):
		return self.__vel

	@property
	def ang(self):
		return self.__ang

	
	#setter asigna valores a la propiedad self.__vel
	@vel.setter
	def vel(self,val):
		if (isinstance(val,int) or isinstance(val,float)) and val > 0:
			self.__vel = val

		else:
			raise ValueError("El campo 'vel' debe ser un valor positivo")

	def h_max(self):
		return (2 * self.vel * sin(radians(self.ang)) / self.g)

	def x_max(self):
		return (self.vel**2 * sin(2 * radians(self.ang))) / (2 * self.g)

	def t_vuelo(self):
		return (self.vel**2 * sin(radians(self.ang))**2) / (2 * self.g)


	@ang.setter
	def ang(self,val):
		if 0 <= val <= 90:
			self.__ang = val
		else:
			raise ValueError("El campo 'ang' debe ser un valor entre 0 y 90 grados")


	def __repr__(self):
		return f'Proyectil(vel={self.vel} km/h, ang={self.ang}°)'


proy = Proyectil(vel=10,ang=90)
print(proy)	

print("h_max:",proy.h_max(),"m")
print("x_max:",proy.x_max(),"m")
print("t_vuelo:",proy.h_max(),"seg")




