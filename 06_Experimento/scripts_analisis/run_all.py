#!/usr/bin/env python3
"""Regenera los resultados cuantitativos publicables de MediCita.

Usa exclusivamente los CSV anonimizados del paquete. La prueba de permutación
emplea 100 000 réplicas y semilla 42, tal como declara el manuscrito.
"""

from __future__ import annotations

import csv
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.stats import nct, t


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "07_Datos" / "datos_procesados"
RESULTS = ROOT / "07_Datos" / "resultados"
FIGURES = ROOT / "07_Publicacion" / "figuras"
TABLES = ROOT / "07_Publicacion" / "tablas"
ZENODO = ROOT / "07_Publicacion" / "dataset_zenodo"


def read_semicolon(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream, delimiter=";"))


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


def write_csv(path: Path, rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        csv.writer(stream, delimiter=";").writerows(rows)


def main() -> None:
    observations = read_semicolon("observaciones_validacion_procesadas.csv")
    relations = read_semicolon("observacion_requisito_long.csv")
    states = Counter(row["estado_tarea"] for row in observations)

    group_order = ["Clínico", "Administrativo", "Paciente simulado"]
    grouped = defaultdict(lambda: [0, 0])
    for row in relations:
        finding = row["estado_tarea"] != "COMPLETADA"
        grouped[group_area(row["area"])][int(finding)] += 1
    contingency = [grouped[group] for group in group_order]
    statistic, expected_min, cramer_v = chi_square(contingency)
    p_value = monte_carlo(contingency, statistic)

    coverage_path = RESULTS / "cobertura_RF_Must_final.csv"
    with coverage_path.open(encoding="utf-8-sig", newline="") as stream:
        coverage = list(csv.DictReader(stream, delimiter=";"))
    status_field = "Estado_C3" if "Estado_C3" in coverage[0] else next(
        field for field in coverage[0] if "estado" in field.lower()
    )
    passed = sum(row[status_field].strip().upper() in {"PASA", "APROBADO", "CERRADO"} for row in coverage)
    total = len(coverage)
    coverage_percent = 100 * passed / total
    power_n = two_sample_power_n()

    result = {
        "fuente_observaciones": str((DATA / "observaciones_validacion_procesadas.csv").relative_to(ROOT)),
        "fuente_relaciones": str((DATA / "observacion_requisito_long.csv").relative_to(ROOT)),
        "observaciones": len(observations),
        "relaciones_observacion_requisito": len(relations),
        "estados_observacion": dict(states),
        "grupos_tabla_3x2": group_order,
        "tabla_sin_hallazgo_con_hallazgo": contingency,
        "chi_cuadrado": round(statistic, 6),
        "frecuencia_esperada_minima": round(expected_min, 6),
        "replicas_monte_carlo": 100_000,
        "semilla": 42,
        "p_permutacion": round(p_value, 6),
        "v_cramer": round(cramer_v, 6),
        "rf_must_aprobados": passed,
        "rf_must_total": total,
        "cobertura_rf_must_porcentaje": round(coverage_percent, 2),
        "power_calculation": {
            "prueba": "t bilateral de dos muestras independientes, grupos iguales",
            "cohen_d": 0.5,
            "alpha": 0.05,
            "potencia": 0.80,
            "n_requerido_por_grupo": power_n,
            "n_total_requerido": 2 * power_n,
            "nota": "Cálculo de referencia; no convierte las sesiones disponibles en una muestra suficiente.",
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "resultados_estadisticos.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    summary_rows = [
        ["metrica", "valor"],
        ["sesiones_validacion_con_transcripcion", len({row["codigo_sesion"] for row in observations})],
        ["observaciones_totales", len(observations)],
        ["completada_con_observacion", states["COMPLETADA_CON_OBSERVACION"]],
        ["no_completada", states["NO_COMPLETADA"]],
        ["completada", states["COMPLETADA"]],
        ["relaciones_observacion_requisito", len(relations)],
        ["p_permutacion_monte_carlo", f"{p_value:.6f}"],
        ["v_cramer", f"{cramer_v:.6f}"],
        ["rf_must_verificacion_tecnica_aprobados", passed],
        ["rf_must_total", total],
        ["cobertura_rf_must_porcentaje", f"{coverage_percent:.2f}"],
    ]
    for destination in [DATA / "resumen_descriptivo.csv", ZENODO / "resumen_descriptivo.csv"]:
        write_csv(destination, summary_rows)

    write_csv(
        TABLES / "resumen_validacion.csv",
        [["estado", "conteo"], ["Completada", states["COMPLETADA"]],
         ["Completada con observación", states["COMPLETADA_CON_OBSERVACION"]],
         ["No completada", states["NO_COMPLETADA"]]],
    )
    write_csv(
        RESULTS / "power_calculation.csv",
        [["cohen_d", "alpha", "potencia", "n_por_grupo", "n_total"],
         ["0.5", "0.05", "0.80", power_n, 2 * power_n]],
    )

    FIGURES.mkdir(parents=True, exist_ok=True)
    labels = ["Completada", "Con observación", "No completada"]
    values = [states["COMPLETADA"], states["COMPLETADA_CON_OBSERVACION"], states["NO_COMPLETADA"]]
    plt.figure(figsize=(7.2, 4.2))
    bars = plt.bar(labels, values, color=["#2e7d32", "#f9a825", "#c62828"])
    plt.ylabel("Observaciones")
    plt.title("Estado de las tareas del walkthrough (N=46)")
    plt.bar_label(bars)
    plt.tight_layout()
    plt.savefig(FIGURES / "estado_tareas_validacion.png", dpi=200)
    plt.close()

    plt.figure(figsize=(6.4, 4.0))
    bars = plt.bar(["RF Must cubiertos", "RF Must no cubiertos"], [passed, total - passed],
                   color=["#1565c0", "#b0bec5"])
    plt.ylabel("Requisitos")
    plt.title(f"Cobertura técnica: {passed}/{total} ({coverage_percent:.2f} %)")
    plt.bar_label(bars)
    plt.tight_layout()
    plt.savefig(FIGURES / "cobertura_rf_must.png", dpi=200)
    plt.close()

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
