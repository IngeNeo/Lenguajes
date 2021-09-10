import random

#Creamos la matriz directamente ingersando los campos de los parametros directamente
mat = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

#Nos regresa el valor de las "Filas" del vector
m = len(mat)

#Lo usaremos para que nos regrese el valor o longitud de lo que existe
# en cada uno de las filas estas seran las "Columnas"
n = len(mat[0])
print("El tamaño de la matriz es:",m,"filas por", n,"columnas")

# Imprimiendo la matriz creada
for i in range(0,m):
	for j in range(0,n):
		print(mat[i][j], end = ", ")
	print()

#Solicitamos los datos para crar la matriz, las filas y las columnas
m = int(input("\nEntre número de filas de la matriz: "))
n = int(input("\nEntre número de columnas de la matriz: "))

#Creamos un vector con las dimensines de m se suma 1 para no usar el campo 0 para dejarlo para otros fines
mat1 = [] * (m+1)

#Creamos un vector con los datos de la columnas y lo adicionamos al vector creado para qeu sean las filas
for i  in range(m+1):
	a = [0]*(n+1)
	mat1.append(a)

# Llenamos la matriz con numeros aleatorios
for i   in range(1, m + 1):
	for j  in range(1, n + 1):
		mat1[i][j] = random.randint(0, 9)

# Imprimiendo sin la fila 0 y la columna 0
for i in range(1,m+1):
	for j in range(1,n+1):
		print(mat1[i][j], end = ", ")
	print()
print()

# Imprimiendo la fila 0 y la columna 0
for i in range(0,m+1):
	for j in range(0,n+1):
		print(mat1[i][j], end = ", ")
	print()
print()