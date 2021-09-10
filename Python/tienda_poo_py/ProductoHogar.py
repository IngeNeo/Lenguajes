from Producto import Articulo

class ProductoHogar(Articulo):
	def __init__(self, codigo = None, nombre = None
				, precio = None, iva = None, stock = None
				, garantia = None, instrucciones = None):
	
		super().__init__(codigo = codigo, nombre = nombre
						, precio = precio, iva = iva, stock = stock )
		self.tiempo_garantia = garantia
		self.instrucciones = instrucciones