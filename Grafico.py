# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('hospital_beds.csv')

# Filtrar las filas que tienen datos de camas (eliminar las filas vacías)
df = df[df['Country Name'].notna() & df['Country Code'].notna()]

# Convertir las columnas de camas a números (float)
df['2019'] = pd.to_numeric(df['2019'], errors='coerce')

# Ordenar el DataFrame por la columna de camas en orden descendente
df_sorted = df.sort_values(by='2019', ascending=False)

# Tomar los 10 primeros países para visualización
top_countries = df_sorted.head(10)

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(top_countries['Country Name'], top_countries['2019'], color='blue')
plt.xlabel('Países')
plt.ylabel('Camas por 1,000 personas')
plt.title('Top 10 Países con Más Camas de Hospital por 1,000 Personas (2019)')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje x para mayor claridad
plt.tight_layout()

# Mostrar el gráfico
plt.show()
