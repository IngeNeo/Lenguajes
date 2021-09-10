import numpy as np
#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""
#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES

"""Fin espacio para programar funciones propias"""

def solucion(A):
	"""
	En esta función deberás programar tu solución.
	Explicación del parámetro que recibe:
	- A: Es una matriz cuadrada de números enteros aleatoria (NO TE DEBES PREOCUPAR POR LLENARLA, YA LO ESTÁ),
		para indexar un elemento en la fila i, columna j se hace así:
		A[i,j] o A[i][j], como te sientas más cómod@.
		El orden de la matriz lo puedes calcular así: n = A.shape[0]


	Explicación de lo que debe retornar:
	-sum_diagonal_principal: Suma de los elementos de la diagonal principal, es de tipo float o entero (Elige el tipo que quieras).
	-prod_diagonal_secundaria: Producto de los elementos de la diagonal secundaria, es de tipo float o entero (Elige el tipo que quieras)
	-resultado2_mod_resultado1:  Módulo entre prod_diagonal_secundaria y sum_diagonal_principal, es de tipo float o entero (Elige el tipo que quieras)
	"""
	suma_principal = 0
	producto_secundario = 1
	#Recorremos la matriz para saber los valores de la diagonal principal y sumarlos
	for x in range (len(A)):
		suma_principal = suma_principal + A[x][x]
	# generamos la variable de la suma y le asignamos el valor resultante del recorrido
	sum_diagonal_principal = suma_principal
	#Recorremos la matriz para saber los valores de la diagonal secundaria y multiplicarlos
	for i in range (len(A)):
		for j in range (len(A)):
			# Hacemos una condicion si la suma de los indices es igual al tamaño de la matriz - 1, recordar que comienza en 1 con la funcion len, por eso se sustrae 1
			if ((i + j) == (len(A) - 1)):
				producto_secundario = producto_secundario * A[j][i]
	# Generamos la variable del producto y le asignamos el valor resultante del recorrido
	prod_diagonal_secundaria = producto_secundario
	# Realizamos el modulo entre el resultado de prod_diagonal_secundaria y sum_diagonal_principal
	resultado2_mod_resultado1 = prod_diagonal_secundaria % sum_diagonal_principal
	# Retorna los valores de las operaciones
	return sum_diagonal_principal, prod_diagonal_secundaria, resultado2_mod_resultado1

"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
#NO MODIFICAR
matriz_entrada =  np.array([[73, 13,  6,  1, 29],
							[28, 72, 76, 86, 48],
							[94, 18, 32, 24, 33],
							[63, 11, 16, 69, 40],
							[38, 20, 45, 78, 61]])
dp_correcto = 307
ds_correcto = 33359744
ds_mod_dp_correcto = 203

dp_estudiante = solucion(matriz_entrada)[0]
ds_estudiante = solucion(matriz_entrada)[1]
ds_mod_dp_estudiante = solucion(matriz_entrada)[2]

print("MATRIZ ENTREGADA:\n", matriz_entrada,"\n")
print(f"""===SALIDA ESPERADA===
		Suma de los elementos de la diagonal principal = {dp_correcto}
		Producto de los elementos de la diagonal secundaria = {ds_correcto}
		{ds_correcto} mod {dp_correcto} = {ds_mod_dp_correcto}""")

print(f"""===TU SALIDA===
		Suma de los elementos de la diagonal principal = {dp_estudiante}
		Producto de los elementos de la diagonal secundaria = {ds_estudiante}
		{ds_estudiante} mod {dp_estudiante} = {ds_mod_dp_estudiante}\n""")

if dp_correcto == dp_estudiante and ds_correcto == ds_estudiante and ds_mod_dp_correcto == ds_mod_dp_estudiante:
	print("Todo se ve correcto, ¡Procede a calificar tu código!")
else:
	print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")