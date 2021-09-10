#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
#from pruebas import pruebas_codigo_estudiante
import csv
import os
"""NOTAS:
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""

"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)

"""Fin espacio para programar funciones propias"""

def solucion():
	#ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.

	ruta = os.path.abspath(__file__)
	partes = os.path.split(ruta)
	ruta = partes[0] + os.sep + "FB.csv"

	encabezado = ["Fecha", "Mean-Min-Max", "Concepto"]
	ruta1 = partes[0] + os.sep + "analisis_archivo.csv"
	with open(ruta1, "w", newline = "") as analisis:
		escribir = csv.writer(analisis, delimiter = "\t")
		escribir.writerow(encabezado)
		analisis.close
	with open(ruta, "r") as file:
		leer = csv.reader(file, delimiter = ",")
		next(leer, None)
		date_lowest_mean = ""
		date_highest_mean = ""
		lowest_mean = 1000.0
		highest_mean = 0.0
		lista = []

		for fila in leer:
			fecha = fila[0]
			precio_aper = float(fila[1])
			precio_hign = float(fila[2])
			precio_low = float(fila[3])
			precio_close = float(fila[4])
			precio_ajust = float(fila[5])

			promedio = ((precio_hign + precio_low) / 2)

			if promedio < 239:
				concepto = "MUY BAJO"
				if promedio < lowest_mean:
					date_lowest_mean = fila[0]
					lowest_mean = promedio
			elif promedio >= 239 and promedio < 265:
				concepto = "BAJO"
				if promedio < lowest_mean:
					date_lowest_mean = fila[0]
					lowest_mean = promedio
			elif promedio >= 265 and promedio < 291:
				concepto = "MEDIO"
			elif promedio >= 291 and promedio < 317:
				concepto = "ALTO"
				if promedio > highest_mean:
					date_highest_mean = fila[0]
					highest_mean = promedio
			elif promedio >= 317:
				concepto = "MUY ALTO"
				if promedio > highest_mean:
					date_highest_mean = fila[0]
					highest_mean = promedio
			lista = [fila[0], promedio, concepto]
			with open(ruta1, "a", newline = "") as analisis:
				escribir = csv.writer(analisis, delimiter = "\t")
				escribir.writerow(lista)
	return date_lowest_mean, lowest_mean, date_highest_mean, highest_mean

prueba = solucion()
"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(solucion)