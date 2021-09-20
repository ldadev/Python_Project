
"""
La clase rastrea a los empleados en el track()método que toma una 
lista de empleados y la cantidad de horas para rastrear. Ahora puede 
agregar el sistema de productividad a su programa:
"""
class ProductivitySystem:

	def track(self, employees, hours):
		print('Tracking Employee Productivity')
		print('==============================')
		for employee in employees:
			employee.work(hours)
		print('')