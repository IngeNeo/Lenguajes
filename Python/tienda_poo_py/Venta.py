from Cliente import Cliente
from Cajero import Cajero
from caja import Caja
class Venta:

	def __init__(self, fecha = None, cliente = None, cajero = None, sede = None, caja = None):
		self.fecha = fecha
		self.cliente = cliente
		self.cajero = cajero
		self.sede = sede
		self.caja = caja