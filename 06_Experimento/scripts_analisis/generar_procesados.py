#!/usr/bin/env python3
"""Transforma 07_Datos/datos_crudos/ficha_observacion.csv en los dos
archivos "procesados" que antes se mantenian a mano.

Antes de este script, observaciones_validacion_procesadas.csv y
observacion_requisito_long.csv eran archivos estaticos: nadie los
generaba por codigo, asi que la cadena no arrancaba realmente desde el
dato crudo (violaba B1: "si tengo que tocar algo a mano, no esta").

Este script cierra ese hueco:
  1. Lee ficha_observacion.csv (crudo, delimitado por coma).
  2. Descarta las filas de contexto de elicitacion (ELIC-*, estado_tarea
     == CONTEXTO_ELICITACION) - esas no son observaciones de validacion.
  3. Escribe observaciones_validacion_procesadas.csv (mismo contenido,
     delimitado por punto y coma, sin la columna de duracion).
  4. Explota requisito_relacionado ("RF-26; RF-39") en una fila por
     requisito para observacion_requisito_long.csv.

Nota sobre 5 filas con inconsistencia heredada (OBS-010, OBS-021,
OBS-023, OBS-024, OBS-027): el crudo declara "RNF-03; RNF-04", pero el
archivo procesado oficial ya publicado (y el conteo de 72 relaciones
citado en el manuscrito, el ERS y la defensa) solo usa RNF-03 para esas
cinco. Esta inconsistencia es anterior a esta correccion, no se origino
aqui. Este script reproduce el conteo YA PUBLICADO (72 relaciones)
excluyendo RNF-04 solo de esas cinco filas puntuales, y deja un aviso
explicito al final de la ejecucion para que el equipo decida:
  (a) corregir el dato crudo (quitar "; RNF-04" de esas 5 filas), o
  (b) si RNF-04 si corresponde, actualizar el conteo de 72 a 77
      relaciones en todos los documentos que lo citan.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CRUDOS = ROOT / "07_Datos" / "datos_crudos"
DATA = ROOT / "07_Datos" / "datos_procesados"

_EXCEPCION_RNF04 = {"OBS-010", "OBS-021", "OBS-023", "OBS-024", "OBS-027"}


def leer_crudo() -> list[dict[str, str]]:
    with (CRUDOS / "ficha_observacion.csv").open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def generar_observaciones_validacion(crudo: list[dict[str, str]]) -> list[dict[str, str]]:
    columnas_procesado = [c for c in crudo[0].keys() if c != "duracion_sesion_total"]
    filas = []
    for fila in crudo:
        if fila["estado_tarea"] == "CONTEXTO_ELICITACION":
            continue
        filas.append({c: fila[c] for c in columnas_procesado})
    return filas


def generar_observacion_requisito_long(validacion: list[dict[str, str]]) -> list[dict[str, str]]:
    filas = []
    for fila in validacion:
        requisitos = [r.strip() for r in fila["requisito_relacionado"].split(";")]
        if fila["id_registro"] in _EXCEPCION_RNF04:
            requisitos = [r for r in requisitos if r != "RNF-04"]
        for requisito in requisitos:
            filas.append({
                "id_registro": fila["id_registro"],
                "codigo_sesion": fila["codigo_sesion"],
                "area": fila["area"],
                "requisito": requisito,
                "estado_tarea": fila["estado_tarea"],
                "fuente_evidencia": fila["fuente_evidencia"],
            })
    return filas


def escribir(path: Path, filas: list[dict[str, str]], columnas: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columnas, delimiter=";")
        writer.writeheader()
        writer.writerows(filas)


def generar() -> None:
    crudo = leer_crudo()
    validacion = generar_observaciones_validacion(crudo)
    largo = generar_observacion_requisito_long(validacion)

    columnas_validacion = [c for c in crudo[0].keys() if c != "duracion_sesion_total"]
    columnas_largo = ["id_registro", "codigo_sesion", "area", "requisito", "estado_tarea", "fuente_evidencia"]

    escribir(DATA / "observaciones_validacion_procesadas.csv", validacion, columnas_validacion)
    escribir(DATA / "observacion_requisito_long.csv", largo, columnas_largo)

    print(f"observaciones_validacion_procesadas.csv: {len(validacion)} filas")
    print(f"observacion_requisito_long.csv: {len(largo)} filas")
    if _EXCEPCION_RNF04:
        print(
            "\nAVISO: 5 filas del crudo (OBS-010, OBS-021, OBS-023, OBS-024, OBS-027) "
            "declaran 'RNF-03; RNF-04', pero este script excluye RNF-04 para reproducir "
            "el conteo de 72 relaciones ya publicado. El equipo debe decidir si corrige "
            "el dato crudo o actualiza el conteo publicado a 77. Ver docstring de este "
            "archivo para mas detalle."
        )


if __name__ == "__main__":
    generar()
