# INF-8239 · Ciencia de Datos II — Unidad 01

**Autora:** Dahianna Vargas
**Asignatura:** INF-8239 Ciencia de Datos II (UASD, Maestría en Ciencia de Datos e IA)
**Unidad:** 01 — Modelos avanzados, reducción dimensional y Green AI
**Dataset:** Iranian Churn Dataset (UCI ML Repository, id 563, CC BY 4.0)

## Estado actual

- [x] LAB00 — Entorno reproducible (`.venv`, dependencias, pruebas, Git).
- [x] LAB01 — Pipeline SVM base y reutilizable (`src/inf8239_u01/models.py`).
- [x] LAB02 — Notebook completo del dataset propio, incluyendo el análisis de fuga
      de datos de la variable `Status` (`notebooks/02_dataset_propio.ipynb`).
      **Falta que ejecutes el notebook de inicio a fin** con el CSV real descargado.
- [ ] LAB03 — Ensambles, PCA/t-SNE y comparación Green AI.
- [ ] Ejercicio 01 — PDF de entrega (dataset + SVM + análisis de fuga).
- [ ] Ejercicio 02 — PDF de entrega (Green AI).

## Instalación

```bash
python -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Descarga del dataset

1. Descarga el CSV del Iranian Churn Dataset (UCI id 563) desde una fuente aprobada
   (por ejemplo, mediante el paquete `ucimlrepo` o un espejo verificado).
2. Colócalo en `data/raw/iranian_churn_dataset.csv`, o edita
   `src/inf8239_u01/data.py` con la URL directa aprobada y ejecuta `download_csv()`.

## Ejecutar pruebas

```bash
# Windows (PowerShell)
$env:PYTHONPATH="src"
python -m pytest -q

# macOS/Linux
PYTHONPATH=src python -m pytest -q
```

Nota: las 3 pruebas de `test_data_contract.py` solo pasan una vez que el CSV real
está en `data/raw/iranian_churn_dataset.csv`.

## Trabajar en Google Colab + Google Drive

**Primera vez:**
1. Abre [colab.research.google.com](https://colab.research.google.com) y sube el archivo
   `notebooks/02_dataset_propio.ipynb` (Archivo → Subir cuaderno).
2. Corre la **Sección 0**: te pedirá autorizar el acceso a tu Google Drive y luego subir
   `INF8239_U01_actualizado.zip` (este mismo zip completo). Lo descomprime dentro de tu
   Drive, en `Mi unidad/INF8239_U01` — queda ahí de forma **permanente**.
3. Corre la **Sección 1.1**: te pedirá el CSV del Iranian Churn Dataset (descárgalo antes
   desde UCI). También queda guardado permanentemente en tu Drive.
4. Corre el resto de las celdas normalmente.

**Sesiones siguientes** (otro día, o si Colab se desconecta): solo abre el notebook de
nuevo y corre la Sección 0 — **no vuelve a pedir el zip ni el CSV**, porque ya están
guardados en tu Drive; solo te pedirá autorizar el acceso a Drive otra vez.

No necesitas instalar nada: Colab ya trae `pandas`, `scikit-learn`, etc. preinstalados.

## Trabajar en Jupyter local

Abre `notebooks/02_dataset_propio.ipynb`, selecciona el kernel `.venv` y ejecuta todas
las celdas en orden. **Puedes renombrar el archivo o moverlo a otra subcarpeta dentro
de `INF8239_U01/` sin que se rompa**: la Sección 0 detecta automáticamente la raíz del
proyecto buscando la carpeta `src/inf8239_u01` hacia arriba desde donde esté el notebook.

El notebook incluye:

0. Detección automática de la carpeta del proyecto (sin rutas fijas como `../src`).
1. Carga y auditoría del Iranian Churn Dataset.
2. Definición de target y partición train/test (fija, estratificada).
3. Preprocesamiento dentro de `Pipeline` (sin fuga de datos).
4. Línea base (Dummy) vs. SVM.
5. Búsqueda de hiperparámetros con `GridSearchCV`.
6. **Análisis de fuga de datos:** comparación del modelo con y sin la variable `Status`,
   guardado en `reports/iranian_churn_leakage_status_comparison.csv`.
7. Guardado del modelo final (`reports/iranian_churn_svm_best.joblib`).
8. Espacio para la conclusión (300–500 palabras).

## Versionar avances

```bash
git add .
git commit -m "feat: notebook Ejercicio 01 con analisis de fuga Status - Iranian Churn Dataset"
```
