#!/usr/bin/env python3
"""Orquestador único del análisis cuantitativo de MediCita.

Importa y ejecuta, en orden, las tres etapas del pipeline:

    1. leer_datos.py        — lee y valida los CSV de entrada
    2. procesar_datos.py    — clasifica y calcula (chi-cuadrado, permutación
                               Monte Carlo, bootstrap de V de Cramér,
                               cobertura de RF Must, cálculo de potencia)
    3. generar_resultados.py — escribe el JSON, los CSV y las figuras finales

Este archivo no contiene ninguna lógica de lectura, cálculo ni escritura
propia: solo coordina el orden de ejecución de las tres etapas.

Uso: python run_all.py
"""

from __future__ import annotations

import json

import generar_resultados
import leer_datos
import procesar_datos


def main() -> None:
    datos = leer_datos.cargar_datos()
    procesado = procesar_datos.procesar(datos)
    resultado = generar_resultados.generar(procesado)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
