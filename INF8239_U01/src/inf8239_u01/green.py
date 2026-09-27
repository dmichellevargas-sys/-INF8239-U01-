def pareto_flags(df, score: str = "f1_macro", cost: str = "fit_median_s"):
    """Marca qué filas están en la frontera de Pareto (score alto, costo bajo).

    Una fila está dominada si existe otra fila con score >= y costo <=,
    y estrictamente mejor en al menos una de las dos dimensiones.
    """
    flags = []
    for _, row in df.iterrows():
        dominated = (
            (df[score] >= row[score])
            & (df[cost] <= row[cost])
            & ((df[score] > row[score]) | (df[cost] < row[cost]))
        ).any()
        flags.append(not bool(dominated))
    return flags
