#!/usr/bin/env python3
"""Calcula el coeficiente de acuerdo (Cohen's Kappa) entre las dos
observaciones independientes de las sesiones de validación
VAL-MG y VAL-ENF (20% de las 8 sesiones de validación), con su
intervalo de confianza del 95%.

Compara la columna 'estado_tarea' de cada observador para cada
id_registro — es el juicio categórico que decide si la tarea del
walkthrough se completó, se completó con observación, o no se
completó, y es lo que la rúbrica pide medir como acuerdo entre
observadores.

Uso:
    python calcular_kappa_observacion.py

Requiere en la misma carpeta:
    hoja_OBSERVADOR_1_VAL-MG_VAL-ENF.csv       (ya completa — es la
        ficha original tal como quedó registrada en campo)
    hoja_OBSERVADOR_2_PLANTILLA_VAL-MG_VAL-ENF.csv  (debe completarse
        primero: un segundo integrante ve los videos de esas 10
        interacciones SIN ver la hoja del observador 1, y llena
        'estado_tarea', 'dificultad_incidente' y
        'observacion_investigador' de forma independiente)

Este script NO genera datos: si la plantilla del observador 2 sigue
vacía, se detiene con un error explicando qué falta.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
HOJA_1 = CARPETA / "hoja_OBSERVADOR_1_VAL-MG_VAL-ENF.csv"
HOJA_2 = CARPETA / "hoja_OBSERVADOR_2_PLANTILLA_VAL-MG_VAL-ENF.csv"


def leer_juicios(ruta: Path) -> dict[str, str]:
    juicios = {}
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        primera_linea = f.readline()
        delimitador = ";" if primera_linea.count(";") > primera_linea.count(",") else ","
        f.seek(0)
        reader = csv.DictReader(f, delimiter=delimitador)
        for fila in reader:
            rid = fila["id_registro"]
            estado = fila["estado_tarea"].strip()
            if not estado:
                raise ValueError(
                    f"Falta llenar 'estado_tarea' para {rid} en {ruta.name}. "
                    "El segundo observador debe ver el video y juzgar cada "
                    "interacción de forma independiente antes de calcular el Kappa."
                )
            juicios[rid] = estado
    return juicios


def cohen_kappa(a: dict[str, str], b: dict[str, str]) -> tuple[float, int]:
    ids = sorted(a.keys())
    if set(ids) != set(b.keys()):
        raise ValueError("Las dos hojas no tienen exactamente los mismos id_registro.")

    n = len(ids)
    acuerdos = sum(1 for i in ids if a[i] == b[i])
    po = acuerdos / n

    categorias = sorted(set(a.values()) | set(b.values()))
    pe = 0.0
    for cat in categorias:
        pa = sum(1 for i in ids if a[i] == cat) / n
        pb = sum(1 for i in ids if b[i] == cat) / n
        pe += pa * pb

    kappa = 1.0 if pe == 1.0 else (po - pe) / (1 - pe)
    return kappa, n


def intervalo_confianza_kappa(kappa: float, n: int) -> tuple[float, float]:
    se = math.sqrt((1 - kappa) / n) if kappa < 1 else 0.0
    z = 1.96  # 95% de confianza
    return (round(kappa - z * se, 4), round(kappa + z * se, 4))


def main() -> None:
    juicios_1 = leer_juicios(HOJA_1)
    juicios_2 = leer_juicios(HOJA_2)

    kappa, n = cohen_kappa(juicios_1, juicios_2)
    ic_bajo, ic_alto = intervalo_confianza_kappa(kappa, n)

    interpretacion = (
        "sin acuerdo" if kappa < 0 else
        "leve" if kappa < 0.20 else
        "aceptable" if kappa < 0.40 else
        "moderado" if kappa < 0.60 else
        "sustancial" if kappa < 0.80 else
        "casi perfecto"
    )

    print(f"Interacciones observadas: {n} (sesiones VAL-MG y VAL-ENF, 20% de 8)")
    print(f"Cohen's Kappa: {kappa:.4f}")
    print(f"Intervalo de confianza 95%: [{ic_bajo}, {ic_alto}]")
    print(f"Interpretación (Landis & Koch, 1977): {interpretacion}")

    with open(CARPETA / "resultado_kappa_observacion.md", "w", encoding="utf-8") as out:
        out.write("# Resultado de la Doble Observación Independiente (B4)\n\n")
        out.write("- **Sesiones cubiertas:** VAL-MG, VAL-ENF (2 de 8 = 25% de las sesiones "
                   "de validación, cumple el mínimo del 20%)\n")
        out.write(f"- **Interacciones observadas:** {n}\n")
        out.write(f"- **Cohen's Kappa:** {kappa:.4f}\n")
        out.write(f"- **Intervalo de confianza 95%:** [{ic_bajo}, {ic_alto}]\n")
        out.write(f"- **Interpretación:** {interpretacion} (escala de Landis & Koch, 1977)\n")
        out.write("- **Generado por:** `calcular_kappa_observacion.py` "
                   "(reproducible, no calculado a mano)\n")

    print("\nResultado guardado en resultado_kappa_observacion.md")


if __name__ == "__main__":
    main()
