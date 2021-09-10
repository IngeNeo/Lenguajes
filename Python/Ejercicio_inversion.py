capital = float(input("Ingrese la inversión: $"))
interes = float(input("Ingrese la interés: $"))

# Proceso
ganancia = capital * interes

if ganancia > 7000:
	total = capital + ganancia
	print("Total inversión es: $", total)
else:
	print("No inviertas")
