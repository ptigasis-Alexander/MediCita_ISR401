<div align="center">

# 🏥 SICM — Sistema de Gestión Inteligente para un Centro Médico

### MediCita_ISR401

**Proyecto Fin de Curso (PFC) – Ingeniería de Requisitos (ISR-401)**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Carrera](https://img.shields.io/badge/Carrera-Ingeniería_de_Software-00509d?style=for-the-badge)
![Norma](https://img.shields.io/badge/ISO-29148:2018-orange?style=for-the-badge)
![Licencia](https://img.shields.io/badge/Licencia-MIT_%2B_CC_BY_4.0-2e7d32?style=for-the-badge)
![Entrega](https://img.shields.io/badge/Entrega_vigente-4_(2B)_/_Defensa_Final-red?style=for-the-badge)

</div>

---

## 📌 Entrega vigente que debe evaluarse

Este repositorio corresponde íntegramente a la **Entrega 4 (2B / Defensa Final)** de Ingeniería de Requerimientos (ISR-401), UTEQ. No existe ninguna otra entrega paralela vigente dentro de este repositorio. Cualquier material de otras unidades o prácticas anteriores a esta asignatura no forma parte de lo que debe calificarse aquí.

## ⚙️ Antes de empezar: clonar el repositorio

Este repositorio pesa varios gigabytes por los contenedores cifrados de audio/video en `02_Evidencias/00_Restringido/`. Un clon normal puede tardar bastante:

```bash
git clone https://github.com/ptigasis-Alexander/MediCita_ISR401.git
cd MediCita_ISR401
```

Si solo necesitas revisar documentación y código (sin descargar los `.7z` pesados), puedes hacer un clon parcial:

```bash
git clone --filter=blob:none https://github.com/ptigasis-Alexander/MediCita_ISR401.git
```

## ✅ Estado real de avance por sección

| Sección | Contenido | Estado |
|---|---|:---:|
| `01_ERS/` | `ERS_SRS_2B_V2.0.tex` (fuente) | 🟡 En cierre — falta compilar el PDF; `Imagenes_IR_PFC/` aún sin las figuras |
| `02_Evidencias/` | Consentimientos, transcripciones, codificación, cuestionario, entorno, restringido cifrado | 🟢 Sustancialmente completo |
| `03_Modelado/` | Diagramas UML, diagramas corregidos, mockups/interfaces finales | 🟢 Completo |
| `04_Trazabilidad/` | Matriz de trazabilidad (70 filas, RF-01–RF-40 y RNF-01–RNF-18 con cobertura completa) y priorización MoSCoW/Kano | 🟢 Completo |
| `05_MVP/` | Producto Mínimo Viable navegable, publicado en GitHub Pages | 🟢 Completo |
| `06_Experimento/` | Datos procesados, prompts LLM, resultados estadísticos reproducibles, scripts | 🟡 Protocolo, registro OSF y desviaciones existen localmente en edición; aún no subidos |
| `07_Publicacion/` | Manuscrito (`.tex`) y paquete de datos para Zenodo | 🟡 Falta compilar el PDF del manuscrito |
| `08_Etica/` | Documentación ética completa (Anexo A.1–A.13, Categoría A, adendas) | 🟢 Completo |
| `09_Defensa/` | Materiales de la defensa oral | 🔴 Pendiente |
| Depósito Zenodo + SWHID | DOI persistente y archivado en Software Heritage | 🔴 Pendiente (acción final) |
| `checksums.sha256` / `fair_assessment.pdf` (raíz) | Integridad y autoevaluación FAIR | 🔴 Pendientes de generar/ejecutar |

> Este cuadro se actualiza en cada commit relevante. Si algún estado no coincide con el contenido real de una carpeta, prevalece el contenido real, no este resumen.

---

## 📖 Resumen del dominio

**SICM (Sistema de Gestión Inteligente para un Centro Médico)** es el sistema especificado y prototipado en este repositorio. Su dominio es la gestión operativa de un centro médico ambulatorio, con las siguientes áreas identificadas mediante entrevistas de elicitación: Medicina General, Terapia Física, Nutrición, Odontología/Coordinación, Enfermería, Psicología, Recepción/Recaudación y la perspectiva del paciente.

---

## 👥 Equipo e integrantes

| Integrante | Rol | Correo institucional | ORCID |
|---|---|---|:---:|
| Paul Alexander Tigasi Sampedro | Líder | ptigasis@uteq.edu.ec | [0009-0005-1812-7100](https://orcid.org/0009-0005-1812-7100) |
| Steven Santiago Díaz Pontón | Técnico | sdiazp3@uteq.edu.ec | [0009-0000-6558-4930](https://orcid.org/0009-0000-6558-4930) |
| Jamileth Estefanía Gamarra Zárate | Secretaria | jgamarraz@uteq.edu.ec | [0009-0002-8916-6578](https://orcid.org/0009-0002-8916-6578) |
| Thais Melanie Herrera Ramos | Técnica | therrerar@uteq.edu.ec | [0009-0005-2666-6921](https://orcid.org/0009-0005-2666-6921) |
| Mayummy Jailly Trujillo Vega | Técnica | mtrujillov@uteq.edu.ec | [0009-0009-5157-290X](https://orcid.org/0009-0009-5157-290X) |

**Docente:** Ing. Gleiston Cicerón Guerrero Ulloa · **Asignatura:** Ingeniería de Requerimientos (ISR-401) · **Facultad:** Ciencias de la Computación — UTEQ

---

## 🔗 Enlaces clave

| Recurso | Enlace | Estado |
|---|---|:---:|
| 📄 ERS/SRS 2B (fuente) | [`01_ERS/ERS_SRS_2B_V2.0.tex`](01_ERS/) | 🟡 Falta compilar PDF |
| 💻 MVP funcional (demo en vivo) | [ptigasis-alexander.github.io/MediCita_ISR401/05_MVP/](https://ptigasis-alexander.github.io/MediCita_ISR401/05_MVP/) | 🟢 Disponible |
| 📝 Registro OSF | [10.17605/OSF.IO/DTYNC](https://doi.org/10.17605/OSF.IO/DTYNC) | 🟢 Público |
| 📦 Depósito Zenodo (dataset con DOI) | *(pendiente de publicar)* | 🔴 Pendiente |
| 🗄️ Archivado Software Heritage (SWHID) | *(pendiente de generar)* | 🔴 Pendiente |
| 📜 Cómo citar este repositorio | [`CITATION.cff`](CITATION.cff) | 🟢 Disponible |
| ⚖️ Licencia | [`LICENSE`](LICENSE) | 🟢 Disponible |

---

## 🔬 Cómo reproducir y ejecutar cada parte del proyecto

### Requisitos previos (instalar una sola vez)

```bash
# Para compilar los documentos LaTeX (ERS y manuscrito)
sudo apt install texlive-xetex texlive-lang-spanish

# Para correr el análisis estadístico
pip install scipy matplotlib --break-system-packages
```

### Tabla de reproducción

| Qué quiero verificar | Dónde | Cómo |
|---|---|---|
| Requisitos funcionales y no funcionales | `01_ERS/` | Ver "Cómo compilar el ERS/SRS" abajo — requiere pasos específicos, no alcanza con un solo `xelatex`. |
| Trazabilidad Ley→RF→CU→Mockup | `04_Trazabilidad/` | Abrir `matriz_trazabilidad.csv` (70 filas). Verificar cobertura completa: `cut -d';' -f6 matriz_trazabilidad.csv \| tr '/' '\n' \| sort -u`. |
| Diagramas UML y mockups | `03_Modelado/` | `Diagramas_UML/`, `Diagramas_UML_Corregidos/` (`.drawio`/`.png`), `Mockups_Prototipo_Final/` (set vigente; `Mockups/` es el histórico) |
| Prototipo funcional | `05_MVP/` | Enlace de GitHub Pages, o local: `cd 05_MVP && python3 -m http.server 8000` |
| Evidencia de campo | `02_Evidencias/` | Cada subcarpeta tiene su propio README con checklist de verificación |
| Evidencia restringida (audio/video originales) | `02_Evidencias/00_Restringido/` | Requiere contraseña entregada por el docente vía SGA. Ver procedimiento de verificación en el README de esa carpeta. |
| Análisis experimental reproducible | `06_Experimento/scripts_analisis/run_all.py` | `cd 06_Experimento/scripts_analisis && python3 run_all.py` — regenera `resultados_estadisticos.json`; comparar con `diff` contra el archivo ya guardado en `06_Experimento/resultados/` |
| Manuscrito de publicación | `07_Publicacion/manuscrito_final.tex` | Ver "Cómo compilar el manuscrito" abajo |
| Documentación ética | `08_Etica/` | Ver `08_Etica_.md` |
| Integridad de archivos | raíz | `sh GENERA_CHEDKSUMS.sh` desde la raíz ya clonada; verificar con `sha256sum --check checksums.sha256` |

### Cómo compilar el ERS/SRS

```bash
cd 01_ERS
# Requiere que Imagenes_IR_PFC/ ya tenga las figuras (ver estado arriba)
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
bibtex ERS_SRS_2B_V2.0
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
```

Usa `xelatex`, no `pdflatex` (el documento requiere `fontspec`). Se necesitan las 3 pasadas + `bibtex` para que el índice y las referencias bibliográficas queden bien enlazados — con una sola pasada no alcanza.

### Cómo compilar el manuscrito

```bash
cd 07_Publicacion
pdflatex -interaction=nonstopmode manuscrito_final.tex
bibtex manuscrito_final
pdflatex -interaction=nonstopmode manuscrito_final.tex
pdflatex -interaction=nonstopmode manuscrito_final.tex
```

---

<div align="center">

## Universidad Técnica Estatal de Quevedo
### Facultad de Ciencias de la Computación · Carrera de Ingeniería de Software
### Proyecto Fin de Curso — Sistema de Gestión Inteligente para un Centro Médico (SICM)

⭐ Repositorio elaborado con fines exclusivamente académicos.

</div>
