
<div align="center">

# 📘 PE5 — Unidad 5 · Ingeniería de Requisitos (ISR-401)

### Guía definitiva de clonado, compilación y revisión — SICM/MediCita

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Curso](https://img.shields.io/badge/Curso-ISR--401-00509d?style=for-the-badge)
![Entrega](https://img.shields.io/badge/Entrega-PE5_/_Unidad_5-6a1b9a?style=for-the-badge)
![Compilador](https://img.shields.io/badge/Compilador-XeLaTeX-2e7d32?style=for-the-badge)

</div>

---

## 🎯 ¿Qué es esta carpeta?

Esta carpeta contiene el **PE5 (Producto Entregable 5)** del curso de **Ingeniería de Requisitos (ISR-401)**, correspondiente a la **Unidad 5**. Es un documento único en LaTeX que **integra y cierra** todo el ciclo de requisitos trabajado en PE1–PE4: especificación final, modelos UML, validación por inspección, gestión de línea base, requisitos de IA, métricas de calidad, retrospectiva, auditoría y banco de defensa.

> **Si estás calificando o revisando esta entrega, esta es la carpeta correcta y este README es el punto de partida.**

**Equipo:** Steven Santiago Díaz Pontón · Jamileth Estefanía Gamarra Zárate · Thais Melanie Herrera Ramos · Paul Alexander Tigasi Sampedro (líder) · Mayummy Jailly Trujillo Vega
**Docente:** Ing. Gleiston Cicerón Guerrero Ulloa
**Versión documental declarada:** PE5 / 4.0

---

## 📂 Contenido de la carpeta

| Archivo | Qué es | Para qué sirve en la revisión |
|---|---|---|
| `PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO.tex` | Fuente LaTeX del documento completo | Compilar y verificar reproducibilidad |
| `PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO.pdf` | PDF ya compilado y versionado | Lectura directa sin necesidad de compilar |
| `Banco_Defensa_PE5_SICM_.md` | Banco de preguntas y respuestas para la defensa oral | Simular preguntas del tribunal con su evidencia asociada |
| `matriz_trazabilidad_PE5.csv` | Matriz de 73 requisitos (fuente → RF/RNF → CU → clase UML → DFD → estado → BDD → CP → historia) | Verificar trazabilidad end-to-end |
| `instrumento_auditoria_PE5_.csv` | Métricas M1–M6 con valores antes/después y acción de mejora | Verificar el cierre cuantitativo de calidad del ERS |
| `backlog_sincronizado_PE5.csv` | 38 historias de usuario (US-01 a US-38) sincronizadas con los RF | Verificar sincronización backlog–ERS |
| `Imagenes_DCF_IR_LATEX/` | Diagramas que el `.tex` referencia: casos de uso, conceptual, estados y DFD | Insumo gráfico del documento — ✅ `D_DFD.png` generado y listo para subir (ver sección de hallazgo) |

---

## 🧰 Requisitos para compilar

- **XeLaTeX** (TeX Live 2023 o superior).
- Paquete de idioma **español para babel** (`texlive-lang-spanish` en Ubuntu/Debian). Sin él, la compilación falla de inmediato con `Package babel Error: Unknown option 'spanish'`.
- Paquetes LaTeX usados por el documento: `fontspec`, `babel`, `geometry`, `amsmath`, `amssymb`, `xcolor`, `longtable`, `booktabs`, `array`, `tabularx`, `multirow`, `graphicx`, `hyperref`, `fancyhdr`, `titlesec`, `enumitem`, `parskip`, `caption`, `float`, `pdflscape`, `tikz`, `pgfplots`, `microtype`, `appendix`, `lastpage`. Todos vienen en una instalación estándar de TeX Live "full" o `texlive-full`.
- El documento **no depende de un archivo `.bib` externo**: la bibliografía está embebida directamente con `\begin{thebibliography}`, así que no hace falta correr `biber` ni `bibtex`.

---

## ▶️ Cómo clonar y compilar (paso a paso)

```bash
# 1. Clonar el repositorio completo
git clone https://github.com/ptigasis-Alexander/MediCita_ISR401.git
cd MediCita_ISR401/PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO

# 2. (Solo si tu sistema no trae soporte de español para babel)
sudo apt-get install -y texlive-lang-spanish

# 3. Compilar exactamente 3 veces (necesario para resolver índice,
#    referencias cruzadas y citas de la bibliografía embebida)
xelatex -interaction=nonstopmode -halt-on-error PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO.tex
xelatex -interaction=nonstopmode -halt-on-error PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO.tex
xelatex -interaction=nonstopmode -halt-on-error PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO.tex
```

Alternativa con `latexmk` (hace las pasadas necesarias automáticamente):

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO.tex
```

**¿Por qué 3 pasadas y no 1?** En la primera pasada, LaTeX aún no conoce los números de página del índice ni las entradas de la bibliografía embebida (verás advertencias `Citation ... undefined` y `Reference ... undefined`, que son normales). Recién en la segunda y tercera pasada esas referencias quedan resueltas.

---

## ✅ Hallazgo de la verificación de reproducibilidad — ya resuelto

Se clonó el repositorio en un entorno limpio y se compiló siguiendo exactamente los pasos de arriba. Resultado:

- ✅ El soporte de español para babel, todas las demás dependencias y la bibliografía embebida funcionan correctamente.
- ❌ **La compilación fallaba de forma fatal** (`xdvipdfmx:fatal: Image inclusion failed`) porque faltaba el archivo `Imagenes_DCF_IR_LATEX/D_DFD.png`. El `.tex` lo referencia en la sección de modelos UML (`\includegraphics{D_DFD.png}`, figura con `\label{fig:DFD}`), pero ese archivo no existía en la carpeta ni en ningún otro lugar del repositorio — solo estaban `D_Casos_Uso_R.png`, `D_Conceptual.png` y `D_Estado_Critico.png`.
- Como confirmación: sustituyendo temporalmente `D_DFD.png` por una imagen de prueba, el documento compiló limpio en 3 pasadas (sin citas ni referencias sin resolver) y generó un PDF de **62 páginas**, muy cercano a las **63 páginas** del PDF ya versionado — es decir, el resto del documento está correcto; el único bloqueante real era esa imagen faltante.

**Solución ya generada:** el archivo **`D_DFD.png`** (DFD con la extensión de los dos procesos de IA — P11 Asistente virtual e IA-02 P12 Estimar riesgo de inasistencia, con sus entidades Paciente/Recepcionista y sus almacenes de datos D1/D2, coherente con `matriz_trazabilidad_PE5.csv` y la sección "Requisitos de Inteligencia Artificial" del `.tex`) fue creado y solo falta:

1. Colocarlo en `Imagenes_DCF_IR_LATEX/D_DFD.png` (mismo nombre exacto).
2. `git add`, `commit`, `push`.
3. Recompilar las 3 pasadas de `xelatex` para confirmar que el PDF se regenera sin errores.

> **Nota de honestidad académica:** este DFD de extensión IA se centra en los procesos P11/P12 y las entidades que intervienen directamente en ellos (Paciente, Recepcionista). No es una fusión completa con el DFD nivel 0 general del sistema (`03_Modelado/Diagramas_UML/Diagrama_nivel_0.png`, que incluye nutricionista, psicólogo, enfermería, etc.). Si el docente evalúa un único DFD que muestre **todos** los roles del sistema junto con P11/P12, hay que integrar ambos diagramas en uno solo antes de la defensa.

---

## ✅ Checklist final 

1. [ ] Clonar el repositorio en una carpeta limpia (sin residuos de compilaciones anteriores).
2. [ ] Instalar `texlive-lang-spanish` si el sistema no lo trae.
3. [ ] Colocar `D_DFD.png` (ya generado) en `Imagenes_DCF_IR_LATEX/`, hacer commit y push.
4. [ ] Ejecutar las 3 pasadas de `xelatex` (o `latexmk`) y confirmar que el PDF se genera **sin errores fatales**.
5. [ ] Abrir el PDF generado y comparar visualmente con `PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO.pdf` (portada, índice, las 4 figuras, tablas largas, apéndices).
6. [ ] Verificar que `matriz_trazabilidad_PE5.csv` tiene **73 filas de requisitos** con cadena completa (Fuente → RF/RNF → CU → Clase → DFD → Estado → BDD → CP → Historia → Estado de la traza).
7. [ ] Verificar que `instrumento_auditoria_PE5_.csv` muestra las 6 métricas (M1a/M1b/M1c, M2, M3, M4ade/M4atr, M5, M6) con valor **antes** y **después**, y que todas cumplen su referencia/umbral declarado.
8. [ ] Verificar que `backlog_sincronizado_PE5.csv` contiene **US-01 a US-38**, incluyendo las historias de IA (US-35 a US-38, ligadas a RF-IA1/RF-IA2). Crear/actualizar esas historias en el **tablero real** (Jira/Trello/GitHub Projects) antes de etiquetar la línea base — el propio CSV lo exige.
9. [ ] Registrar el **hash real** del commit que contiene todos los artefactos PE5 (PDF, `.tex`, matriz, instrumento de auditoría, `D_DFD.png` y este README) y crear el tag `baseline-pe5-v4.0` sobre ese commit. No inventar el hash antes de que el commit exista.
10. [ ] Confirmar que cada integrante añadió sus **hashes de commit reales** en la sección "Declaración individual de aporte" del `.tex` (no atribuir aportes sin evidencia visible en Git).
11. [ ] Leer `Banco_Defensa_PE5_SICM_.md` y verificar que cada respuesta cita una sección/evidencia real del PDF (frontera del sistema, requisitos de IA, equidad, línea base, etc.).
12. [ ] Si el docente pide un único DFD con todos los roles del sistema (no solo IA), integrar `D_DFD.png` con `03_Modelado/Diagramas_UML/Diagrama_nivel_0.png` en una sola imagen antes de la defensa.

---

## 🧭 Orden sugerido de lectura para el revisor (humano o IA)

El `.tex`/PDF está organizado en 15 secciones. Para evaluar con criterio de rúbrica, se sugiere este recorrido:

1. **Introducción** y **Metodología de Ingeniería de Requisitos** — contexto del proceso incremental PE1–PE5.
2. **ERS/SRS final integrada** — alcance funcional y no funcional consolidado.
3. **Modelos UML y lectura interpretativa** — casos de uso, clases, estados y DFD (con `D_DFD.png` ya colocado, ver sección de hallazgo).
4. **Validación: inspección, defectos y re-inspección** — los 10 defectos cerrados y la re-inspección sin conflictos abiertos.
5. **Gestión, línea base y trazabilidad** — versión 4.0 y condición para el tag `baseline-pe5-v4.0`.
6. **Requisitos de Inteligencia Artificial** — IA-01 (consultas administrativas) e IA-02 (riesgo de inasistencia), con sus mecanismos de *fallback*.
7. **Métricas de calidad del ERS** — M1–M6, ver `instrumento_auditoria_PE5_.csv` para los números crudos.
8. **Retrospectiva Start–Stop–Continue** y **Conclusiones**.
9. **Instrumento de auditoría y matriz final** — cruzar contra los CSV de esta misma carpeta.
10. **Banco de preguntas para la defensa** — usar `Banco_Defensa_PE5_SICM_.md` para simular el tribunal.
11. **Declaración individual de aporte** — cruzar contra el historial real de `git log --author`.
12. **Referencias y declaración de uso de IA** — bibliografía embebida (ISO 29148, ISO 25010, LOPPD, EU AI Act, WHO, entre otras).

---

## 📌 Antes de la entrega/defensa final

- [ ] Colocar `D_DFD.png` en `Imagenes_DCF_IR_LATEX/` y confirmar que la compilación ya no falla.
- [ ] Sustituir en el informe la referencia a "commit base auditado" por el **hash real** del commit PE5, una vez publicados estos archivos.
- [ ] Confirmar que US-35 a US-38 existan también en el **tablero real** del equipo, no solo en el CSV.
- [ ] Confirmar que la matriz PE5 coincida con los diagramas reales una vez agregado `D_DFD.png` — los enlaces de Clase/DFD/Estado deben ser validados por el equipo.
- [ ] Firmar/validar colectivamente la sección de declaración de aporte y añadir los hashes individuales reales de cada integrante.
- [ ] Etiquetar la línea base final como `baseline-pe5-v4.0` sobre el commit correcto.

---

<div align="center">

**Universidad Técnica Estatal de Quevedo · Facultad de Ciencias de la Computación**
**Ingeniería de Requisitos (ISR-401) · PE5 / Unidad 5**

⭐ Repositorio elaborado con fines exclusivamente académicos.

</div>
