import random
import time
import os

no1 = random.randint(0, 9)
no2 = random.randint(0, 9)
no3 = random.randint(0, 9)
n1 = None
n2 = None
n3 = None

while no1 == n2:
	no2 = random.randint(0, 9)

while no2 == n3:
	no3 = random.randint(0, 9)

while no1 == n3:
	no3 = random.randint(0, 9)

for i in range(1, 4):
	while True:
		n1, n2, n3 = input("Tres numeros entre 0 a 9 separados por espacio: ").split()
		n1 = int(n1)
		n2 = int(n2)
		n3 = int(n3)
		if n1 < 0 or n1 > 9:
			print("El primero numero no cumple la regla (0 -9)")
			continue
		if n2 < 0 or n2 > 9:
			print("El segundo numero no cumple la regla (0 -9)")
			continue
		if n3 < 0 or n3 > 9:
			print("El tercer numero no cumple la regla (0 -9)")
			continue
		break
	print(no1, no2, no3)

	pista = ""
	if n1 != no1 and n1 != no2 and n1 != no3:
		pista += "R"
	elif n1 == no1:
		pista += "V"
	elif n1 == no2 or n1 == no3:
		pista += "A"

	if n2 != no1 and n2 != no2 and n2 != no3:
		pista += " R"
	elif n2 == no2:
		pista += " V"
	elif n2 == no1 or n2 == no3:
		pista += " A"

	if n3 != no1 and n3 != no2 and n3 != no3:
		pista += " R"
	elif n2 == no2:
		pista += " V"
	elif n3 == no1 or n3 == no2:
		pista += " A"

	print(pista)
	if pista == "V V V":
		print(no1, no2, no3)
		print("Ganaste")
		break
else:
	print(no1, no2, no3)
	print("Perdiste")