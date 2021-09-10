import json
import os

ruta = os.path.split(__file__)
ruta = ruta[0] + os.sep + "grupo_udea_python.json"

datos_grupo_alumnos = {
    "docente":
      {
          "nombre": "john Arrieta",
          "rol"   : "Formador",
          "email" : "johncarlosarrietaarrieta@gmail.com"
      },
    "alumnos": ["Juan", "maria", "jose", "pedo"],
    "numero" :  7
}

print("Guardando datos en un archivo")

with open(ruta,"w") as archivo:
    json.dump(datos_grupo_alumnos, archivo, indent=2 )






