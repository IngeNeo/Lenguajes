#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""

#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES

"""Fin espacio para programar funciones propias"""

def traductor_a_morse(mensaje_a_traducir):
	#PROGRAMA ACÁ TU SOLUCIÓN
	mensaje_traducido = ""
	dic_morse = {
		#Letra : Morse
		"A": ".-",
		"B": "-...",
		"C": "-.-.",
		"D": "-..",
		"E": ".",
		"F": "..-.",
		"G": "--.",
		"H": "....",
		"I": "..",
		"J": ".---",
		"K": "-.-",
		"L": ".-..",
		"M": "--",
		"N": "-.",
		"O": "---",
		"P": ".--.",
		"Q": "--.-",
		"R": ".-.",
		"S": "...",
		"T": "-",
		"U": "..-",
		"V": "...-",
		"W": ".--",
		"X": "-..-",
		"Y": "-.--",
		"Z": "--..",
		" ": "/"
	}
	for i in range(len(mensaje_a_traducir)):
		mensaje_a_traducir[i]
		mensaje_traducido = mensaje_traducido + " "+ dic_morse[mensaje_a_traducir[i]]
	return mensaje_traducido.lstrip()

mensaje1 = "NOS HAN PICADO DOS MOSQUITOS"
mensaje2 = "HEMOS ENCONTRADO UNA PLANTA NUNCA ANTES VISTA"
mensaje3 = "TENEMOS COMIDA PARA TRES DIAS MAS"

Esperado1 = "-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- ..- .. - --- ..."

Esperado2 = ".... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-"

Esperado3 = "- . -. . -- --- ... / -.-. --- -- .. -.. .- / .--. .- .-. .- / - .-. . ... / -.. .. .- ... / -- .- ..."

generado1 = traductor_a_morse(mensaje1)
print("Este es el mensaje", mensaje1)
print("Este es el esperado", Esperado1)
print("Este es el generado", generado1)
print()
generado2 = traductor_a_morse(mensaje2)
print("Este es el mensaje", mensaje2)
print("Este es el esperado", Esperado2)
print("Este es el generado", generado2)
print()
generado3 = traductor_a_morse(mensaje3)
print("Este es el mensaje", mensaje3)
print("Este es el esperado", Esperado3)
print("Este es el generado", generado3)
print()

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
#pruebas_codigo_estudiante(traductor_a_morse)