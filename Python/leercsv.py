import csv
import os
# obtener la ruta del programa
ruta = os.path.abspath(__file__)
partes = os.path.split(ruta)
ruta = partes[0]+ os.sep + "FB.csv"
# archivo-entrada.py
#f = open (FB.csv','r')
#mensaje = f.read()
#print(mensaje)
#f.close()
#f = open(ruta, "r")
#while(True):
#    linea = f.readline() # EOF
#    print(linea)
archivo = open(ruta, "r")
datos =[]
for linea in archivo:
	datos = linea.split(",")
	print(datos[0]+"\t" +datos[1]+"\t"+datos[2]+"\t" +datos[3]+"\t" +datos[4]+"\t" +datos[5]+"\t" +datos[6])

#with open(ruta) as archivo:
#    reader = csv.reader(archivo, delimiter=",")
#    for row in reader:
#        print()
"	"