import time as t

def sumar( ):
	print("Sumando...")
	n1 = float(input("Digite un numero: "))
	n2 = float(input("Digite un numero: "))
	r = n1 + n2
	print("resultado:",r)

def restar(n1, n2):
	print("Restando...")
	r = n1 - n2
	print("Resultado original:",r)
	print("Resultado redondeado:",round(r, 3))

def multiplicar( ):
	print("Multiplicando...")
	n1 = float(input("Digite un numero: "))
	n2 = float(input("Digite un numero: "))
	r = n1 * n2
	return r

def dividir(dividendo, divisor):
	print("Dividiendo...")
	if divisor == 0:
		return "Jodaa, Brutoo, vez para primaria"
	else:
		return dividendo / divisor

def mostrar_lentamente(mensaje, velocidad):
	print("*****************")
	for i in range(len(mensaje)): # SUMAR
		print(mensaje[i], end="")
		t.sleep(velocidad)
	print("")    
	print("*****************")
	print("")

num1 = float(input("Digite un numero:"))
while True:
	num2 = float(input("Digite otro numero: "))
	if num2 == 0:
		print("El segundo numero deber ser diferente de 0")
	else:
		break

mostrar_lentamente("RESTAR", 0.3)
restar(num1, num2)
mostrar_lentamente("SUMAR", 0.5)
sumar()

res = None

mostrar_lentamente("MULTIPLICAR", 0.8)
res = multiplicar()
print("Resultado:",res)

mostrar_lentamente("DIVIDIR", 1.1)
res = dividir(num1, num2)
print("Resultado:",res)