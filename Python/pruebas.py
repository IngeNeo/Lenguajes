"""import random

class vector:
	def __init__(self, n):
		self.n = n
		self.V = [0] * (n+1)

#INICIE COMPLETANDO LA FUNCIÓN SOLUCIÓN

a = random.randint(15,30)
v = vector(a)

for i in range(1, a+1):
	v.V[i] = random.randint(1,9999)	
	v.V[0] += 1


def imprimeVector(vector, mensaje="vector sin nombre: \t"):
	print("\n", mensaje, end="        ")
	for i in range(1, vector.V[0] + 1):
		print(vector.V[i], end=", ")
		if i % 30 == 0:
			print("\n                      ", end="")
	print()

imprimeVector(a, 'Original')"""

"""V = [8, 3, 1, 6, 2, 7, 4, 9, 5]
for i in range(8, 1, -1):
	V[i] = V[(i-1)%8]
for i in range(1, 9):
	print(V[i], sep=",", end=" ")"""

"""x = int(input("entre un número "))
y = int(input("entre otro número "))

z = x % y
print(x, y, end=":", sep=",")
xx = x
yy = y

while z != 0:
	xx = yy
	yy = z
	z = xx % yy
	bb = x * y // yy

print(yy, bb, sep=",")"""