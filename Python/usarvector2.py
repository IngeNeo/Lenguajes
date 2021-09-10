from claseVector import vector  
import random

n = int(input("Entre tamaño del vector: "))
vec = vector(n)
vec.V[0] = n // 2

for i in range(1, n // 2 + 1):
	vec.V[i] = random.randint(1, 100)

vec.imprimeVector("Vector de prueba creado")
vec.agregarDato(13)
vec.imprimeVector("Vector con dato agregado")
vec.burbuja()
vec.imprimeVector("Vector ordenado ascendentemente")
i =vec.buscarDondeInsertar(39)
vec.insertar(39, i)
vec.imprimeVector("Vector con dato 39 insertado") 
vec.insertar(44)
vec.imprimeVector("Vector con dato 44 insertado")