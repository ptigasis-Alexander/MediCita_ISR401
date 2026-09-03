#!/usr/bin/env python3
"""Orquestador único de 07_Datos/.

Este script NO reimplementa el análisis: ejecuta el pipeline real que ya
existe en 06_Experimento/scripts_analisis/run_all.py (rutas verificadas y
usadas por el manuscrito) y luego sincroniza sus salidas hacia
07_Datos/datos_procesados/ y 07_Datos/resultados/, para que ambas copias
queden siempre generadas por el mismo código, sin edición manual.

Uso (desde la raíz del repositorio):
    python 07_Datos/scripts/generar_paquete_datos.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIPELINE_REAL = ROOT / "06_Experimento" / "scripts_analisis" / "run_all.py"

FUENTE_PROCESADOS = ROOT / "06_Experimento" / "datos_procesados"
FUENTE_RESULTADOS = ROOT / "06_Experimento" / "resultados"

DESTINO_CRUDOS = ROOT / "07_Datos" / "datos_crudos"
DESTINO_PROCESADOS = ROOT / "07_Datos" / "datos_procesados"
DESTINO_RESULTADOS = ROOT / "07_Datos" / "resultados"

ARCHIVOS_CRUDOS = [
    (ROOT / "06_Experimento" / "instrumentos" / "ficha_observacion.csv", DESTINO_CRUDOS),
    (ROOT / "06_Experimento" / "datos_crudos" / "manifest_transcripciones_validacion.csv", DESTINO_CRUDOS),
]

ARCHIVOS_PROCESADOS = [
    "observacion_requisito_long.csv",
    "observaciones_validacion_procesadas.csv",
    "resumen_descriptivo.csv",
]

ARCHIVOS_RESULTADOS = [
    "cobertura_RF_Must_final.csv",
    "resultados_estadisticos.json",
    "run_all_output.json",
    "verificacion_tecnica_RF_Must.json",
    "trazabilidad_observacion_correccion.csv",
    "power_calculation.csv",
    "power_calculation_justificacion.md",
]


def ejecutar_pipeline_real() -> None:
    print(f"Ejecutando pipeline real: {PIPELINE_REAL}")
    resultado = subprocess.run([sys.executable, str(PIPELINE_REAL)], cwd=ROOT)
    if resultado.returncode != 0:
        raise SystemExit(
            "El pipeline real (06_Experimento/scripts_analisis/run_all.py) "
            "falló. Corríjalo antes de regenerar 07_Datos/."
        )


def sincronizar() -> None:
    DESTINO_CRUDOS.mkdir(parents=True, exist_ok=True)
    DESTINO_PROCESADOS.mkdir(parents=True, exist_ok=True)
    DESTINO_RESULTADOS.mkdir(parents=True, exist_ok=True)

    for origen, destino_dir in ARCHIVOS_CRUDOS:
        shutil.copy2(origen, destino_dir / origen.name)
        print(f"  crudo:      {origen.name}")

    for nombre in ARCHIVOS_PROCESADOS:
        shutil.copy2(FUENTE_PROCESADOS / nombre, DESTINO_PROCESADOS / nombre)
        print(f"  procesado:  {nombre}")

    for nombre in ARCHIVOS_RESULTADOS:
        origen = FUENTE_RESULTADOS / nombre
        if origen.exists():
            shutil.copy2(origen, DESTINO_RESULTADOS / nombre)
            print(f"  resultado:  {nombre}")


def main() -> None:
    ejecutar_pipeline_real()
    sincronizar()
    print("\n07_Datos/ regenerado a partir del pipeline real de 06_Experimento.")


if __name__ == "__main__":
    main()
