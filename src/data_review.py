
import pandas as pd
import numpy as np
import os

def deep_review():
    file_path = "data/bogota_displacement_data.csv"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} no existe.")
        return

    # Cargar datos
    df = pd.read_csv(file_path)
    
    print("=== REVISIÓN PROFUNDA DE LA BASE DE DATOS ===\n")
    
    # 1. Información General
    print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
    print("\nColumnas presentes:")
    print(df.columns.tolist())
    
    # 2. Valores Nulos
    print("\n--- Valores Nulos por Columna ---")
    nulls = df.isnull().sum()
    print(nulls[nulls > 0] if not nulls[nulls > 0].empty else "No hay valores nulos.")
    
    # 3. Tipos de Datos y Valores Únicos
    print("\n--- Cardinalidad (Valores únicos) ---")
    for col in df.columns:
        unique_count = df[col].nunique()
        print(f"{col}: {unique_count} valores únicos (Tipo: {df[col].dtype})")
        
    # 4. Análisis de Variables Numéricas (o que deberían serlo)
    numeric_cols = ['year_radica', 'num_anotacion', 'count_a', 'count_de', 'predios_nuevos', 'tiene_valor']
    # Asegurar que sean numéricas
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    print("\n--- Estadísticas Descriptivas (Numéricas) ---")
    print(df[numeric_cols].describe().round(2))
    
    # 5. Análisis de Variables Categóricas Clave
    print("\n--- Top 5 Tipos de Actos Jurídicos (nombre_natujur) ---")
    print(df['nombre_natujur'].value_counts().head(5))
    
    print("\n--- Distribución por Zona (tipo_predio_zona) ---")
    print(df['tipo_predio_zona'].value_counts())
    
    # 6. Detección de posibles problemas de calidad
    print("\n--- Calidad de Datos ---")
    duplicates = df.duplicated().sum()
    print(f"Filas duplicadas: {duplicates}")
    
    # 7. Potencial para Modelado Bayesiano
    print("\n--- Evaluación para Modelado Bayesiano ---")
    print("Variables predictoras potenciales (Estructura Jerárquica):")
    print("- orip (Oficina de Registro)")
    print("- tipo_predio_zona (Urbano/Rural)")
    print("- nombre_natujur (Tipo de trámite)")
    
    print("\nVariables objetivo potenciales:")
    print("- num_anotacion (Complejidad del historial del predio)")
    print("- tiene_valor (Probabilidad de que un trámite involucre transacciones monetarias)")
    
    # Guardar un resumen técnico para el usuario
    with open("data/review_summary.txt", "w") as f:
        f.write(f"Resumen de Revisión de Datos - Bogotá DC\n")
        f.write(f"Total registros: {len(df)}\n")
        f.write(f"Acto jurídico más común: {df['nombre_natujur'].iloc[0]}\n")
        f.write(f"Zonificación: {df['tipo_predio_zona'].value_counts().to_dict()}\n")

if __name__ == "__main__":
    deep_review()
