# Dinámicas del Mercado Inmobiliario en Bogotá: Un Enfoque Social y Comparativo de Modelos Predictivos

Este proyecto aborda la predicción de precios de bienes raíces residenciales en Bogotá como un problema profundamente social marcado por la desigualdad espacial y la estratificación. Se desarrolla un escenario comparativo de modelado que va más allá de buscar un simple "menor margen de error" (RMSE), evaluando **qué modelo es más efectivo según el objetivo de interés y qué aporta cada uno a la comprensión del problema del acceso a la vivienda**.

El proyecto destina su **enfoque y esfuerzo principal a la Estadística Bayesiana**, utilizándola como la herramienta definitiva para medir y proyectar la incertidumbre espacial y el riesgo en transacciones inmobiliarias. 

## 🎯 Enfoque Comparativo del Proyecto

En el proyecto se entrenan y analizan los siguientes tipos de modelos extraídos de la literatura:

1. **Modelo Hedónico/Lineal (Clásico OLS):**  
   *Aporte Social:* Alta interpretabilidad socioeconómica. Nos permite responder de manera exacta cuánto impacta el "estrato institucional" o el "área" en la formación del costo de la vivienda. Ideal para guiar **Política Pública**.
2. **Modelo Computacional Predictivo (Random Forest):**  
   *Aporte Social/Técnico:* Alta capacidad de asimilar dinámicas no lineales complejas del entorno urbano. Utilizado como _Baseline Predictivo_ de alta fidelidad, de gran utilidad para estimadores y tasaciones rápidas corporativas.
3. **⭐ Modelo Probabilístico Bayesiano (Foco Principal):**  
   *Aporte Social:* Proporciona una cuantificación rigurosa del **Riesgo y la Incertidumbre**. Al generar distribuciones (intervalos de credibilidad) en vez de valores puntuales absolutos, este modelo permite detectar desigualdades de la información, informando qué nivel de riesgo asumen los habitantes en zonas dispares de la ciudad de Bogotá.

## 🚀 Conexión de Datos

El repositorio emplea los datos oficiales de transacciones verificadas (SNR/IGAC). Las consultas se conectan dinámicamente a la API gubernamental de [datos.gov.co](https://www.datos.gov.co/resource/7y2j-43cv.json) para el espectro de Bogotá D.C. restringido para actos residenciales.

### Variables Estructurales y Sociales

| Elemento | Variable Propuesta | Enfoque de Estudio |
| :--- | :--- | :--- |
| **Variable Dependiente** | `valor` | Costo del acceso a la vivienda formal comercializada. |
| **Socio-Espacial 1** | `orip` / `localidad` / `zona` | Segmentación y segregación espacial en la urbe. |
| **Socio-Económico 2**| `estrato` (*Por incorporar/Mapear*) | Influencia burocrática en la valoración social y estatus del predio. |
| **Físico/Estructural**| `area` / `edad` | Desvalorización y condiciones habitables. |
| **Temporal** | `year_radica` | Dinámicas de inflación y shocks del mercado (ej. Post-pandemia). |

## 🚀 Configuración y Datos

Dado el tamaño del dataset completo (~1.2 GB), este no se encuentra alojado directamente en el repositorio de GitHub. Para obtener los datos actualizados desde la fuente oficial (SODA API):

1. **Instalar dependencias necesarias:**
   ```bash
   pip install requests
   ```

2. **Ejecutar el script de descarga:**
   ```bash
   python fetch_all_bogota.py
   ```
   *Nota: El proceso descarga aproximadamente 4 millones de registros y puede tomar varios minutos dependiendo de la conexión a internet.*

## 📂 Estructura del Proyecto

- `data/`: Datos transaccionales en JSON/CSV utilizados y registros técnicos.
- `src/`: 
  - Scripts de recuperación oficial (`fetch_bogota_data.py`, `fetch_all_bogota.py`)
  - Control de limpieza de datos crudos institucionales a través de EDA (`data_review.py`).
- `notebooks/`: Cuadernos dedicados a la fase comparativa, exploración descriptiva con enfoque social, y la implementación primaria del Modelo de Estadística Bayesiana vía `PyMC`.

## 📊 Retos y Trabajo Futuro

- **Heterogeneidad de Datos Restantes:** La gran mayoría de los registros crudos no reportan su precio real comercial explícito debido a prácticas de subdeclaración o vacíos de formato notarial.
- Es vital usar los algoritmos **Bayesianos** para evaluar precisamente la incertidumbre producida por esta deficiencia institucional asimétrica sobre la población que busca adquirir vivienda en el contexto presente de la ciudad.
