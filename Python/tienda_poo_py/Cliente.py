from Persona import Persona

class Cliente(Persona):

	def __init__(self, codigo = None, nombre = None
				, email = None, telefono = None, categoria = None):
		super().__init__(codigo=codigo, nombre=nombre, email=email, telefono=telefono)
		self.categoria = categoria