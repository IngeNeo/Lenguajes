import random

n = int(input("entre tamaño del vector: "))
vec = [0]*(n+1)
m = len(vec)

for i  in range(1, m):
	vec[i] = random.randint(1, 100)

for i in range(1, m):
	print(vec[i])