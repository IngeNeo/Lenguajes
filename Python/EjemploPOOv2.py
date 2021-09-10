# CLASE CON PROPIEDADES

# UN NUEVO TIPO DE DATO
class Persona:
# LAS PROPIEDADES DEBEN TENER VALOR INCIAL

	def __init__(self,  ced, nom, ape, em, tel, gen, dir):
		self.cedula = ced
		self.nombre = nom
		self.apellido = ape
		self.email = em
		self.telefono = tel
		self.genero = gen
		self.direccion = dir

	def copiar(self):
		copia = Persona( self.cedula,  self.nombre,  self.apellido,  self.email
						, self.telefono,  self.genero,  self.direccion)
		return copia

	def imprimir_personas():
		for p in l1:
			print("Nombre: ",p.nombre)
			print("Apellido: ",p.apellido)

"""
n = input("Ingrese el Nombre: ")
cc = input("Ingrese la Cedula: ")
ap = input("Ingrese el Apellido: ")
e = input("Ingrese el Email: ")
d = input("Ingrese la Direccion: ")
g = input("Ingrese el Genero: ")
t = input("Ingrese el Telefono: ")
"""

n = "Gustavo"
cc = "1234"
ap = "Petro"
e = "petro@comlombia.com"
d = "Bogota"
g = "Masculino"
t = "3017355444"

p1 = Persona(cc, n, ap, e, t, g, d)
p2 = Persona(cc, n, ap, e, t, g, d)

print(type(p1))
print(type(p2))

if p1 == p2:
	print("p1 es el mismo p2")
	print("P1 esta en: ",p1)
	print("P2 esta en: ",p2)
else:
	print("p1 NO es el mismo p2")
	print("P1 esta en: ",p1)
	print("P2 esta en: ",p2)

p1.email = "prosky@colombia.com"
print("p1.email: ",p1.email)
print("p2.email: ",p2.email)


p3 = p1
if p1 == p3:
	print("p1 es el mismo p3")
	print("P1 esta en: ",p1)
	print("P3 esta en: ",p3)
else:
	print("p1 NO es el mismo p3")
	print("P1 esta en: ",p1)
	print("P3 esta en: ",p3)

p4 = p1.copiar()

if p1 == p4:
	print("p1 es el mismo p4")
	print("P1 esta en: ",p1)
	print("P4 esta en: ",p4)
else:
	print("p1 NO es el mismo p4")
	print("P1 esta en: ",p1)
	print("P4 esta en: ",p4)

print("p1.email: ",p1.email)
print("p3.email: ",p3.email)
p3.email = "eljefe@decolombia.com"
print("p1.email: ",p1.email)
print("p3.email: ",p3.email)
print("p1.nombre: ",p1.nombre)
p3.nombre = "El duque"
print("p1.nombre: ",p1.nombre)
p4.nombre ="Claudia"
print("p1.nombre: ",p1.nombre)
print("p2.nombre: ",p2.nombre)
print("p3.nombre: ",p3.nombre)
print("p4.nombre: ",p4.nombre)

l1 = []
l1.append(p1)
l1.append(p2)
l1.append(p3)
l1.append(p4)