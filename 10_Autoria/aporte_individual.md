<div align="center">

# 👤 A10 — Aporte Individual por Integrante

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![Fuente](https://img.shields.io/badge/Fuente-git_log_%2B_bitácora_A1-informational?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-08/09/2026-blue?style=for-the-badge)

</div>

---

## 📌 Metodología

Este documento se construyó cruzando dos fuentes verificables:
1. **Conteo de commits** por integrante (`git shortlog -sne HEAD` sobre un clon completo, con `.mailmap` aplicado).
2. **Bitácora de sesiones** (`10_Autoria/bitacora_sesiones.csv`), que registra en qué días participó cada quien y qué se decidió/hizo ese día, con base en los mensajes reales de commit.

## ⚠️ Alcance de los 21 días registrados

Los 21 días de la bitácora **cubren la totalidad del historial del repositorio**: desde el primer commit (21/07/2026) hasta el más reciente (08/09/2026). No es una muestra — es cada día distinto en el que hubo al menos un commit, sin excepciones.

## ⚠️ Importante: "días de participación" no equivale a "volumen de trabajo"

La tabla de días cuenta en cuántas fechas distintas aparece cada integrante, **no cuántos commits hizo**. Esto puede ser engañoso: por ejemplo, el 31/08/2026 concentró **597 commits en un solo día**, con los 5 integrantes participando. El indicador principal de aporte individual es el conteo total de commits (tabla siguiente), no la cantidad de días.

## ✅ Conteo total de commits — confirmado con clon completo (`git shortlog -sne HEAD`)

| Integrante | Commits totales | % del total (1.441) |
|---|---:|---:|
| Paul Alexander Tigasi Sampedro | 298 | 20,68 % |
| Thais Melanie Herrera Ramos | 292 | 20,26 % |
| Steven Santiago Díaz Pontón | 287 | 19,92 % |
| Mayummy Jailly Trujillo Vega | 283 | 19,64 % |
| Jamileth Estefanía Gamarra Zárate | 281 | 19,50 % |
| **Total** | **1.441** | **100 %** |

El reparto es notablemente parejo entre los cinco integrantes (19,50 % a 20,68 %), el rango más estrecho registrado hasta ahora en el proyecto.

## 🔍 Comparación con la vista "Contributors" de GitHub

GitHub ofrece una vista gráfica de commits por integrante en la pestaña "Insights → Contributors" del repositorio. Sus números, al 09/09/2026, no coinciden exactamente con el conteo de `git shortlog`:

| Integrante | GitHub (Insights) | `git shortlog` (clon completo) | Diferencia |
|---|---:|---:|---:|
| Paul Alexander Tigasi Sampedro | 292 | 298 | +6 |
| Thais Melanie Herrera Ramos | 277 | 289 | +12 |
| Steven Santiago Díaz Pontón | 278 | 285 | +7 |
| Mayummy Jailly Trujillo Vega | 278 | 279 | +1 |
| Jamileth Estefanía Gamarra Zárate | 277 | 278 | +1 |
| **Total** | **1.402** | **1.429** | **+27** |

### Por qué existe esta diferencia

1. **GitHub no aplica el `.mailmap` de la misma forma que Git.** El salto más grande (+12 en Thais) corresponde a los 8 commits de la identidad genérica `MediCita Team` que el `.mailmap` atribuye a Thais Melanie Herrera Ramos. `git shortlog` respeta ese archivo automáticamente; la vista de Contributors de GitHub sigue mostrando esa identidad por separado (visible como "Melanie-G23" sin fusionar en algunas capturas), y no refleja la atribución completa.
2. **La vista de GitHub tiene retraso de caché.** Es una analítica que se recalcula periódicamente, no en tiempo real. El resto de la diferencia (+14 repartidos entre los demás integrantes) corresponde a actividad de los días más recientes (07-08/09/2026) que la caché de GitHub todavía no reflejaba al momento de la captura.

### Cuál se usa como fuente oficial en este documento

El conteo de **`git shortlog -sne HEAD` sobre un clon completo (1.411)**, por ser una lectura directa del historial real de Git, sin intermediarios ni caché, y por aplicar correctamente el `.mailmap` ya adoptado por el equipo.

---

## 📊 Resumen cuantitativo secundario (días de participación)

| Integrante | Días con participación registrada (bitácora A1) |
|---|---:|
| Paul Alexander Tigasi Sampedro | 18 de 21 |
| Jamileth Estefanía Gamarra Zárate | 13 de 21 |
| Thais Melanie Herrera Ramos | 13 de 21 |
| Steven Santiago Díaz Pontón | 11 de 21 |
| Mayummy Jailly Trujillo Vega | 11 de 21 |

---

## 📝 Detalle cualitativo por integrante

### Paul Alexander Tigasi Sampedro (líder de equipo)

**Participación:** 18 de los 21 días registrados en la bitácora — la más alta del equipo.

**Aporte narrativo:** Carga inicial de fotografías del entorno; organización de la estructura de `02_Evidencias`; consolidación del ERS 2A; creación de guías de verificación de codificación temática y transcripciones; participó en la jornada de anonimización del 31/08; lideró la corrección final del repositorio en la Entrega 4 (2B): migración de evidencia audiovisual a GitHub Release, renombrado de scripts, construcción de `07_Datos/`, eliminación de `PE5_U5`, `.mailmap`, documentación de `10_Autoria/`, y la corrección final del manuscrito y del guion/presentación de defensa (07/09).

**Commits que lo acreditan:** ver columna `commits_producidos` de `bitacora_sesiones.csv`, filas 2026-07-21 a 2026-09-07 donde aparece `ptigasis-Alexander`.

---

### Steven Santiago Díaz Pontón

**Participación:** 11 de 21 días.

**Aporte narrativo:** Carga y organización de fotografías de entorno; creación de mockups de interfaz; trabajo en la práctica independiente PE5 (Unidad V); participó en la jornada de anonimización del 31/08; corrección de rutas de diagramas UML y renombrado de fotos con metadatos EXIF (04/09); registro de datos de Member Checking (06/09); corrección final del manuscrito y del guion de defensa (07/09); renombrado uniforme de los índices de carpeta a `Readme.md` (08/09).

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `DIAZ PONTON STEVEN`.

---

### Jamileth Estefanía Gamarra Zárate

**Participación:** 13 de 21 días.

**Aporte narrativo:** Organización de fotos de entorno; limpieza de transcripciones duplicadas; incorporación de ORCID de los 5 integrantes en `CITATION.cff`; reorganización estructural de `02_Evidencias`; creación de mockups; trabajo en práctica PE5; participó en la jornada de anonimización; corrección de rutas de diagramas y fotos (04/09); actualización de `02_Evidencias`, `00_Restringido` y `Capturas` (05/09) — incluye la corrección del número de oficio (059→069) y la sesión de facilitación del Member Checking; aclaración de roles de participantes en la validación walkthrough (07/09); renombrado uniforme de índices a `Readme.md` (08/09).

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `Jami1405`.

---

### Thais Melanie Herrera Ramos

**Participación:** 13 de 21 días *(incluye los 8 commits atribuidos vía `.mailmap` desde la identidad `MediCita Team`, del 18-19/08)*.

**Aporte narrativo:** Limpieza de transcripciones y actualización de `CITATION.cff`; reorganización de `02_Evidencias`; creación de mockups; trabajo en las dos prácticas independientes PE5 (18-21/08); participó en la jornada de anonimización del 31/08; actualización de documentación (05/09); registro y facilitación de la sesión de Member Checking (06/09); corrección final del manuscrito y del guion de defensa (07/09); renombrado uniforme de índices a `Readme.md` (08/09).

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `Thais Melanie Herrera Ramos`.

**Nota de atribución:** incluye 8 commits (18-19/08/2026) originalmente registrados bajo la identidad genérica `MediCita Team <team@medicita.local>` sobre la carpeta de práctica `PE5_U5_PFC_DIAZ_TIGASI_VERA/` (ya eliminada del repositorio), atribuidos mediante `.mailmap` el 03/09/2026.

---

### Mayummy Jailly Trujillo Vega

**Participación:** 11 de 21 días.

**Aporte narrativo:** Organización de fotos de entorno; reorganización de `02_Evidencias`; creación de mockups; trabajo en la práctica PE5 (Unidad V); participó en la jornada de anonimización del 31/08; actualización de documentación (05/09); registro de datos de Member Checking (06/09); renombrado uniforme de índices a `Readme.md` (08/09).

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `mtrujillov-sys`.

---

## 🔍 Nota metodológica

El reparto de participación por días es razonablemente parejo entre los cinco integrantes (11 a 18 de 21 días), consistente con lo ya señalado en el informe individual del docente: *"El reparto de confirmaciones en la ventana es notablemente parejo entre los cinco integrantes."* Paul Alexander Tigasi Sampedro, como líder de equipo, presenta la mayor participación por haber coordinado directamente la corrección final del repositorio en la Entrega 4 (2B).

---

## ✍️ Firma de los integrantes

Al firmar, cada integrante confirma que la información de este documento es correcta según su propio conocimiento, y corrige cualquier atribución que no le correspondiera.

| Integrante | Firma | Fecha |
|---|---|---|
| Paul Alexander Tigasi Sampedro | Tigasi Sampedro | 07/09/2026 0:28 |
| Steven Santiago Díaz Pontón |Steven Diaz | 07/09/2026 0:16 |
| Jamileth Estefanía Gamarra Zárate | Jamileth Gamarra | 07/09/2026 0:25 |
| Thais Melanie Herrera Ramos | Herrera Thais | 07/09/2026 0:19 |
| Mayummy Jailly Trujillo Vega | Trujillo Mayummy | 07/09/2026 0:20 |

> **Nota:** las cifras de commits y días de esta versión se actualizaron el 08/09/2026, con posterioridad a las firmas anteriores. Si algún integrante considera que su aporte narrativo necesita ajuste tras esta actualización, puede corregirlo y volver a firmar.
