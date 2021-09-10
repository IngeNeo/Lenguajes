"""numero = float(input("Número que desea multiplicar:"))
while True:
	inicio = int(input("Número desde donde inicará la multiplicación menor a 10:"))
	if inicio > 10:
		print(inicio,"Debe ser inferior a 10")
		continue
	else:
		for i in range(inicio, 11):
			multiplo = numero * i
			print(i, "x", numero, "=", multiplo)
	break
print("Fin")"""
suma = 0
for i in range(50):
	suma += i
print("Total =",suma)