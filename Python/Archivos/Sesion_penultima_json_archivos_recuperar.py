import json
import os

ruta = os.path.split(__file__)
ruta = ruta[0] + os.sep + "grupo_udea_python.json"

archivo_json = open(ruta) 
diccionario = json.load(archivo_json)
docente = diccionario["docente"]
print(docente["nombre"])
print(docente["email"])