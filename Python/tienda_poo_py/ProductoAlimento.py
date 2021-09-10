from Producto import Articulo

class ProductoAlimento(Articulo):
	def __init__(self, codigo = None, nombre = None
				, precio = None, iva = None, stock = None 
				, vencimiento = None, fecha_creacion = None):
		super().__init__(codigo = codigo, nombre = nombre
						, precio = precio, iva = iva, stock = stock )
		self.fecha_vencimiento = vencimiento
		self.fecha_produccion = fecha_creacion