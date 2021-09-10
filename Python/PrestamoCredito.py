# DATOS DE ENTRADA
print("Nombre: ")
nombre = input()  
telefono = input("Telefono: ") 
print("Valor a prestar: $", end="")
monto = input() 
monto = int(monto)
cuotas = int(input("Numero de cuotas por mes: ")) 
interes = float(input("Interés (0.01 - 1): ")) 
# PROCESO
cuota_base = monto / cuotas
ganancia_mes = cuota_base * interes
cuota_total = cuota_base + ganancia_mes
ganacia_total = ganancia_mes * cuotas
credito_total = monto + ganacia_total
# SALIDA
print("** PARATE FIRME **")
print("*******************")
print("Usted ",nombre, " me debe $",monto)
print("Tus datos de contacto son: ", telefono)
print("=======================================")
print("")
print("Numero de cuotas: ",cuotas)
print("Cuota base: $",cuota_base)
print("INTERES: $",interes)
print("GANANCIA POR MES: $",ganancia_mes)
print("PAGO MENSUAL: $",cuota_total)
print("------------------------------------")
print("TOTAL PRESTAMOS: $",credito_total )
print("------------------------------------")
print("OJO Y NO ME PAGAS")