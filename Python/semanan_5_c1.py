"""
python
NO SOPORTA ARREGLOS NI MATRICES
LISTAS
-- ARREGLOS DINAMICO 
-- LISTA
-- PILA
-- COLA
-- MATRIZ
"""

def tamaño(arreglo):
	cuenta = 0
	for i in arreglo:
		cuenta += 1
	return cuenta


def tamaño_matriz(matriz):
	cuenta_fila = tamaño(matriz)
	cuenta_columna = tamaño(matriz[0])
	return (cuenta_fila, cuenta_columna)

def sumar_elementos(arreglo):   
	suma = 0
	for i in arreglo:
		suma += i
	return suma

def sumar_elementos_matriz(matriz):
	suma = 0
	for i in matriz:
		for j in i:
			suma += j
	return suma

def sumar_2_arreglos(arreglo1, arreglo2):
	arreglo_resultado = []
	if tamaño(arreglo1) == tamaño(arreglo2):
		arreglo_resultado = []
		for i in range(tamaño(arreglo1)):
			suma = arreglo1[i] + arreglo2[i]
			arreglo_resultado.append(suma)      
	return arreglo_resultado


a1 = [1, 20, 3, 50, -11]
a2 = [57, 0, 100, 1, 9]
print(a1)
print("-----")
print("Tamaño del arreglo a1 usando len: ",len(a1))
print("-----")
print("Tamaño del arreglo a1 usando tamaño: ",tamaño(a1))
print("-----")

m1 = [
	[1, 20, 3, 50, -11]
	,[57, 0, 100, 88, 90]
	]

m2 = [
	[15, 6, 21, 3, 166]
	,[57, 0, 100, 88, 90]
	,[5, 77, 19, 8, 200]
	,[88, 12, 11, 22, 44]
	]


print(m1)
print("-----")
tamaño_matriz(m1)
print("")
print("-----")
print("Tamaño de la Matriz m1 usando len: Filas=", len(m1), "Colum=",len(m1[0]))
print("-----")
dimension = tamaño_matriz(m1)
print("-----")
print("Tamaño de la Matriz m1 usando tamaño_matriz: Filas=", dimension[0], "Colum=", dimension[1])
print("-----")
print("LA SUMA DEL CONTENIDO DE a1: ", sumar_elementos(a1))
print("-----")
print("LA SUMA DEL CONTENIDO DE a2: ", sumar_elementos(a2))
print("-----")
print("LA SUMA DEL CONTENIDO DE m1: ", sumar_elementos_matriz(m1))
print("-----")
print("LA SUMA DEL CONTENIDO DE m2: ", sumar_elementos_matriz(m2))
print("-----")
resultado = sumar_2_arreglos(a1, a2)
print("LA SUMA ARREGLO a1 + a2 es:", resultado)
print("-----")