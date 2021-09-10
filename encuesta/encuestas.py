from Database import *
import numpy as np
import matplotlib.pyplot as plt

database = Database()
#database.select_encuesta(26)
database.select_all_encuesta()
#database.promedio("Cabecera", "servicio")
#R = database.promedio("Cabecera_servicio", "suma_cabecera")
print("************************************")
sucursar = "Cabecera"
S_Cabe = round(database.promedio_servico(sucursar), 2)
P_Cabe = round(database.promedio_puntualidad(sucursar), 2)
I_Cabe = round(database.promedio_instalaciones(sucursar), 2)
T_Cabe = round(database.promedio_tratamiento(sucursar), 2)
B_Cabe = round(database.promedio_bioseguridad(sucursar), 2)
print(f"El promedio de servicio en:", {sucursar}, "es:", S_Cabe)
print(f"El promedio de puntualidad en:", {sucursar}, "es:", P_Cabe)
print(f"El promedio de instalaciones en:", {sucursar}, "es:", I_Cabe)
print(f"El promedio de tratamiento en:", {sucursar}, "es:", T_Cabe)
print(f"El promedio de bioseguridad en:", {sucursar}, "es:", B_Cabe)
print("************************************")

sucursar = "Castellana"
S_Caste = round(database.promedio_servico(sucursar), 2)
P_Caste = round(database.promedio_puntualidad(sucursar), 2)
I_Caste = round(database.promedio_instalaciones(sucursar), 2)
T_Caste = round(database.promedio_tratamiento(sucursar), 2)
B_Caste = round(database.promedio_bioseguridad(sucursar), 2)
print(f"El promedio de servicio en:", {sucursar}, "es:", S_Caste)
print(f"El promedio de puntualidad en:", {sucursar}, "es:", P_Caste)
print(f"El promedio de instalaciones en:", {sucursar}, "es:", I_Caste)
print(f"El promedio de tratamiento en:", {sucursar}, "es:", T_Caste)
print(f"El promedio de bioseguridad en:", {sucursar}, "es:", B_Caste)
print("************************************")

sucursar = "Normandia"
S_Norma = round(database.promedio_servico(sucursar), 2)
P_Norma = round(database.promedio_puntualidad(sucursar), 2)
I_Norma = round(database.promedio_instalaciones(sucursar), 2)
T_Norma = round(database.promedio_tratamiento(sucursar), 2)
B_Norma = round(database.promedio_bioseguridad(sucursar), 2)
print(f"El promedio de servicio en:", {sucursar}, "es:", S_Norma)
print(f"El promedio de puntualidad en:", {sucursar}, "es:", P_Norma)
print(f"El promedio de instalaciones en:", {sucursar}, "es:", I_Norma)
print(f"El promedio de tratamiento en:", {sucursar}, "es:", T_Norma)
print(f"El promedio de bioseguridad en:", {sucursar}, "es:", B_Norma)


"""np.random.seed(6789)
x = np.random.gamma(4, 0.5, 1000)
result = plt.hist(x, bins=20, color='c', edgecolor='k', alpha=0.65)
plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=1)

min_ylim, max_ylim = plt.ylim()
plt.text(x.mean()*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(x.mean()))
plt.show()"""

servicio = [S_Cabe, S_Caste, S_Norma]
Columna3 = ["Cabecera", "Castellana", "Normandia"]
plt.grid(True)

#Para lineas
#plt.plot(servicio, Columna3, '#cd98f1', alpha=0.6)
# Para histograma
#plt.hist(servicio, bins=30)
# Para barras
plt.bar(servicio, Columna3, color='#cd98f1')
plt.legend(('Servicio', ), loc = 'upper right')
plt.xlabel("Satisfacción", fontsize = 15)
plt.ylabel("Clínica o sede", fontsize = 15)
plt.savefig("Servicio.jpg")
plt.show()