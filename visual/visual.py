import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../ventas.csv', delimiter=';')

# print(df.head())

# EDA

# Eliminar filas con valores nulos
df_limpio = df.dropna()

# Configurar el estilo visula de seaborn
sns.set_theme(style='whitegrid')


# 1 - Distribución del Precio de Venta.
# plt.figure(figsize=(10,6))
# sns.histplot(df_limpio['precio de venta'], kde=True, bins=5, element='step', alpha=0.4)
# plt.title('Distribución del Precio de Venta')
# plt.xlabel('Precio de Venta')
# plt.ylabel('Frecuencia')
# plt.show()

######
# # 2 Ventas por Categoría de Producto
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Categoria', order=df_limpio['Categoria'].value_counts().index, palette='pastel', hue='Categoria', legend=True)
# plt.title('Venta por Categoría de Producto')
# plt.xlabel('Categoría')
# plt.ylabel('Número de Venta')
# plt.xticks(rotation=45)
# plt.show()


######
# # 3 Ventas por Género de Producto
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Genero', order=df_limpio['Genero'].value_counts().index, palette='pastel', hue='Genero', legend=True)
# plt.title('Venta por Genero de Producto')
# plt.xlabel('Genero')
# plt.ylabel('Número de Venta')
# plt.xticks(rotation=45)
# plt.show()


######
# # 4 Ventas por Marca de Producto
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Marca', order=df_limpio['Marca'].value_counts().index, palette='pastel', hue='Marca', legend=True)
# plt.title('Venta por Marca de Producto')
# plt.xlabel('Marca')
# plt.ylabel('Número de Venta')
# plt.xticks(rotation=45)
# plt.show()


######
# 5 Ventas por Color de Producto
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Color', order=df_limpio['Color'].value_counts().index, palette='pastel', hue='Genero', legend=True)

# plt.title('Venta por Color de Producto')
# plt.xlabel('Color')
# plt.ylabel('Número de Venta')
# plt.xticks(rotation=45)
# plt.show()


######
# 6 Distribución de Ventas por Hora del día

# df_limpio['Hora'] = pd.to_datetime(df_limpio['Hora'], format='%H:%M:%S').dt.hour

# plt.figure(figsize=(10,6))
# sns.histplot(df_limpio['Hora'], bins=24)
# plt.title('Distribución de Venta por Hora del día')
# plt.xlabel('Hora del Día')
# plt.ylabel('Número de Ventas')
# plt.xticks(range(0,24))
# plt.show()


######
# 7 Ventas a lo largo del mes

# df_limpio['Fecha'] = pd.to_datetime(df_limpio['Fecha'], format= '%d/%m/%Y')
# df_limpio['Día'] = df_limpio['Fecha'].dt.day

# plt.figure(figsize=(10,6))

# sns.lineplot(data=df_limpio, x='Día', y='precio de venta', estimator='sum', errorbar=None)

# plt.title('Ventas a lo largo del Mes')
# plt.xlabel('Día del Mes')
# plt.ylabel('Total de Venta')
# plt.xticks(range(1, 32))
# plt.show()


######
# 8 Distribución de Ventas por día de la Semana

# ### df_limpio['Hora'] = pd.to_datetime(df_limpio['Hora'], format='%H:%M:%S').dt.hour
# df_limpio['Fecha'] = pd.to_datetime(df_limpio['Fecha'], format= '%d/%m/%Y')
# df_limpio['Día de la Semana'] = df_limpio['Fecha'].dt.day_name()


# plt.figure(figsize=(10,6))

# sns.countplot(data=df_limpio, x='Día de la Semana', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], legend=True)

# ### sns.countplot(data=df_limpio, x='Día de la Semana', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], hue='Hora', legend=True)

# plt.title('Distribución de Ventas por día de la semana')
# plt.xlabel('Día de la Semana')
# plt.ylabel('Número de Venta')
# plt.xticks(rotation=45)
# plt.show()


df_limpio['Fecha'] = pd.to_datetime(df_limpio['Fecha'], format='%d/%m/%Y')
df_limpio['Hora'] = pd.to_datetime(df_limpio['Hora'], format='%H:%M:%S')


# Extraer componentes de la fecha
df_limpio['Año'] = df_limpio['Fecha'].dt.year
df_limpio['Mes'] = df_limpio['Fecha'].dt.month
df_limpio['Día'] = df_limpio['Fecha'].dt.day
df_limpio['DíaSemana'] = df_limpio['Fecha'].dt.day_name()
df_limpio['SemanaDelAño'] = df_limpio['Fecha'].dt.isocalendar().week

# print(df_limpio[['Año', 'Mes', 'Día', 'DíaSemana', 'SemanaDelAño']])


# Extraer componentes de la hora

df_limpio['Segundo'] = df_limpio['Hora'].dt.second
df_limpio['Minuto'] = df_limpio['Hora'].dt.minute
df_limpio['Horas'] = df_limpio['Hora'].dt.hour


# print(df_limpio[['Hora', 'Minuto', 'Segundo']])



# Fecha y Hora

df_limpio['FechaHora'] = pd.to_datetime(df_limpio['Fecha'].astype(str) + ' ' + df_limpio['Hora'].astype(str))

# print(df_limpio['FechaHora'].dt.year)
# print(df_limpio['FechaHora'].dt.month)
# print(df_limpio['FechaHora'].dt.hour)
# print(df_limpio['FechaHora'].dt.second)


####
# Distrubución de Ventas por Hora del Día

# Propósito: Ver la distribución de las ventas a diferentes horas del día para identificar patrones de compra.

# plt.figure(figsize=(10, 6))
# sns.histplot(df_limpio['FechaHora'].dt.hour, bins=24, kde=True)
# plt.title('Distribución de Ventas por Horas del Día')
# plt.xlabel('Hora del Día')
# plt.ylabel('Frecuencia')
# plt.show()

'''
Métodos y Parámetros:

    plt.figure(figsize=(10, 6)): Configura el tamaño de la figura (10 unidades de ancho por 6 unidades de alto).

    sns.histplot: Crea un histograma.

        - df_limpio['FechaHora'].dt.hour: Extrae la hora del día de la columna FechaHora.

        - bins=24: Define el número de intervalos (barras) en el histograma, en este caso 24 horas.

        - kde=False: Desactiva la curva de densidad (Kernel Density Estimate) para mostrar solo el histograma.

    plt.title: Añade un título al gráfico.

    plt.xlabel y plt.ylabel: Etiquetan los ejes X e Y respectivamente.

    plt.show(): Muestra el gráfico.

'''


####
# Precio Promedio por Hora

# Propósito: Evaluar cómo varía el precio promedio de venta a lo largo del día.

# plt.figure(figsize=(10, 6))
# sns.lineplot(x=df_limpio['FechaHora'].dt.hour, y=df_limpio['precio de venta'], estimator='mean')
# plt.title('Precio Promedio por Hora del Día')
# plt.xlabel('Hora del Día')
# plt.ylabel('Precio Promedio')
# plt.show()

'''
Métodos y Parámetros:

    sns.lineplot: Crea un gráfico de líneas.
        - x=df_limpio['FechaHora'].dt.hour: Establece el eje X con la hora del día.
        - y=df_limpio['precio de venta']: Establece el eje Y con los precios de venta.
        - estimator='mean': Calcula la media de los precios para cada hora.

    plt.title, plt.xlabel, plt.ylabel, plt.show(): Añaden título, etiquetas de los ejes y muestran el gráfico.
'''


####
# Precios por Categoría

# Propósito: Comparar la variabilidad de los precios entre diferentes categorías de productos.

# plt.figure(figsize=(12, 6))
# sns.boxplot(x='Categoria', y='precio de venta', data=df_limpio)
# plt.title('Distribución de Precios por Categoría')
# plt.xlabel('Categoría')
# plt.ylabel('Precio de Venta')
# plt.show()

'''
Métodos y Parámetros:

    sns.boxplot: Crea un gráfico de cajas (boxplot).
        - x='Categoria': Establece el eje X con las categorías de productos.
        - y='precio de venta': Establece el eje Y con los precios de venta.
        - data=df: Indica el DataFrame que contiene los datos.
    
    plt.title, plt.xlabel, plt.ylabel, plt.show(): Añaden título, etiquetas de los ejes y muestran el gráfico.
'''


####
# Número de Ventas por Día de la Semana

# Propósito: Analizar en qué días de la semana se realizan más ventas.

plt.figure(figsize=(10, 6))
sns.countplot(x=df_limpio['DíaSemana'])
plt.title('Número de Ventas por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Número de Ventas')
plt.show()

'''
Métodos y Parámetros:

    sns.countplot: Crea un gráfico de conteo.
        - x=df_limpio['DíaSemana']: Establece el eje X con los días de la semana.
    
    plt.title, plt.xlabel, plt.ylabel, plt.show(): Añaden título, etiquetas de los ejes y muestran el gráfico.
'''