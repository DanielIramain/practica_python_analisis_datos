# # Introducción a la Estadística Descriptiva
# # 1- Medidas de resumen para variables cuantitativas


import numpy as np
import statistics as stat

# # Datos de ejemplo
# datos = np.array([10, 20, 20, 30, 40, 50])


# # media
# media = np.mean(datos)
# print(f'Media: {media:.2f}')


# # mediana
# mediana = np.median(datos)
# print(f'Mediana: {mediana}')


# # moda
# moda = stat.mode(datos)
# print(f'Moda: {moda}')


# # varianza
# varianza = np.var(datos)
# print(f'Varianza: {varianza:.2f}')


# # desviacion estandar
# desvio_estandar = np.std(datos)
# print(f'Desvío Estandar: {desvio_estandar}')

# # Cuartiles
# q1 = np.percentile(datos, 25)
# q2 = np.percentile(datos, 50)
# q3 = np.percentile(datos, 75)
# ric = q3 - q1


# print(f'Q1: {q1}')
# print(f'Q2 (Mediana): {q2}')
# print(f'Q3: {q3}')
# print(f'Ric: {ric}')



# #########
# # 2. Correlación y Causalidad

# #2.1 Correlación Perason - -1 y 1

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([10, 8, 6, 4, 2])

# # Cálculo de la correlación de Pearson
# correlacion = np.corrcoef(x, y)[0 , 1]
# print(f'Correlación de Person: {correlacion}')



# 3. Práctica Integrada

'''
    En esta sección, se sugiere realizar una serie de ejercicios prácticos que integren los conceptos aprendidos:

    Cálculo de medidas de resumen: Utiliza un conjunto de datos real o simulado para calcular la media, mediana, moda, varianza, desvío estándar y cuartiles.

    Análisis de correlación: Selecciona dos variables continuas de un conjunto de datos y calcula su coeficiente de correlación. Interpreta el resultado y discute si podría existir una relación causal.

    Interpretación de resultados: Discute cómo las medidas de resumen pueden cambiar si se añaden outliers o si se modifican ciertos valores de los datos.
'''


# Calificaciones en dos exámenes
examen1 = np.array([78, 85, 92, 88, 70, 85, 95, 90, 100, 88])
examen2 = np.array([82, 80, 91, 85, 75, 87, 96, 93, 98, 89])


# Cálculo de medidas de resumen
media_ex1 = np.mean(examen1)
media_ex2 = np.mean(examen2)
mediana_ex1 = np.median(examen1)
moda_ex1 = stat.mode(examen1)
varianza_ex1 = np.var(examen1)
desvio_estandar_ex1 = np.std(examen1)
q1_ex1 = np.percentile(examen1, 25)
q2_ex1 = np.percentile(examen1, 50)
q3_ex1 = np.percentile(examen1, 75)
ric = q3_ex1 - q1_ex1


# Cálculo de la correlación de los exámenes
correlacion_ex1_ex2 = np.corrcoef(examen1, examen2)[0, 1]

print(f'Media Examen 1: {media_ex1}')
print(f'Media Examen 2: {media_ex2}')
print(f'Mediana Examen 1: {mediana_ex1}')
print(f'Moda Examen 1: {moda_ex1}')
print(f'Varianza Examen 1: {varianza_ex1}')
print(f'Desvio Estandar Examen 1: {desvio_estandar_ex1}')
print(f'Q1 Examen 1: {q1_ex1}')
print(f'Q2 Examen 1: {q2_ex1}')
print(f'Q3 Examen 1: {q3_ex1}')
print(f'Rango Intercuartil Examen 1: {ric}')
print(f'Correlación entre Examen 1 y Examen 2: {correlacion_ex1_ex2}')














