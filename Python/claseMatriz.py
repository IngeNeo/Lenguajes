import random
import Vectores as vector

class matriz:

	def __init__(self, m, n):
		self.m = m
		self.n = n
		self.mat = [] * (m + 1)
		for i in range(m + 1):
			a = [0] * (n + 1)
			self.mat.append(a)

#Crea la matriz y la llena con datos aleatorios
	def construyeMatriz(self, r = 100):
		for i in range(1, self.m + 1):
			for j in range(1, self.n +1):
				self.mat[i][j] = random.randint(1, r)

#Imprime la matriz por filas
	def imprimeMatrizPorFilas(self, mensaje="Matriz sin nombre "):
		print("\n", mensaje)
		for i in range(1, self.m + 1):
			for j in range(1, self.n + 1):
				print(self.mat[i][j], "\t", end="")
			print()

#Imprime la matriz por columnas
	def imprimeMatrizPorColumnas(self, mensaje="Matriz sin nombre "):
		print("\n", mensaje)
		for i in range(1, self.n + 1):
			for j in range(1, self.m + 1):
				print(self.mat[j][i], "\t", end="")
			print()

# Sumar filas de una matriz
	def sumarFilas(self):
		v = vector(self.m)
		for i in range(1, self.m + 1):
			s = 0
			for j in range(1, self.n + 1):
				s = s + self.mat[i][j]
				v.agregarDato(s)
		return v

# Sumar columnas de una matriz
	def sumarColumnas(self):
		v = vector(self.n)
		for i in range(1, self.n + 1):
			s = 0
			for j in range(1, self.m + 1):
				s = s + self.mat[j][i]
				v.agregarDato(s)
		return v

# Intercambiar filas de una matriz
	def intercambiarFilas(self, i, j):
		for k in range(1, self.n):
			aux = self.mat[i][k]
			self.mat[i][k] = self.mat[j][k]
			self.mat[j][k] = aux

# Intercambiar columnas de una matriz
	def intercambiarColumnas(self, i, j):
		for k in range(1, self.m):
			aux = self.mat[k][i]
			self.mat[k][j] = self.mat[k][i]
			self.mat[k][i] = aux

# Hacer la traspuesta de una matriz
	def traspuesta(self):
		c = matriz(self.n, self.m)
		for i in range(1, self.m + 1):
			for j in range(1, b.n + 1):
				c.mat[j][i] = self.mat[i][j]
		return c

# Multiplicar martices
	def __mul__(self, b):
		c = matriz(self.m, b.n)
		for i in range(1, self.m + 1):
			for j in range(1, b.n + 1):
				c.mat[i][j] = 0
				for k in range(1, self.n + 1):
					c.mat[i][j] = c.mat[i][j] + self.mat[i][k] * b.mat[k][j]
		return c