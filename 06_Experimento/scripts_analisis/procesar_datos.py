#!/usr/bin/env python3
"""Etapa 2 de 3 — Procesamiento: limpieza, clasificación y cálculo.

Recibe los datos ya leídos y validados por leer_datos.py, los clasifica en
los tres grupos de área (Clínico / Administrativo / Paciente simulado),
calcula la prueba de chi-cuadrado con permutación Monte Carlo, el intervalo
de confianza bootstrap de V de Cramér, la cobertura de RF Must y el cálculo
de potencia estadística de referencia.

No escribe ningún archivo — eso es responsabilidad de generar_resultados.py.
"""

from __future__ import annotations

import math
import random
from collections import Counter, defaultdict

from scipy.optimize import brentq
from scipy.stats import nct, t


def group_area(area: str) -> str:
    if "Paciente" in area:
        return "Paciente simulado"
    if area in {"Coordinación", "Recepción/Recaudación"}:
        return "Administrativo"
    return "Clínico"


def chi_square(table: list[list[int]]) -> tuple[float, float, float]:
    rows = [sum(row) for row in table]
    cols = [sum(row[j] for row in table) for j in range(len(table[0]))]
    n = sum(rows)
    expected = [[rows[i] * cols[j] / n for j in range(len(cols))] for i in range(len(rows))]
    statistic = sum(
        (table[i][j] - expected[i][j]) ** 2 / expected[i][j]
        for i in range(len(rows))
        for j in range(len(cols))
    )
    cramer_v = math.sqrt(statistic / (n * min(len(rows) - 1, len(cols) - 1)))
    return statistic, min(min(row) for row in expected), cramer_v


def monte_carlo(table: list[list[int]], observed: float, replicas: int = 100_000) -> float:
    row_sizes = [sum(row) for row in table]
    col_sizes = [sum(row[j] for row in table) for j in range(len(table[0]))]
    labels = [index for index, size in enumerate(row_sizes) for _ in range(size)]
    outcomes = [0] * col_sizes[0] + [1] * col_sizes[1]
    rng = random.Random(42)
    extreme = 0
    for _ in range(replicas):
        rng.shuffle(outcomes)
        candidate = [[0, 0] for _ in row_sizes]
        for label, outcome in zip(labels, outcomes):
            candidate[label][outcome] += 1
        statistic, _, _ = chi_square(candidate)
        if statistic >= observed - 1e-12:
            extreme += 1
    return (extreme + 1) / (replicas + 1)


def two_sample_power_n(effect: float = 0.5, alpha: float = 0.05, target: float = 0.8) -> int:
    """Tamaño por grupo para t bilateral, grupos iguales y d de Cohen."""

    def power(n: float) -> float:
        df = 2 * n - 2
        critical = t.ppf(1 - alpha / 2, df)
        noncentrality = effect * math.sqrt(n / 2)
        return nct.sf(critical, df, noncentrality) + nct.cdf(-critical, df, noncentrality)

    solution = brentq(lambda n: power(n) - target, 2.01, 200)
    return math.ceil(solution)


def bootstrap_cramer_ci(
    relations: list[dict[str, str]],
    group_order: list[str],
    replicas: int = 10_000,
    seed: int = 42,
) -> tuple[float, float]:
    """IC 95% de V de Cramér por bootstrap no paramétrico sobre las unidades
    observación-requisito (remuestreo con reemplazo), percentiles 2.5/97.5.
    Misma semilla que la prueba de permutación, para reproducibilidad.
    """

    rng = random.Random(seed)
    n = len(relations)
    valores = []
    for _ in range(replicas):
        muestra = [relations[rng.randrange(n)] for _ in range(n)]
        grouped = defaultdict(lambda: [0, 0])
        for row in muestra:
            finding = row["estado_tarea"] != "COMPLETADA"
            grouped[group_area(row["area"])][int(finding)] += 1
        tabla = [grouped[group] for group in group_order]
        # si algún grupo quedó vacío en la remuestra, se omite esa réplica
        if any(sum(fila) == 0 for fila in tabla):
            continue
        try:
            _, expected_min, v = chi_square(tabla)
        except ZeroDivisionError:
            continue
        if expected_min <= 0:
            continue
        valores.append(v)
    valores.sort()
    lo = valores[int(0.025 * len(valores))]
    hi = valores[int(0.975 * len(valores)) - 1]
    return lo, hi


def procesar(datos: dict[str, list[dict[str, str]]]) -> dict[str, object]:
    """Clasifica y calcula todo lo necesario a partir de los datos crudos.

    Devuelve un diccionario con los resultados numéricos y los valores
    intermedios que generar_resultados.py necesita para escribir las
    tablas, el JSON y las figuras.
    """
    observations = datos["observations"]
    relations = datos["relations"]
    coverage = datos["coverage"]

    states = Counter(row["estado_tarea"] for row in observations)

    group_order = ["Clínico", "Administrativo", "Paciente simulado"]
    grouped = defaultdict(lambda: [0, 0])
    for row in relations:
        finding = row["estado_tarea"] != "COMPLETADA"
        grouped[group_area(row["area"])][int(finding)] += 1
    contingency = [grouped[group] for group in group_order]
    statistic, expected_min, cramer_v = chi_square(contingency)
    p_value = monte_carlo(contingency, statistic)
    cramer_v_ic_inf, cramer_v_ic_sup = bootstrap_cramer_ci(relations, group_order)

    status_field = "Estado_C3" if "Estado_C3" in coverage[0] else next(
        field for field in coverage[0] if "estado" in field.lower()
    )
    passed = sum(row[status_field].strip().upper() in {"PASA", "APROBADO", "CERRADO"} for row in coverage)
    total = len(coverage)
    coverage_percent = 100 * passed / total
    power_n = two_sample_power_n()

    return {
        "observations": observations,
        "relations": relations,
        "states": states,
        "group_order": group_order,
        "contingency": contingency,
        "statistic": statistic,
        "expected_min": expected_min,
        "cramer_v": cramer_v,
        "p_value": p_value,
        "cramer_v_ic_inf": cramer_v_ic_inf,
        "cramer_v_ic_sup": cramer_v_ic_sup,
        "passed": passed,
        "total": total,
        "coverage_percent": coverage_percent,
        "power_n": power_n,
    }


if __name__ == "__main__":
    import leer_datos

    datos = leer_datos.cargar_datos()
    procesado = procesar(datos)
    print(f"chi-cuadrado: {procesado['statistic']:.4f}")
    print(f"p (permutación): {procesado['p_value']:.6f}")
    print(f"V de Cramér: {procesado['cramer_v']:.4f}")
    print(f"cobertura RF Must: {procesado['passed']}/{procesado['total']}")
    print("Procesamiento OK.")
