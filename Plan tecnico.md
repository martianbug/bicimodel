## Plan técnico (alto nivel)

# Recolectar datos

1.  Descargar meta-datos de estaciones (id, nombre, lat/lon, capacidad) desde EMT/OpenData.

2.  Descargar ficheros históricos de uso (viajes por estación / actividad horaria) desde el portal Open Data.

Para cada estación, usar Google Places Nearby Search (o Place Search) para contar restaurantes/delivery en radios distintos (ej. 100m, 250m, 500m).

(Opcional) si tienes acceso oficial a JustEat/Glovo partner APIs, incluir su base de restaurantes/partners y volumen de pedidos; si no, usar Google Places y cadenas conocidas.

# Preprocesado / Features

Para cada estación × hora (o ventana temporal): 

feature = #restaurantes en 100m/250m/500m, 
distancia media ponderada
capacidad estación
día de semana
hora
festivo/fiesta local
clima (opcional)

Agregar series históricas: bicis disponibles iniciales, entradas/salidas, ratio llenado.

# Modelado

Modelos de series temporales por estación: Prophet o SARIMAX (si quieres modelo por estación).

Modelos ML que aprovechen features espac-temporales: XGBoost/LightGBM para predecir número de bicis disponibles (regresión) o probabilidad de quedarse vacío/lleno (clasificación).

Alternativa avanzada: modelos seq2seq / LSTM / Transformer para series por estación.

# Evaluación

Métricas: MAE / RMSE (regresión), F1/ROC (clasificación de bins). Validación por tiempo (walk-forward).

# Despliegue / uso

Pipeline de ETL (descargas + cache), base de datos (Postgres/PostGIS) para consultas espaciales, endpoints para predicciones (Flask/FastAPI).