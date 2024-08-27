import pandas as pd

# Paso 1: Cargar los Datos

# Cargar el archivo excel
file_path = 'SuperStoreUS-2015.xlsx'
df = pd.read_excel(file_path)

# # Mostrar las primeras filas para verificar carga
# print(df.head())

# # Información general del DataFrame
# print(df.info())


# ########
# # Paso 2: Exploración Inicial de los Datos

# # Resumen estadístico de las columnas numéricas
# print(df.describe())

# # Verificación de valores faltantes
# print(df.isnull().sum())

# # Columnas disponibles en el dataset
# print(df.columns)


########
# Paso 3: Análisis específico de las Preguntas

# ####
# # 1. ¿Cúal es el ingreso total generado por la Tienda.
# # Para calcular el ngreso total generado por la tienda, sumamos la comulna 'Ventas'

# ingreso_total = df['Ventas'].sum()
# print(f'Ingreso total generado por la tienda $ {ingreso_total:,.2F}')

# ####
# # 2. Qué categoría de productos contribuye mas a las ventas?
# # Sumamos las ventas por cada categoría y encontramos la categoría con el valor más alto.

# # Ventas por categoría de producto
# ventas_por_categoria = df.groupby('Categoría de Producto')['Ventas'].sum()

# # Categoría con mayor contribución a las ventas
# categoria_mayor_ventas = ventas_por_categoria.idxmax()

# print(f'La categoría de productos que más contribuye a las ventas es: {categoria_mayor_ventas} con un total de ventas de $ {ventas_por_categoria.max():,.2f}')


# ####
# # 3. Qué región tiene las ventas más altas y cuál tiene las más bajas?

# # Ventas por región
# ventas_por_region = df.groupby('Región')['Ventas'].sum()

# # Región con mayores y menores ventas
# region_mayor_ventas = ventas_por_region.idxmax()
# region_menor_ventas = ventas_por_region.idxmin()

# print(f'La región con las ventas más altas es: {region_mayor_ventas} con un total de ${ventas_por_region.max():,.2f} ')
# print(f'La región con las ventas más bajas es: {region_menor_ventas} con un total de ${ventas_por_region.min():,.2f} ')

# ####
# # 4. Cuál es el margen de utilidad promedio de la tienda?

# # Margen de utilidad promedio
# margen_utilidad_promedio = df['Margen Base del Producto'].mean()
# print(f'El margen de utilidad promedio de la tienda es: {margen_utilidad_promedio:,.2f}')

# ####
# # # 5. Proyección de Compras Basadas en lo Vendido

# # Asegurarnos de que la columna de fechas esté en formato datetime
df['Fecha de Pedido'] = pd.to_datetime(df['Fecha de Pedido'])

# # Agregar una columna con el mes y año del pedido
df['Mes-Año'] = df['Fecha de Pedido'].dt.to_period('M')

# # Agrupar por mes y calcular la cantidad total vendida
# ventas_mensuales = df.groupby('Mes-Año')['Cantidad Ordenada'].sum()

# # Calcular el promedio de ventas mensuales
# promedio_ventas_mensuales = ventas_mensuales.mean()
# print(f'El promedio de ventas mensuales es: {promedio_ventas_mensuales:.2f}')

# # Proyectar ventas paralos próximos 6 meses
# proyeccion = promedio_ventas_mensuales * 6
# print(f'La proyección de ventas para los próximos 6 meses es: {proyeccion:.2f} unidades')

# ####
# # 6. Margen de Ganancia por Categoría de Producto
# # Analizar cuál es el margen de ganancia promedio por categoría de producto para identificar cuáles son más rentables

# # Agrupar por categoría de producto y calcular el margen de ganancia promedio
# margen_por_categoria = df.groupby('Categoría de Producto')['Margen Base del Producto'].mean()

# print('Margen de ganancia promedio por categoría de producto:')
# print(margen_por_categoria)



# ####
# # 7. Análisis de Ventas por Segmentos de Cliente
# # Entenderemos cómo se distribuyen las ventas entre los diferentes segmentos de clientes

# # Agrupar por segmento de cliente y sumar las ventas
# ventas_por_segmento = df.groupby('Segmento de Cliente')['Ventas'].sum()

# print('Ventas por segmento de cliente:')
# print(ventas_por_segmento)


####
# 8. Tendencia de Ganancias a lo Largo del Tiempo
# Analizar cómo han evolucionado las ganancias a lo largo del tiempo

# Agrupar por mes y calcular las ganancias totales 
ganancias_mensuales = df.groupby('Mes-Año')['Ganancia'].sum()

print('Tendencia de ganancias mensuales:')
print(ganancias_mensuales)

