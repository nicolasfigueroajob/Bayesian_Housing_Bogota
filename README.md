# Proyecto de Estadística Bayesiana: Valuación Inmobiliaria en Bogotá

Este proyecto utiliza estadística bayesiana para predecir el comportamiento futuro de los precios de bienes raíces en Bogotá, utilizando datos oficiales de registros notariales (SNR).

## 🚀 Conexión de Datos
El proyecto se conecta dinámicamente a la API de [datos.gov.co](https://www.datos.gov.co/resource/7y2j-43cv.json) para filtrar información de Bogotá D.C. sin necesidad de descargas masivas de archivos locales.

### Variables del Modelo Bayesiano Propuesto

| Elemento | Variable Propuesta | Definición | Nivel |
| :--- | :--- | :--- | :--- |
| **Variable Dependiente** | `valor` | Precio de transacción inmobiliaria registrado. | Inmueble |
| **Independiente 1** | `orip` | Oficina de Registro (Proxy geográfico: Cercado, Centro, Sur). | Zona |
| **Independiente 2** | `year_radica` | Año de radicación (Tendencia temporal). | Tiempo |
| **Independiente 3** | `num_anotacion` | Complejidad del historial del predio (Proxy antigüedad). | Inmueble |
| **Independiente 4** | `tipo_predio_zona`| Clasificación (Urbano / Rural). | Zona |

## 📂 Estructura del Proyecto
- `data/`: Contiene muestras de datos en JSON/CSV y resúmenes de revisión técnica.
- `src/`: 
  - `fetch_bogota_data.py`: Script para extracción de muestras locales.
  - `dynamic_query_trends.py`: Consultas SoQL directas para análisis de tendencias.
  - `data_review.py`: Script de análisis estadístico profundo (EDA).
- `notebooks/`: Análisis exploratorio y prototipado de modelos bayesianos (PyMC).

## 📊 Problemas Identificados
- **Faltantes**: El 90% de los datos no reportan valor comercial explícito. Se recomienda usar modelos de imputación bayesiana o filtrado por actos de `COMPRAVENTA`.
