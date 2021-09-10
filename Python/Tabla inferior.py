numero = float(input("Número que desea multiplicar:"))
inicio = int(input("Número desde donde inicará la multiplicación:"))

if inicio > 10:
	print("El inicio debe ser inferior a 10")
else:
	for i in range(inicio, 11):
		multiplo = numero * i
		print(i, "x", numero, "=", multiplo)
print("Fin")