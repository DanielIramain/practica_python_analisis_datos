import numpy as np

# # Convertir una lista de Python a un array de NumPy
# arr = np.array([1,2,3,4,5])

# #print (arr)

# # Array de 2 dimensiones (Misma cantidad de elementos)
# arr_2d = np.array([[1,2,3,4], [6,7,8,9]])


# #print (arr_2d)


# arr_3x3 = np.zeros((3,3))

# arr_3x3_one = np.ones((2,4))

# arr_alea = np.arange(0, 10, 2)



# print(arr_alea)


# Ejercicios Prácticos

# Ejercicio 1: Creación y Manipulación de Arrays
# Objetivo: Crear un array de NumPy a partir de una lista de Python y realizar operaciones básicas con el array.
# Instrucciones:
# Crea un array con los números del 1 al 10.
# Multiplica todos los elementos por 2.
# Extrae todos los elementos que sean mayores a 5.

#########
# # Crear el array
# arr = np.array([1,2,3,4,5,6,7,8,9,10])

# # Multiplicar por 2
# arr_mult = arr * 2

# print(arr_mult)

# # Filtrar elementos mayores a 5
# arr_filtrado = arr[arr > 5]

# print(arr_filtrado)


# Ejercicio 2: Operaciones Matemáticas con Arrays
# Objetivo: Realizar operaciones matemáticas básicas con NumPy.
# Instrucciones:
# Crea dos arrays: a y b de tamaño 5 con valores aleatorios.
# Suma, resta, multiplica y divide los arrays.
# Calcula la media y desviación estándar de los valores de los arrays.

#########
# a = np.random.rand(5)
# b = np.random.rand(5)


# suma = a + b
# resta = a - b
# mult = a * b
# divi = a / b


# # Media y desviación estándar

# media = np.mean(a)

# print(media)

# desvi = np.std(a)
# print(desvi)


# Ejercicio 3: Manipulación de Arrays Multidimensionales
# Objetivo: Trabajar con arrays multidimensionales.
# Instrucciones:
# Crea un array 3x3 de números enteros aleatorios.
# Accede al elemento en la posición (1, 2).
# Cambia el valor de la fila 2 por ceros.
# Calcula la suma de todos los elementos del array.

#######
# # Array de 3x3
# arr_3d = np.random.randint(1,10, (3,3))
# print(arr_3d)

# elemento = arr_3d[1,2]

# arr_3d[2, :] = 0 


# suma_total = np.sum(arr_3d)
# print(suma_total)


# Ejercicio 4: Uso de Funciones de NumPy
# Objetivo: Utilizar funciones predefinidas de NumPy para el análisis de datos.
# Instrucciones:
# Crea un array de 100 números aleatorios entre 0 y 1.
# Calcula la suma, el promedio, el máximo y el mínimo de los elementos.
# Ordena los elementos del array de menor a mayor.

# # Crea un array de 100 números aleatorios entre 0 y 1.
# arr_random = np.random.rand(100)

# # Calcula la suma, el promedio, el máximo y el mínimo de los elementos.

# suma = np.sum(arr_random)
# promedio = np.mean(arr_random)
# maximo = np.max(arr_random)
# minimo = np.min(arr_random)

# # Ordena los elementos del array de menor a mayor.
# arr_ordenado = np.sort(arr_random)
# print(arr_ordenado)




# Ejercicio 5: Análisis de Ventas
# Objetivo: Utilizar NumPy para realizar un análisis detallado de ventas, identificar patrones de compra y generar informes de desempeño.

# Contexto Empresarial: Una empresa desea analizar sus ventas mensuales para identificar los productos más vendidos y los meses de mayor actividad.

# Instrucciones:
# Simula un conjunto de datos que represente las ventas mensuales de 5 productos durante un año (12 meses):
# Calcula el total de ventas por producto en el año.
# Identifica el mes con mayores ventas para cada producto.
# Calcula el promedio de ventas mensuales por producto.
# Genera un array que contenga la diferencia porcentual de ventas entre meses consecutivos.


# Simula un conjunto de datos que represente las ventas mensuales de 5 productos durante un año (12 meses)
ventas = np.random.randint(500, 2000, (5, 12))
print(ventas)

# Calcula el total de ventas por producto en el año.
total_ventas_producto = np.sum(ventas, axis=1)
# print(total_ventas_producto)
# print()

# Identifica el mes con mayores ventas para cada producto.
mes_max_ventas = np.argmax(ventas, axis=1)
# print(mes_max_ventas)

# Calcula el promedio de ventas mensuales por producto.
promedio_ventas_producto = np.mean(ventas, axis=1)
# print(promedio_ventas_producto)

# Genera un array que contenga la diferencia porcentual de ventas entre meses consecutivos.

diferencia_porcentual = np.diff(ventas, axis=1) / ventas[:, :-1] * 100
print(diferencia_porcentual)


