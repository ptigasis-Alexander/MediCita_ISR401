#!/usr/bin/env python3
"""Etapa 1 de 3 - Lectura y validacion de datos.

Arranca desde el dato realmente crudo (07_Datos/datos_crudos/
ficha_observacion.csv), lo transforma en los dos archivos "procesados"
mediante generar_procesados.py, y luego los lee y valida junto con la
cobertura de RF Must, antes de pasarlos a la etapa de procesamiento.

No calcula estadisticas ni clasifica nada - eso es responsabilidad de
procesar_datos.py.
"""

from __future__ import annotations

import csv
from pathlib import Path

import generar_procesados

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "07_Datos" / "datos_procesados"
RESULTS = ROOT / "07_Datos" / "resultados"

# Columnas minimas que cada archivo debe tener para que el resto del
# pipeline funcione correctamente. Si falta alguna, se detiene aqui en vez
# de fallar mas adelante con un error criptico.
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
    """Regenera los procesados desde el crudo, los lee y los valida.

    Devuelve un diccionario con las tres listas de registros, listas para
    que procesar_datos.py las transforme.
    """
    generar_procesados.generar()
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
    print("Lectura y validacion OK.")
