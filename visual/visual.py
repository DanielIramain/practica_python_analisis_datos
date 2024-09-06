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
