#!/usr/bin/env python3
"""Calcula el coeficiente de acuerdo (Cohen's Kappa) entre las dos
hojas de codificación independiente de 10_Autoria/doble_codificacion/,
con su intervalo de confianza del 95%.

Uso:
    python calcular_kappa.py

Requiere: hoja_CODIFICADOR_A.csv y hoja_CODIFICADOR_B.csv en la misma
carpeta, ambas completas (columna codigo_asignado llena en todas las
filas).
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
HOJA_A = CARPETA / "hoja_CODIFICADOR_A.csv"
HOJA_B = CARPETA / "hoja_CODIFICADOR_B.csv"


def leer_codigos(ruta: Path) -> dict[str, str]:
    codigos = {}
    with open(ruta, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for fila in reader:
            sid = fila["id_segmento"]
            codigo = fila["codigo_asignado (C01-C49, ver referencia)"].strip()
            if not codigo:
                raise ValueError(
                    f"Falta codificar el segmento {sid} en {ruta.name}. "
                    "Completa TODAS las filas antes de calcular el Kappa."
                )
            # si asignaron varios códigos separados por coma, usar solo el primero
            # para el cálculo de acuerdo simple (declarar esto en el reporte)
            codigos[sid] = codigo.split(",")[0].strip()
    return codigos


def cohen_kappa(a: dict[str, str], b: dict[str, str]) -> tuple[float, int]:
    ids = sorted(a.keys())
    if set(ids) != set(b.keys()):
        raise ValueError("Las dos hojas no tienen exactamente los mismos segmentos.")

    n = len(ids)
    acuerdos = sum(1 for i in ids if a[i] == b[i])
    po = acuerdos / n

    categorias = sorted(set(a.values()) | set(b.values()))
    pe = 0.0
    for cat in categorias:
        pa = sum(1 for i in ids if a[i] == cat) / n
        pb = sum(1 for i in ids if b[i] == cat) / n
        pe += pa * pb

    if pe == 1.0:
        kappa = 1.0
    else:
        kappa = (po - pe) / (1 - pe)

    return kappa, n


def intervalo_confianza_kappa(kappa: float, n: int, nivel: float = 0.95) -> tuple[float, float]:
    # Aproximación estándar del error estándar de Kappa (Fleiss, 1981)
    se = math.sqrt((1 - kappa) / n) if kappa < 1 else 0.0
    z = 1.96  # para 95% de confianza
    return (round(kappa - z * se, 4), round(kappa + z * se, 4))


def main() -> None:
    codigos_a = leer_codigos(HOJA_A)
    codigos_b = leer_codigos(HOJA_B)

    kappa, n = cohen_kappa(codigos_a, codigos_b)
    ic_bajo, ic_alto = intervalo_confianza_kappa(kappa, n)

    print(f"Segmentos codificados: {n}")
    print(f"Cohen's Kappa: {kappa:.4f}")
    print(f"Intervalo de confianza 95%: [{ic_bajo}, {ic_alto}]")

    interpretacion = (
        "sin acuerdo" if kappa < 0 else
        "leve" if kappa < 0.20 else
        "aceptable" if kappa < 0.40 else
        "moderado" if kappa < 0.60 else
        "sustancial" if kappa < 0.80 else
        "casi perfecto"
    )
    print(f"Interpretación (escala de Landis & Koch, 1977): {interpretacion}")

    with open(CARPETA / "resultado_kappa.md", "w", encoding="utf-8") as out:
        out.write("# Resultado de la Doble Codificación (A7)\n\n")
        out.write(f"- **Segmentos codificados:** {n}\n")
        out.write(f"- **Cohen's Kappa:** {kappa:.4f}\n")
        out.write(f"- **Intervalo de confianza 95%:** [{ic_bajo}, {ic_alto}]\n")
        out.write(f"- **Interpretación:** {interpretacion} (escala de Landis & Koch, 1977)\n")
        out.write(f"- **Generado por:** `calcular_kappa.py` (reproducible, no calculado a mano)\n")

    print("\nResultado guardado en resultado_kappa.md")


if __name__ == "__main__":
    main()
