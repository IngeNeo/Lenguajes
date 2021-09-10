## clase producto
class Articulo:
	# propiedad de la clase	
	def __init__(self, codigo = None, nombre = None, precio = None, iva = None, stock = None ):
		self.codigo = codigo
		self.nombre = nombre
		self.precio = precio
		self.iva = iva
		self.stock = stock