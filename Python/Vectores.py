import math

class vector:
	def __init__(self, n):
		self.n = n
		self.V = [0] * (n+1)

	# Generar datos aleatorios para el vector
	def construyeVector(V, n):
		V[0] = n
		for i in range(1, n + 1):
			V[i] = math.random.randint(1, 99)
	
	# Función para mostrar los datos del vector
	def imprimeVector(V, mensaje = "Vector sin nombre"):
		print("\n", mensaje, end=" ")
		m = V[0] + 1
		for i in range(1, m):
			print(V[i], end = ", ")
	
	#Función para validar si el Vector esta Vacio
	def esVacio(V):
		if V[0] == 0:
			return True
		return False
	
	#Función para validar si el Vector esta Vacio
	def esLleno(V, n):
		if V[0] == n:
			return True
		return False
	
	#Función para Sumar los datos de un Vector
	def sumaVector(V):
		n = V[0] + 1
		s = 0
		for i in range(1, n):
			s = s + V[i]
		return s
	
	#Función para Agregar datos a un Vector en ultima posición
	def agregarDato(d, V, n):
		if esLleno(V, n):
			return
		V[0] = V[0] + 1
		V[V[0]] = d
	
	#Función para Agregar datos a un Vector
	def insertarDato(d, i, V, n):
		if esLleno(V, n):
			return
		for j in range(V[0], i - 1, -1):
			V[j + 1] = V[j]
		V[i] = d
		V[0] = V[0] + 1
	
	#Función para definir el dato mayor de un Vector
	def mayorDato(V):
		mayor = 1
		for i in range(2, V[0] + 1):
			if V[i] > V[mayor]:
				mayor = i
		return mayor
	
	#Función para definir el dato menor de un Vector
	def menorDato(V):
		menor = 1
		for i in range(2, V[0] + 1):
			if V[i] < V[menor]:
				menor = i
		return menor
	
	#Función para intercambiar datos en un Vector
	def intercambiar(V, i, j):
		aux = V[i]
		V[i] = V[j]
		V[j] = aux
	
	#Función para Buscar donde insertar datos en un Vector
	def buscarDondeInsertar(V, d):
		k = 1
		while k <= V[0]  and  V[k] < d:
			k = k + 1
		return k
	
	#Función para insertar en la posición donde corresponde el valor el un Vector
	def insertar(V, d, k):
		for i  in range(V[0], k - 1,  -1  ):
			V[i+1] = V[i]
		V[k] = d
		V[0] = V[0] + 1
	
	#Función para buscar dato a borrar en un Vector
	def buscarDato(V, d):
		i = 1
		while i <= V[0]  and  V[i] != d:
			i = i + 1
		if i <= V[0]:
			return i
		return -1
	
	#Función para borrar dato en un Vector
	def borrar(V, i):
		for j  in  range(i, V[0]):
			V[j] = V[j + 1]
		V[0] = V[0] - 1
	
	#Función para ordenar ascendentemente datos en un Vector
	def ordenaAscen(V):
		for i in range(1, V[0]):
			k = i
			for j in range(i+1, V[0] + 1):
				if V[j] < V[k]:
					k = j
					intercambiar(V, i, k)
	
	#Función metodo burbuja
	def ordenaAscen(V):
		for i in range(1, V[0]):
			for j in range(1, V[0] - i + 1):
				if V[j] > V[j + 1]:
					intercambiar(V, j, j + 1)
	
	# Busqueda binaria
	def busbin(V, d): 
		inicio = 1
		fin = V[0]
		while inicio < fin:
			mitad = (inicio + fin) // 2
			if V[mitad] == d:
				return mitad
			if d < V[mitad]:
				fin = mitad - 1
			else:
				inicio = mitad + 1
		return -1
	
	#Función ordenado por selección
	def selección(V):
		for i  in  range(1, V[0]):
			k = i
			for j  in range(i+1, V[0] + 1):
				if V[j] < V[k]:
					k = j
			intercambiar(i, k)
	
	#Función ordenado burbuja
	def burbuja(V):
		for i  in range(1, V[0]):
			for j  in range(1, V[0] - i + 1):
				if V[j]  >  V[j+1]:
					intercambiar(V, j, j+1)
	
	#Función ordenado por inserción
	def insercion(V):
		for i in range(2, V[0]+1):
			d = V[i]
			j = i - 1
			while j > 0  and  V[j] > d:
				V[j+1] = V[j]
				j = j - 1
			V[j+1] = d
	
	
	#n = int(input("Entre tamaño del vector "))
	#V = [0] * (n + 1)