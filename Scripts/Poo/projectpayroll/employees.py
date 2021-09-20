import disgruntled

"""
El sistema de recursos humanos necesita procesar
la nómina de los empleados de la empresa, pero existen
diferentes tipos de empleados dependiendo de cómo se calcule su nómina.

El sistema de recursos humanos requiere que cada Employee procesado debe proporcionar
 una .calculate_payroll() interfaz que devuelva el salario semanal del empleado.
  La implementación de esa interfaz difiere según el tipo de Employee.
"""

class Employee:

	"""
	clase base Employee que maneja la interfaz común para cada tipo de empleado.
	Esta es la clase base para todos los tipos de empleados.
	Está construido con una id y una name. Lo que está diciendo es que cada uno 
	Employee debe tener un nombre id asignado y un nombre.
	"""
	def __init__(self, id, name):
		self.id = id
		self.name = name


class PayrollSystem:

	"""
	PayrollSystem implementa un .calculate_payroll(), método que toma un conjunto
	de empleados e  imprime su id, name y la cantidad del cheque mediante el .calculate_payroll()
	método expuesto en cada objeto empleado.
	"""
	def calculate_payroll(self, employees):
		print('Calculating Payroll')
		print('===================')
		for employee in employees:
			print(f'Payroll for: {employee.id} - {employee.name}')
			print(f'- Check amount: {employee.calculate_payroll()}')
			print('')


class SalaryEmployee(Employee):

	"""
	Los trabajadores administrativos tienen un salario fijo,
	por lo que cada semana se les paga la misma cantidad.

	La clase derivada SalaryEmployee que hereda Employee. 
	La clase se inicializa con id y  name requerida por la clase base, y se usa super() 
	para inicializar los miembros de la clase base. 

	SalaryEmployee también requiere un weekly_salary parámetro de inicialización que 
	representa la cantidad que el empleado gana por semana.

	La clase proporciona el .calculate_payroll() método requerido utilizado 
	por el sistema de recursos humanos. La implementación solo devuelve la cantidad almacenada en weekly_salary.
	"""

	def __init__(self, id, name, weekly_salary):
		super().__init__(id, name)
		self.weekly_salary = weekly_salary

	def calculate_payroll(self):
		return self.weekly_salary

class HourlyEmployee(Employee):

	"""
	La empresa también emplea trabajadores de fabricación a los que se les paga por hora, 
	por lo que agrega un HourlyEmployee al sistema de recursos humanos.

	La clase HourlyEmployee se inicializa con id y name, como la clase base, 
	más hours_worked y el hour_rate requerido para calcular la nómina. 
	El .calculate_payroll() método se implementa devolviendo las horas trabajadas por la tarifa por hora.
	"""

	def __init__(self, id, name, hours_worked, hour_rate):
		super().__init__(id, name)
		self.hours_worked = hours_worked
		self.hour_rate = hour_rate

	def calculate_payroll(self):
		return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):

	"""
	Finalmente, la empresa emplea asociados de ventas a los que se les paga a 
	través de un salario fijo más una comisión basada en sus ventas, 
	por lo que crea una CommissionEmployee.

	Se deriva CommissionEmployee de SalaryEmployee porque ambas clases tienen weekly_salary que considerar. 
	Al mismo tiempo, CommissionEmployee se inicializa con un commission valor que se basa en las ventas 
	para el empleado.

	.calculate_payroll() Aprovecha la implementación de la clase base para recuperar el fixed salario y
	 agrega el valor de la comisión.

	 Dado que se CommissionEmployee deriva de SalaryEmployee, tiene acceso a la weekly_salary 
	 propiedad directamente y podría haber implementado .calculate_payroll() utilizando el valor de esa propiedad.
	"""
	def __init__(self, id, name, weekly_salary, commission):
		super().__init__(id, name, weekly_salary)
		self.commission = commission

	def calculate_payroll(self):
		fixed = super().calculate_payroll()
		return fixed + self.commission



"""
Primero, agrega una Managerclase que deriva de SalaryEmployee.
La clase expone un método work()que será utilizado por el sistema de productividad.
El método toma hoursel empleado trabajado.

A continuación, se agrega Secretary, SalesPersony FactoryWorker a continuación, 
implementar la work() interfaz, para que puedan ser utilizados por el sistema de productividad.

"""
class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')

class TemporarySecretary(HourlyEmployee, Secretary):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name, hours_worked, hour_rate)