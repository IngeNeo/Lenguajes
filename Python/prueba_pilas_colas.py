from colecciones_de_datos import *


## probando la Cola
una_cola = Cola()
print(una_cola)
una_cola.entrar_a_la_cola("John")
una_cola.entrar_a_la_cola("JUAN")
una_cola.entrar_a_la_cola("PEDRO")
una_cola.entrar_a_la_cola("JOSE")
una_cola.entrar_a_la_cola("JESUS")
una_cola.entrar_a_la_cola("MARIA")
una_cola.entrar_a_la_cola("ANDRES")
try:
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
	item =  una_cola.salir_de_la_cola()
	print(item,"eliminado de la cola")
	print(una_cola)
except ColeccionVaciaError as msj:
	print(msj)

p = Pila()
print(p)
try:
	p.colcar_en_la_cima("libro1")
	p.colcar_en_la_cima("libro2")
	p.colcar_en_la_cima("libro3")
	p.colcar_en_la_cima("libro4")
	print(p)
	p.quitar_de_la_cima()
	print(p)
	p.quitar_de_la_cima()
	print(p)
	p.quitar_de_la_cima()
	print(p)
	p.quitar_de_la_cima()
	print(p)
	p.quitar_de_la_cima()
	print(p)
except Exception as er:
	print(er)