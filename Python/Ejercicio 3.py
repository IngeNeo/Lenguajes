""" Elabore un programa en Python que lea una longitud en metros y la convierta y escriba en centímetros, pies y pulgadas."""

longitud = float(input("Digite el valor en metros que desea convertir "))
centimetros = longitud / 0.010000
pies = longitud * 3.2808
pulgadas = longitud * 39.370

print(longitud, "metros equivale a:", centimetros,"centimetros, a", pies, "pies", "y a", pulgadas, "pulgadas")