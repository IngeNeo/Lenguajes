from Persona import Persona

class Cajero(Persona):
	def __init__(self, codigo = None, nombre = None, email = None, 
				telefono = None, contrato = None, salario = None):
		super().__init__(codigo=codigo, nombre=nombre, email=email, telefono=telefono)
		self.numero_contrato = contrato
		self.salario = salario