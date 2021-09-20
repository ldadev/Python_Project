class DisgruntledEmployee:

	
	"""
	La DisgruntledEmployee clase no deriva de Employee , pero expone la misma interfaz requerida 
	por PayrollSystem. El PayrollSystem.calculate_payroll() requiere una lista de objetos que 
	implementan la interfaz siguiente:

    * Un id propiedad o atributo que devuelve la identificación del empleado.
    * Un name propiedad o atributo que representa el nombre del empleado.
    * Un .calculate_payroll() método que no toma ningún parámetro y devuelve el monto de la nómina para procesar

    Todos estos requisitos los cumple el DisgruntledEmployee clase, por lo PayrollSystemque aún puede calcular su nómina.
	"""

	def __init__(self, id, name):
	    self.id = id
	    self.name = name

	def calculate_payroll(self):
	    return 1000000
