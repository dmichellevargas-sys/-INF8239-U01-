from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def build_svm(C: float = 1.0, gamma="scale") -> Pipeline:
    """Pipeline SVM sin fuga de datos: el escalado ocurre dentro del Pipeline,
    por lo tanto se ajusta únicamente con datos de entrenamiento en cada fold.
    """
    if C <= 0:
        raise ValueError("C debe ser positivo")
    return Pipeline([
        ("scale", StandardScaler()),
        ("model", SVC(C=C, gamma=gamma, kernel="rbf", probability=True, random_state=42))
    ])
