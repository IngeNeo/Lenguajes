#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante
"""NOTAS:
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""

"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL

"""Fin espacio para programar funciones propias"""

def actualizar_estado_editor(operaciones_usuario):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.

    cadena_final = ""
    texto_actual = ""
    texto_escrito = []
    action_rehacer = []

    for x in range(len(operaciones_usuario)):
        if((operaciones_usuario[x] != "REHACER") and (operaciones_usuario[x] != "DESHACER")):
            if texto_actual != "":
                texto_escrito.append(texto_actual)
                texto_actual = operaciones_usuario[x]
            else:
                texto_actual = operaciones_usuario[x]
        elif operaciones_usuario[x] == "REHACER":
            texto_escrito.append(texto_actual)
            texto_actual = action_rehacer.pop()
        elif operaciones_usuario[x] == "DESHACER":
            action_rehacer.append(texto_actual)
            texto_actual = texto_escrito.pop()

    for i in range(len(texto_escrito)):
        cadena_final += texto_escrito[i]
    cadena_final += texto_actual
    return cadena_final

lista = ["Definamos qué es una función de Python:","Una función es","un arreglo unidimensional de datos", "DESHACER", "DESHACER", "REHACER", "un grupo de instrucciones"]
cadena_esperada = "Definamos qué es una función de Python:Una función esun grupo de instrucciones"
print("La cadena esperada es: ", cadena_esperada)
final = actualizar_estado_editor(lista)
print ("La cadena generada es: ",final)
"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(actualizar_estado_editor)