""" Elabore programa en Python que le permita al usuario ingresar números enteros de manera indefinida, 
	hasta que ingrese un número negativo, y al final imprimir la suma de los números enteros pares sin 
	incluir el número negativo en la suma."""
numero = int(input("Digite un numero entero: "))
suma = 0
while numero >= 0:
	if(numero%2) == 0:
		suma += numero
	numero = int(input("Digite otro numero entero: "))
print("La suma de los numeros pares es:", suma)