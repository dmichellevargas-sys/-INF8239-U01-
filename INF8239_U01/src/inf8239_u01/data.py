"""
Descarga reproducible del dataset propio del Ejercicio 01/02:
Iranian Churn Dataset (UCI Machine Learning Repository, id 563, licencia CC BY 4.0,
DOI 10.24432/C5JW3Z).

No usar rutas de Google Drive personal ni C:\\Users\\... como única fuente:
la función siempre descarga desde una URL HTTP(S) verificada y guarda una copia
local reproducible en data/raw/.
"""
from pathlib import Path

import pandas as pd

# Sustituir por la URL directa aprobada (espejo de Hugging Face o descarga
# oficial de UCI ya verificada por el estudiante).
IRANIAN_CHURN_DATASET_URL = "PEGAR_URL_DIRECTA_APROBADA"


def download_csv(url: str = IRANIAN_CHURN_DATASET_URL,
                  destination: str = "data/raw/iranian_churn_dataset.csv") -> Path:
    if not url.startswith(("https://", "http://")):
        raise ValueError("La fuente debe ser una URL HTTP(S)")

    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)

    frame = pd.read_csv(url)
    if frame.empty:
        raise ValueError("El dataset descargado está vacío")

    frame.to_csv(path, index=False)
    return path
