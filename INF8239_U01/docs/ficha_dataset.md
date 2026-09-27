# Ficha del dataset

- **Dominio:** Telecomunicaciones (churn / abandono de clientes).
- **Unidad de análisis:** Un cliente/línea de un operador de telecomunicaciones.
- **Decisión que apoya:** Priorizar campañas de retención sobre los clientes con mayor
  probabilidad de darse de baja.
- **Target:** `Churn` (binario: 1 = abandonó, 0 = se mantuvo activo), medido a los 12 meses.
- **Tipo de tarea:** Clasificación binaria.
- **Error más costoso:** Falso negativo (no detectar a un cliente que sí va a abandonar).
- **Usuario de la solución:** Equipo de retención / marketing del operador.

## Dataset seleccionado: Candidato A — Iranian Churn Dataset

- **Procedencia:** UCI Machine Learning Repository, id 563 (donado 2020).
- **Ficha:** https://archive.ics.uci.edu/dataset/563/iranian+churn+dataset
- **Licencia:** CC BY 4.0 (DOI 10.24432/C5JW3Z).
- **Tamaño:** 3,150 filas × 13 atributos + target.
- **Balance de clases:** minoritaria (churn) ~15.7 %.
- **Riesgo de fuga:** bajo-moderado — ver análisis de la variable `Status` más abajo.

## Candidato B (respaldo, no usado): Telco Customer Churn

- **Procedencia:** OpenML (id 42178), réplica del dataset IBM Sample Data Sets.
- **Tamaño:** 7,043 filas × 21 columnas + target.
- Queda como alternativa si el docente prefiere variables más cercanas a un ISP de
  banda ancha o mayor volumen de datos.

## Diccionario de datos (Iranian Churn Dataset)

| Columna | Significado | Tipo | Momento de disponibilidad |
|---|---|---|---|
| Call Failure | Nº de llamadas fallidas | Entero | Antes de predecir |
| Complains | Reclamo registrado (0/1) | Binario | Antes de predecir |
| Subscription Length | Meses de suscripción | Entero | Antes de predecir |
| Charge Amount | Monto de cargo, ordinal 0-9 | Ordinal | Antes de predecir |
| Seconds of Use | Segundos totales de llamadas | Entero | Antes de predecir |
| Frequency of use | Nº total de llamadas | Entero | Antes de predecir |
| Frequency of SMS | Nº total de SMS | Entero | Antes de predecir |
| Distinct Called Numbers | Nº de números distintos llamados | Entero | Antes de predecir |
| Age Group | Grupo etario ordinal (1-5) | Ordinal | Antes de predecir |
| Tariff Plan | Plan (1=prepago, 2=contrato) | Binario | Antes de predecir |
| Status | Estado de la cuenta a los 9 meses (1=activo, 2=no activo) | Binario | Antes de predecir* |
| Age | Edad real del cliente | Entero | Antes de predecir |
| Customer Value | Valor calculado del cliente | Continuo | Antes de predecir |
| **Churn** | **Target: 1 = abandonó, 0 = activo (a los 12 meses)** | Binario | — |

\* `Status` mide actividad a los 9 meses; el target mide abandono a los 12 meses. No es
una fuga idéntica, pero está fuertemente correlacionada con el target. Se conserva como
variable siguiendo el diseño original del dataset, pero se compara el modelo **con y sin**
esta columna (ver `notebooks/02_dataset_propio.ipynb`, Sección 8, y
`reports/iranian_churn_leakage_status_comparison.csv`).

## Hallazgos de auditoría conocidos (confirmar al ejecutar el notebook)

- Sin valores ausentes declarados por UCI.
- Duplicados: la literatura reporta ~300 registros duplicados exactos (~9.5 % de las
  3,150 filas); decidir si conservarlos o eliminarlos y justificarlo.
- Balance de clases: minoritaria (churn) ~15-17 %, desbalance moderado similar a un ISP real.
