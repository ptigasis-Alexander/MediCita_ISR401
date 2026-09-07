
<div align="center">

# 👤 A10 — Aporte Individual por Integrante

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-En_progreso-yellow?style=for-the-badge)
![Fuente](https://img.shields.io/badge/Fuente-git_log_%2B_bitácora_A1-informational?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-07/09/2026-blue?style=for-the-badge)

</div>

---

## 📌 Metodología

Este documento se construyó cruzando dos fuentes verificables:
1. **Conteo de commits** por integrante (`git shortlog -sne HEAD`, con `.mailmap` aplicado).
2. **Bitácora de sesiones** (`10_Autoria/bitacora_sesiones.csv`), que ya registra en qué días participó cada quien y qué se decidió/hizo ese día, con base en los mensajes reales de commit.

## ⚠️ Alcance de los 19 días registrados

Los 19 días de la bitácora **cubren la totalidad del historial del repositorio**: desde el primer commit (21/07/2026) hasta el más reciente (06/09/2026). No es una muestra — es cada día distinto en el que hubo al menos un commit, sin excepciones.

## ⚠️ Importante: "días de participación" no equivale a "volumen de trabajo"

La tabla de abajo cuenta en cuántas fechas distintas aparece cada integrante, **no cuántos commits hizo**. Esto puede ser engañoso: por ejemplo, el 31/08/2026 concentró **597 commits en un solo día**, con los 5 integrantes participando. Una persona pudo haber generado un volumen de trabajo muy alto en pocos días concentrados, y aparecer con un número de "días" menor que alguien que participó de forma más distribuida pero con menos commits por sesión. **El indicador principal de aporte individual es el conteo total de commits (tabla siguiente, pendiente de confirmar), no la cantidad de días.**

## ⚠️ Nota sobre el conteo total de commits

El número total de commits varía según se consulte desde un clon completo o uno superficial. **El número de referencia** debe tomarse de:
```bash
git shortlog -sne HEAD
```
ejecutado sobre un clon completo del repositorio. *(Pendiente de confirmación final con el resultado de ese comando.)*

---

## 📊 Resumen cuantitativo

| Integrante | Días con participación registrada (bitácora A1) |
|---|---:|
| Paul Alexander Tigasi Sampedro | 17 de 19 |
| Jamileth Estefanía Gamarra Zárate | 11 de 19 |
| Thais Melanie Herrera Ramos | 11 de 19 |
| Steven Santiago Díaz Pontón | 9 de 19 |
| Mayummy Jailly Trujillo Vega | 9 de 19 |

---

## 📝 Detalle cualitativo por integrante

### Paul Alexander Tigasi Sampedro (líder de equipo)

**Participación:** 17 de los 19 días registrados en la bitácora — la más alta del equipo.

**Aporte narrativo:** Carga inicial de fotografías del entorno; organización de la estructura de `02_Evidencias`; consolidación del ERS 2A; creación de guías de verificación de codificación temática y transcripciones; participó en la jornada de anonimización del 31/08; lideró la corrección final del repositorio en la Entrega 4 (2B): migración de evidencia audiovisual a GitHub Release, renombrado de scripts, construcción de `07_Datos/`, eliminación de `PE5_U5`, `.mailmap`, y documentación de `10_Autoria/`.

**Commits que lo acreditan:** ver columna `commits_producidos` de `bitacora_sesiones.csv`, filas 2026-07-21 a 2026-09-06 donde aparece `ptigasis-Alexander`.

---

### Steven Santiago Díaz Pontón

**Participación:** 9 de 19 días.

**Aporte narrativo:** Carga y organización de fotografías de entorno; creación de mockups de interfaz; trabajo en la práctica independiente PE5 (Unidad V); participó en la jornada de anonimización del 31/08; corrección de rutas de diagramas UML y renombrado de fotos con metadatos EXIF (04/09); registro de datos de Member Checking (06/09).

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `DIAZ PONTON STEVEN`.

---

### Jamileth Estefanía Gamarra Zárate

**Participación:** 11 de 19 días.

**Aporte narrativo:** Organización de fotos de entorno; limpieza de transcripciones duplicadas; incorporación de ORCID de los 5 integrantes en `CITATION.cff`; reorganización estructural de `02_Evidencias`; creación de mockups; trabajo en práctica PE5; participó en la jornada de anonimización; corrección de rutas de diagramas y fotos (04/09); actualización de `02_Evidencias`, `00_Restringido` y `Capturas` (05/09) — incluye la corrección del número de oficio (059→069) y la sesión de facilitación del Member Checking.

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `Jami1405`.

---

### Thais Melanie Herrera Ramos

**Participación:** 11 de 19 días *(incluye los 8 commits atribuidos vía `.mailmap` desde la identidad `MediCita Team`, del 18-19/08)*.

**Aporte narrativo:** Limpieza de transcripciones y actualización de `CITATION.cff`; reorganización de `02_Evidencias`; creación de mockups; trabajo en las dos prácticas independientes PE5 (18-21/08); participó en la jornada de anonimización del 31/08; actualización de documentación (05/09); registro y facilitación de la sesión de Member Checking (06/09).

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `Thais Melanie Herrera Ramos`.

**Nota de atribución:** incluye 8 commits (18-19/08/2026) originalmente registrados bajo la identidad genérica `MediCita Team <team@medicita.local>` sobre la carpeta de práctica `PE5_U5_PFC_DIAZ_TIGASI_VERA/` (ya eliminada del repositorio), atribuidos mediante `.mailmap` el 03/09/2026.

---

### Mayummy Jailly Trujillo Vega

**Participación:** 9 de 19 días.

**Aporte narrativo:** Organización de fotos de entorno; reorganización de `02_Evidencias`; creación de mockups; trabajo en la práctica PE5 (Unidad V); participó en la jornada de anonimización del 31/08; actualización de documentación (05/09); registro de datos de Member Checking (06/09).

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `mtrujillov-sys`.

---

## 🔍 Nota metodológica

El reparto de participación por días es razonablemente parejo entre los cinco integrantes (9 a 17 de 19 días), consistente con lo ya señalado en el informe individual del docente: *"El reparto de confirmaciones en la ventana es notablemente parejo entre los cinco integrantes."* Paul Alexander Tigasi Sampedro, como líder de equipo, presenta la mayor participación por haber coordinado directamente la corrección final del repositorio en la Entrega 4 (2B).

---

## ✍️ Firma de los integrantes

Al firmar, cada integrante confirma que la información de este documento es correcta según su propio conocimiento, y corrige cualquier atribución que no le correspondiera.

| Integrante | Firma | Fecha |
|---|---|---|
| Paul Alexander Tigasi Sampedro | | |
| Steven Santiago Díaz Pontón |Steven Diaz | 07/09/2026 0:16 |
| Jamileth Estefanía Gamarra Zárate | | |
| Thais Melanie Herrera Ramos | | |
| Mayummy Jailly Trujillo Vega | | |
