from Venta import Venta
from Cajero import Cajero
from caja import Caja
from Cliente import Cliente
from Producto import Articulo
from Cliente import Cliente
from caja import Caja
from Cajero import Cajero

p1 = Articulo(codigo="123", nombre="Yuca", precio=1200)
cli = Cliente(nombre="JOHN", categoria="VIP")
cj = Caja(numero=20, tiene_peso=False)
cajero = Cajero(codigo="12", nombre="Miguel", salario=1000000)
v = Venta(fecha="2021-06-09", cliente=cli, cajero=cajero, caja=cj)
print("FECHA: ",v.fecha)
print("CLIENTE: ",v.cliente.nombre)
print("VENDIÓ: ",v.cajero.nombre)
print("EN LA CAJA: ",v.caja.numero)