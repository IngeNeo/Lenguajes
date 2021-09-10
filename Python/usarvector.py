from claseVector import vector 
import random

n = int(input("Entre tamaño del vector: "))  
vec = vector(n)
vec.V[0] = n // 2

for i in range(1, n // 2 + 1):
	vec.V[i] = random.randint(1, 100) 

vec.imprimeVector("Vector de prueba") 

mayda = vec.mayor()
menda = vec.menor()

print("El mayor dato está en la posición ", mayda, "y es",  
vec.V[mayda])

print("El menor dato está en la posición ", menda, "y es", 
vec.V[menda])
vec.burbuja()
vec.imprimeVector("Vector de prueba ordenado")