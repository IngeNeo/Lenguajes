import numpy as np
import matplotlib.pyplot as plt

serie_1 = [406, 387, 442, 457, 485]
serie_2 = [421, 453, 435, 478, 512]


numero_de_grupos = len(serie_1)
indice_barras = np.arange(numero_de_grupos)
ancho_barras =0.35

plt.bar(indice_barras, serie_1, width=ancho_barras, label='Hombres')
plt.bar(indice_barras + ancho_barras, serie_2, width=ancho_barras, label='Mujeres')
plt.legend(loc='best')
## Se colocan los indicadores en el eje x
plt.xticks(indice_barras + ancho_barras, ('2017', '2018', '2019', '2020','2021'))

plt.ylabel('Numero de habitantes')
plt.xlabel('Año')
plt.title('Numero de habitantes por genero')

plt.show()