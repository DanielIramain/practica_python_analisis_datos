# # import pandas as pd

# # # Cargar el dataset
# # df = pd.read_csv('train.csv')

# # #print(df.head())

# # # Información general del DataFrame
# # #print(df.info())

# # # Resumen estadístico de las coolumnas numerícas
# # #print(df.describe())

# # # Mostrar las columnas
# # # print(df.columns)

# # # Contar valores faltantes en cada columna
# # #print(df.isnull().sum())

# # # Eliminar filas con valores faltantes
# # df_limpio = df.dropna()

# # # Eliminar filas duplicadas
# # df_sin_duplicados = df_limpio.drop_duplicates()
# # print(df_sin_duplicados)


#################
# EDA Enfoque estructura

import pandas as pd

####
# 1 Cargar los datos

# Cargar el dataset
df = pd.read_csv('student_performance_data.csv')

# Mostrar primeras y últimas 5 filas
#print(df)


####
# 2 Exploración Inicial de los Datos

# 2.1 Entender la Extructura del DataSet

# Información general del DataFrame
#print(df.info())

# Resumen estadístico de lass columnas numéricas
#print(df.describe())

# Mostrar las columnas
#print(df.columns)

# 2.2 Identificar los valores Faltantes

# Contar valores faltantes en cada columna
#print(df.isnull().sum())

####
# 3 Análisis Estadístico y Distribución de Datos

# 3.1 Distribución de las Variables Numéricas

# Distribución de las edades
#print(df['Age'].describe())

#print(df['StudyHoursPerWeek'].describe())

# 3.1 Análisis de Variables Categóricas

# print(df['Gender'].value_counts())
# print(df['Major'].value_counts())
# print(df['PartTimeJob'].value_counts())
# print(df['ExtraCurricularActivities'].value_counts())

####
# 4 Indentificación de Patrones y Relaciones

#4.1 Relación entre variables numéricas

# Filtrar solo las columnas numéricas

df_numerico = df.select_dtypes(include=['number'])

print(df_numerico.corr())



