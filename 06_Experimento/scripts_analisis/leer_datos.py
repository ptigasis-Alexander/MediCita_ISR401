#!/usr/bin/env python3
"""Etapa 1 de 3 — Lectura y validación de datos.

Abre los CSV de datos procesados que alimentan el análisis cuantitativo de
MediCita (observaciones de validación, relaciones observación-requisito, y
cobertura de RF Must), y valida que las columnas esperadas estén presentes
antes de pasarlos a la etapa de procesamiento.

No transforma ni calcula nada — esa es responsabilidad de procesar_datos.py.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "07_Datos" / "datos_procesados"
RESULTS = ROOT / "07_Datos" / "resultados"

# Columnas mínimas que cada archivo debe tener para que el resto del
# pipeline funcione correctamente. Si falta alguna, se detiene aquí en vez
# de fallar más adelante con un error críptico.
COLUMNAS_REQUERIDAS = {
    "observaciones_validacion_procesadas.csv": {"codigo_sesion", "estado_tarea"},
    "observacion_requisito_long.csv": {"area", "estado_tarea"},
}


def read_semicolon(name: str) -> list[dict[str, str]]:
    """Lee un CSV delimitado por punto y coma desde datos_procesados/."""
    path = DATA / name
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter=";"))
    if name in COLUMNAS_REQUERIDAS:
        faltantes = COLUMNAS_REQUERIDAS[name] - set(rows[0].keys() if rows else [])
        if faltantes:
            raise ValueError(f"{name}: faltan columnas obligatorias {faltantes}")
    if not rows:
        raise ValueError(f"{name}: el archivo no tiene registros")
    return rows


def read_coverage() -> list[dict[str, str]]:
    """Lee la cobertura de RF Must desde 07_Datos/resultados/."""
    path = RESULTS / "cobertura_RF_Must_final.csv"
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter=";"))
    if not rows:
        raise ValueError("cobertura_RF_Must_final.csv: el archivo no tiene registros")
    return rows


def cargar_datos() -> dict[str, list[dict[str, str]]]:
    """Carga y valida los tres insumos crudos del análisis.

    Devuelve un diccionario con las tres listas de registros, listas para
    que procesar_datos.py las transforme.
    """
    return {
        "observations": read_semicolon("observaciones_validacion_procesadas.csv"),
        "relations": read_semicolon("observacion_requisito_long.csv"),
        "coverage": read_coverage(),
    }


if __name__ == "__main__":
    datos = cargar_datos()
    print(f"observaciones: {len(datos['observations'])} filas")
    print(f"relaciones: {len(datos['relations'])} filas")
    print(f"cobertura RF Must: {len(datos['coverage'])} filas")
    print("Lectura y validación OK.")
