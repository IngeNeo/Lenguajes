# crear un tupla vacia
t1 = ()
print(t1)
print("Elementos:", len(t1))

# otra forma de crear una tupla vacia
t2 = tuple()
print(t2)
print("Elementos:", len(t2))
t3 = (
		212124 				# 0: cedula
		, "john arrieta"	# 1: nombre
		, 43				# 2: edad
		, 93.2				# 3: peso
		, False				# 4: sabe leer
		)

print(t3)
print("Elementos:", len(t3))

t4 = tuple(("ing","esp","mag", "Phd"))
print(t4)
print("Elementos:", len(t4))
print("t1:",type(t1))
print("t2:",type(t2))
print("t3:",type(t3))
print("t4:",type(t4))

t5 = (17,)
print("t5:",type(t5))
print(t5)
print("Elementos:", len(t5))

## --- CREAR UNA LISTA DE VARIAS FORMAS ---
L1 = []
print(L1)
print("L1:",type(L1))
print("Elementos:", len(L1))

L2 = list()
print(L2)
print("L2:",type(L2))
print("Elementos:", len(L2))

L3 = [1234, "John Arrieta"]
print(L3)
print("L3:",type(L3))
print("Elementos:", len(L3))

L4 = [1234,]
print(L4)
print("L4:",type(L4))
print("Elementos:", len(L4))

L5 = list([2.5, 4.1, 1.5])
print(L5)
print("L4:",type(L5))
print("Elementos:", len(L5))

## --- CREAR UNA DICCIONARIO DE VARIAS FORMAS ---
d1 = {}
print(d1)
print("d1:",type(d1))
print("Elementos:", len(d1))

d2 = dict()
print(d2)
print("d2:",type(d2))
print("Elementos:", len(d2))

d3 = {"nombre":"JOHN"}
print(d3)
print("d3:",type(d3))
print("Elementos:", len(d3))

d4 = {
		"placa": "abc-123"
		, "modelo": 2012
		, "color": "plata"
		, "cc": 1.599
		}

print(d4)
print("d4:",type(d4))
print("Elementos:", len(d4))

## --- CREAR UNA CONJUNTOS DE VARIAS FORMAS ---
c1 = set()
print(c1)
print("c1:",type(c1))
print("Elementos:", len(c1))

## -- agregar elementos a una lista
print(L3)
L3.append("jarrieta@gmail.com")
print(L3)
L3.append(5)
print(L3)
L3.append(5)
print(L3)
print("---------")
c1.add(10)
print(c1)
c1.add(-2)
print(c1)
c1.add("Hola")
print(c1)
c1.add(10)
print(c1)

## -- recorrer cada elemento de una lista
print(t3[3])
print(L3[1])
print(d4["modelo"])

suma = 0
for i in t3:
	print(i,end=",")
	try:
		suma += float(i) 
	except ValueError:
		continue

print("---------------")
print("")
print("Suma:", suma)
print("---------------")

for i in range(len(L3)):
	print(i,":",L3[i])
print("---------------")

for i in L3:
	print(i)
print("---------------")

for i in c1:
	print(i)
print("---------------")

for clave, dato in d4.items():
	print(clave,":",dato)

print(L3[1:3])