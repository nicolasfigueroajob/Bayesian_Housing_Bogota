# Entrega 1: Dinámicas del Mercado Inmobiliario en Bogotá: Un Problema Social Analizado a través de la Comparación de Modelos Predictivos

### 1. Tema y delimitación inicial
Este proyecto aborda la fijación de precios en el mercado inmobiliario de Bogotá entendiéndolo como un profundo problema social ligado a la desigualdad espacial, la accesibilidad a la vivienda y la estratificación. En lugar de limitarse a un ejercicio técnico de predicción, la investigación busca evaluar y comparar cómo diferentes aproximaciones estadísticas entienden y explican este fenómeno. El análisis se centra en transacciones reales de vivienda (2015-2023) registradas por el IGAC en el casco urbano de Bogotá D.C. Se busca demostrar que la elección de un modelo matemático (tradicional, ML o Bayesiano) no es trivial, ya que cada uno aporta información distinta para entender las brechas socioeconómicas, siendo el modelo bayesiano la pieza clave para cuantificar la incertidumbre y el riesgo formal en el acceso a la vivienda.

### 2. Pregunta de investigación
¿De qué manera la comparación metodológica entre modelos lineales, de ensamble predictivo (Random Forest) y estadísticos probabilísticos (Bayesianos) permite explicar las dinámicas de desigualdad socioespacial en el precio de la vivienda residencial en Bogotá, y qué aporta específicamente la estimación de incertidumbre Bayesiana al entendimiento del riesgo de este problema social?  
La investigación trasciende la búsqueda de la simple minimización del error; se enfoca en evaluar empíricamente el sesgo y el valor metodológico (trade-off) de cada enfoque: capacidad predictiva estática, interpretabilidad causal política y estimación estocástica del riesgo (especialmente importante para zonas vulnerables o con alta evasión informacional).

### 3. Mini-protocolo de revisión (síntesis)
*   **PICOC adaptado:**
    *   **P (Población):** Transacciones inmobiliarias y grupos residenciales en contextos urbanos de alta estratificación socioeconómica (sistema de clases).
    *   **I (Intervención):** Implementación predictiva comparativa con foco principal de desarrollo analítico en procesos Bayesianos (Modelación Probabilística GPR / PyMC).
    *   **C (Comparación):** Modelos hedónicos clásicos (OLS econométrico) para evaluar interpretabilidad vs. modelos de algoritmos de Ensambles (Random Forest) para establecer un baseline predictivo comercial de máxima precisión.
    *   **O (Resultados):** Aportación social frente a la capacidad predictiva (RMSE, MAE), interpretabilidad directa diferencial sobre variables de estratificación y distribución probabilística de la incertidumbre espacial.
    *   **C (Contexto):** Megaciudades del sur global y países en vía de desarrollo marcadas por heterogeneidad de información pública e índices de segregación espacial crónicos como Bogotá D.C.
*   **Cadena de búsqueda:** `TITLE-ABS-KEY ( ( "housing affordability" OR "spatial inequality" OR "housing prices" ) AND ( "model comparison" OR "bayesian model" OR "machine learning" ) AND "urban" )`
*   **Criterios de inclusión:** (1) Estudios evaluativos de modelos analíticos en fenómenos habitacionales, (2) Publicados entre 2000 y 2026.
*   **Criterios de exclusión:** (1) Trabajos concentrados puramente en la reducción del error computacional sin derivación interpretativa socioespacial, (2) Propiedades netamente corporativas / industriales.
*   **Número final de artículos incluidos:** 4

### 4. Síntesis crítica de la literatura
El consenso metodológico actual refleja un patrón de desalineamiento científico en la proptech: el campo opta recurrentemente por hiper-optimizar algoritmos de "caja negra" orientados a minimizar el error predictivo general, reduciendo ciegamente el RMSE, e ignorando la profunda asimetría espacial urbana. Autores de base (como Jin & Xu, 2024) y ensayos sobre ciencia urbana advierten que los mercados de países en vía de desarrollo son espacialmente muy volátiles. Las aproximaciones puramente algorítmicas imponen así un enfoque determinístico perjudicial: fallan en la segmentación social equitativa y no proveen formas de entender qué dinámicas burocráticas provocan que los precios se encarezcan especulativamente asfixiando el modelo del estado de bienestar urbano.

### 5. Identificación del vacío
Se subraya un déficit notable al interpretar teóricamente al mercado de bienes raíces como algo determinístico e invariable y no como un sistema social estocástico y probabilístico.
*   **Patrón identificado:** Privilegio sistémico por maximizaciones matemáticas (Random Forest/XGBoost) mermando la equidad algorítmica y ocultando la asimetría de la varianza en zonas económicas desfavorecidas.
*   **Supuesto subyacente:** Tratar un único estimado predictivo puntual ("caja negra") como la respuesta fáctica y neutral más idónea para todas las geografías internas por igual.
*   **Vacío investigativo/empírico:** Ausencia evidente de esquemas técnicos que crucen datos del catastro oficial (IGAC de Bogotá) integrando la comparativa directa entre los aportes de las técnicas probabilísticas Bayesianas para capturar incertidumbre urbana (esfuerzo central), y los estándares clásicos predictivos, todo en el marco explícito de identificar a la vivienda y la segregación geoespacial formal como foco social.

### 6. Declaración formal de contribución
Este proyecto re-articula el diseño analítico implementando un andamiaje técnico comparativo apoyado en tres pilares que capturan interacciones diferentes del mercado inmobiliario bogotano: Un pilar de **causalidad y política pública** (algoritmos Baseline Hedónicos/Lineales), un pilar de **optimización de mercado ciego** (Machine Learning estructurado vía Random Forest) y, ocupando el enfoque y recurso investigativo y de desarrollo predominante del curso, el **Pilar de Evaluación del Riesgo Bayesiano Probabilístico**. La contribución fundamental será ilustrar matemáticamente lo indispensable que es un modelo probabilístico bayesiano al permitir emitir curvas continuas de certidumbre (distribuciones a posteriori) indicadoras directamente de zonas donde el sistema institucional socioeconómico tiene grandes y dispares fallas de mercado.

### 7. Alcance y viabilidad
*   **Dataset identificado:** Censo y Registro oficial de Transacciones Inmobiliarias vía API IGAC (Sectores residenciales, base de datos `datos.gov.co` clave `7y2j-43cv`) en el marco metropolitano de Bogotá D.C.
*   **Variable objetivo:** Costo y devaluación del bien en términos de valor unitario por metro cuadrado formal.
*   **Variables clave sociales y físicas:** Elementos de localización (Zonning Institucional Céntrico/Periferia), antigüedad inmobiliaria, nivel de Estrato económico implícito y fluctuación post-pandemia a nivel años.
*   **Modelos a Evaluar/Contrastar:** 
    1. Regresión Lineal OLS / Hedónica (*Propósito Social: Causalidad, Transparencia para Políticas Públicas y Estructuración*).
    2. Ensamble de Árboles - Random Forest (*Propósito Técnico: Precisión de predicciones sin sesgos estructurales y tasaciones en masa*).
    3. **Regresión Estadística Bayesiana** (*Eje de Enfoque Principal: Entendimiento de la desigualdad informativa, cálculo de varianzas, e intervalos de validación probabilística del sesgo social de los avalúos*).
*   **Métricas Evaluativas:** MAE, MSE/RMSE conjugadas obligatoriamente en cruce con Cobertura de Intervalos Bayesianos de Credibilidad (HPD Coverage Ratio) o sesgos residuales por área social.
*   **Declaración de No Alcance:** Modelación e inclusión computacional de activos remiseros comerciales o naves industriales puras. No se busca un bot o agente inmobiliario absoluto e interpretado sin revisión humana.
*   **Justificación de viabilidad:** Técnicamente consolidado por disponer exitosamente de las colecciones de base de datos a lo largo de un marco histórico multianual por API, las limpiezas basales, una sólida revisión bibliográfica pre-estructurada y lineamientos claros sobre metodologías bayesianas y sus respectivos frameworks teóricos ya establecidos en python (`PyMC`).
