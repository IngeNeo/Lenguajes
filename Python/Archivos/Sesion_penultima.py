import json

edad = 10
estatura = 1.72
exito = True
nombre = "John Arrieta"
nada = None
lista = [25, 15, 43, 47]
tupla_nombre = ("JOHN", "CARLOS","ADRIAN", "JULIAN")
diccionario = {'Nombre':"john", "Edad": 43, "Genero": 'Masculino'}
print("Dic de Python")
print(diccionario)
print()
print("De Dict de Python a JSon sin formato")
json_dato = json.dumps(diccionario)
print(json_dato)
print()
print("De Dict de Python a JSon con formato" )
json_dato = json.dumps(diccionario, indent=4)
print(json_dato)
print(type(diccionario))
print(type(json_dato))

class Alumno:
    nombre = "JOHN"

a = Alumno()
"""
# LA SIGUIENTES INSTRUCCION GENERA UNA EXCEPCION
json_dato = json.dumps(a)
print(json_dato)
"""

