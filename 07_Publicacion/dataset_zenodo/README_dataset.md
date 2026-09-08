<div align="center">

# 📦 Dataset de Replicación — MediCita

### Proyecto MediCita (SICM) — ISR-401

![Licencia](https://img.shields.io/badge/Licencia-CC_BY_4.0-success?style=for-the-badge)
![Zenodo](https://img.shields.io/badge/Zenodo-v1.0.0_(01/09/2026)-003366?style=for-the-badge)
![Cobertura](https://img.shields.io/badge/RF_Must-90.91%25-blue?style=for-the-badge)

</div>

---

## 📌 Nota de versión

Este README describe **exactamente** el contenido depositado en Zenodo (DOI 10.5281/zenodo.22236373, v1.0.0, 01/09/2026). El repositorio de GitHub ha avanzado desde esa fecha (RNF-19/20, Kappa, member checking, 16 participantes confirmados), pero **se decidió mantener esta versión de Zenodo como la definitiva** — no se publicará una v2. Para el estado más reciente de esos temas, ver el README principal del repositorio y `10_Autoria/`.

---

## 📋 Contenido

| Archivo | Descripción |
|---|---|
| `observaciones_validacion_procesadas.csv` | 46 observaciones derivadas de la evidencia de validación disponible. |
| `observacion_requisito_long.csv` | 72 relaciones normalizadas entre observaciones y requisitos. |
| `resumen_descriptivo.csv` | Conteos regenerables de estados, áreas y requisitos. |
| `cobertura_RF_Must_final.csv` | Matriz de cierre técnico de los 22 RF Must. |
| `verificacion_tecnica_RF_Must.json` | Salida de la verificación técnica reproducible del MVP. |
| `resultados_estadisticos.json` | Prueba de permutación Monte Carlo (χ²=1,9921, V de Cramér=0,1663, p=0,4131) y cálculo de potencia, regenerables con `run_all.py`. |
| `run_all_output.json` | Salida íntegra de la última ejecución del script anterior, para verificación de reproducibilidad. |

---

## 📅 Alcance temporal del corte

Primera ronda: 8 entrevistas de levantamiento realizadas. Segunda ronda: 10 sesiones de validación con transcripción disponible (incluye Psicología y el paciente simulado 02). Ninguna sesión queda pendiente en este corte.

## 📊 Resultado técnico reproducible

Cobertura de RF Must: **20/22 = 90,91%**. Este porcentaje es cobertura técnica del MVP y no representa satisfacción, SUS ni aprobación de participantes.

De las 46 observaciones: 39 completadas con observación de mejora, 5 no completadas, 2 completadas sin observaciones.

## ♻️ Reutilización

El conjunto está preparado para licencia **CC BY 4.0**.

## 🔒 Exclusiones

No contiene audio, video, consentimientos firmados, identificadores directos ni la clave de reidentificación.
