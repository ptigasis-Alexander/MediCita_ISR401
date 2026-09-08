<div align="center">

# 📋 instrumentos/ — Reubicado

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Reubicado-informational?style=for-the-badge)
![Redirección](https://img.shields.io/badge/Ver_en-07__Datos%2Fdatos__crudos-blue?style=for-the-badge)

</div>

---

## 📌 Qué pasó con esta carpeta

Esta carpeta estaba destinada originalmente a los instrumentos de recolección de datos del componente empírico (ficha de observación, manifiesto de transcripciones, etc.).

Con la **Guía de Desarrollo del 02/09/2026**, el proyecto adoptó una nueva numeración de carpetas para el paquete de datos (Sección 7 de la guía), que exige una estructura específica con `datos_crudos/`, `datos_procesados/`, `resultados/` y `scripts/`. Los instrumentos de recolección, al ser datos sin procesar, quedaron reubicados dentro de esa nueva estructura en vez de permanecer aquí.

## 📂 Dónde están ahora los archivos reales

| Instrumento | Ubicación actual |
|---|---|
| `ficha_observacion.csv` | [`07_Datos/datos_crudos/ficha_observacion.csv`](../../07_Datos/datos_crudos/ficha_observacion.csv) |
| `manifest_transcripciones_validacion.csv` | [`07_Datos/datos_crudos/manifest_transcripciones_validacion.csv`](../../07_Datos/datos_crudos/manifest_transcripciones_validacion.csv) |

## ✅ Por qué esta carpeta se conserva (vacía) en vez de eliminarse

Se mantiene la carpeta `06_Experimento/instrumentos/` como referencia de la estructura original del componente empírico, con esta nota explicando la reubicación — para que nadie que la encuentre piense que el instrumento se perdió o nunca existió.

**Para ver los instrumentos reales, ve a [`07_Datos/datos_crudos/`](../../07_Datos/datos_crudos/README.md).**
