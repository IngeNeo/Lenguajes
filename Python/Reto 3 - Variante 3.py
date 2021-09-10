#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""

#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES

"""Fin espacio para programar funciones propias"""

def calculadora(bits1, bits2, OP):

	#PROGRAMA ACÁ LA SOLUCIÓN
	resultado = ""
	for i in range (len(bits1)):
		if OP == "OR":
			if (bits1[i] == "0") and (bits2[i] == "0"):
				resultado = resultado + "0"
			else:
				resultado = resultado + "1"
		if OP == "AND":
			if (bits1[i] == "1") and (bits2[i] == "1"):
				resultado = resultado + "1"
			else:
				resultado = resultado + "0"
		if OP == "XOR":
			if (bits1[i] == "1") and (bits2[i] == "1"):
				resultado = resultado + "0"
			elif (bits1[i] == "0") and (bits2[i] == "0"):
				resultado = resultado + "0"
			else:
				resultado = resultado + "1"
	return resultado

bits1 = "0110110110"
bits2 = "1100011101"
OP = "AND"

prueba = calculadora(bits1, bits2, OP)
print(prueba)
"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
#pruebas_codigo_estudiante(calculadora)