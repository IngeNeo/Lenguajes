""" Elabore un programa en Python que lea una temperatura en grados Celsius, la convierta a grados Fahrenheit y muestre el resultado con un mensaje bien explicativo.
No use aproximaciones """
gradoC = float(input("Ingrese los grados Celsius a convertir: "))
gradoF = (1.8 * gradoC) + 32

print(gradoC, "grados Celsius equivalen a", gradoF, "grados Fahrenheit")