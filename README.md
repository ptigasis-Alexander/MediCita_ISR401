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
| `01_ERS/` | ERS 2A (`.tex` + `.pdf`), `ERS_SRS_2B_V2.0.tex`, referencias, `Imagenes_DCF_IR_LATEX/` e `Imagenes_IR_PFC/` | 🟡 En cierre — las imágenes ya están presentes; falta compilar y subir el PDF final del ERS 2B |
| `02_Evidencias/` | Consentimientos, transcripciones, codificación, cuestionario, entorno, validación walkthrough y restringido cifrado | 🟢 Sustancialmente completo |
| `03_Modelado/` | Diagramas UML, diagramas corregidos, mockups/interfaces finales | 🟢 Completo |
| `04_Trazabilidad/` | Matriz de trazabilidad original, matriz actualizada y priorización MoSCoW/Kano | 🟢 Completo |
| `05_MVP/` | Demo guiada publicada en GitHub Pages + `MediCita_prototipo_final_actualizado.html` | 🟢 Completo |
| `06_Experimento/` | Datos, instrumentos, prompts LLM, resultados, scripts, protocolo, registro OSF y desviaciones | 🟢 Completo en repositorio |
| `07_Publicacion/` | Manuscrito (`.tex`/`.pdf`, compilado con DOI de Zenodo incorporado), referencias, figuras, tablas y paquete de datos ya depositado en Zenodo | 🟢 Completo |
| `08_Etica/` | Documentación ética completa (Anexos A1–A13 y documentos complementarios) | 🟢 Completo |
| `09_Defensa/` | Actualmente solo contiene `defensa.md` como marcador | 🔴 Pendiente |
| Depósito Zenodo | DOI persistente: [10.5281/zenodo.22236373](https://doi.org/10.5281/zenodo.22236373) | 🟢 Publicado |
| Archivado Software Heritage (SWHID) | Identificador persistente del código | 🔴 Pendiente |
| `checksums.sha256` / `fair_assessment.pdf` (raíz) | Integridad y autoevaluación FAIR | 🔴 Pendientes de generar/subir |

> Este cuadro se actualiza en cada commit relevante. Si algún estado no coincide con el contenido real de una carpeta, prevalece el contenido real, no este resumen.

---

## 📖 Resumen del dominio

**SICM (Sistema de Gestión Inteligente para un Centro Médico)** es el sistema especificado y prototipado en este repositorio. Su dominio es la gestión operativa de un centro médico ambulatorio, con las siguientes áreas identificadas mediante entrevistas de elicitación y sesiones posteriores de validación: Medicina General, Terapia Física, Nutrición, Odontología/Coordinación, Enfermería, Psicología, Recepción/Recaudación y la perspectiva del paciente.

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
| 📄 ERS/SRS 2A | [`01_ERS/ERS_SRS_2A_v1.0.pdf`](01_ERS/ERS_SRS_2A_v1.0.pdf) | 🟢 Disponible |
| 📄 ERS/SRS 2B (fuente) | [`01_ERS/ERS_SRS_2B_V2.0.tex`](01_ERS/ERS_SRS_2B_V2.0.tex) | 🟡 Falta compilar PDF final |
| 💻 MVP funcional (demo en vivo) | [ptigasis-alexander.github.io/MediCita_ISR401/](https://ptigasis-alexander.github.io/MediCita_ISR401/) | 🟢 Disponible |
| 🖥️ Prototipo final revisado | [`05_MVP/MediCita_prototipo_final_actualizado.html`](05_MVP/MediCita_prototipo_final_actualizado.html) | 🟢 Disponible |
| 📝 Registro OSF | [10.17605/OSF.IO/DTYNC](https://doi.org/10.17605/OSF.IO/DTYNC) | 🟢 Público |
| 📄 Protocolo experimental | [`06_Experimento/protocolo.pdf`](06_Experimento/protocolo.pdf) | 🟢 Disponible |
| 📄 Registro OSF en PDF | [`06_Experimento/osf_registration.pdf`](06_Experimento/osf_registration.pdf) | 🟢 Disponible |
| 📄 Desviaciones del protocolo | [`06_Experimento/osf_deviations.pdf`](06_Experimento/osf_deviations.pdf) | 🟢 Disponible |
| 📦 Depósito Zenodo (dataset con DOI) | [10.5281/zenodo.22236373](https://doi.org/10.5281/zenodo.22236373) | 🟢 Publicado |
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
| ERS 2A compilado | `01_ERS/ERS_SRS_2A_v1.0.pdf` | Abrir directamente el PDF disponible en el repositorio. |
| Imágenes del ERS 2A | `01_ERS/Imagenes_DCF_IR_LATEX/` | Contiene las figuras utilizadas por `ERS_SRS_2A_v1.0.tex`. |
| Imágenes del ERS 2B | `01_ERS/Imagenes_IR_PFC/` | Carpeta de figuras utilizada por la versión 2B. |
| Trazabilidad Ley→RF→CU→Mockup | `04_Trazabilidad/` | Abrir preferentemente `matriz_trazabilidad_ACTUALIZADA.csv`; también se conserva la matriz anterior como evidencia de evolución. |
| Diagramas UML y mockups | `03_Modelado/` | Revisar diagramas UML, versiones corregidas y `Mockups_Prototipo_Final/`. |
| Demo guiada del MVP | `05_MVP/` | Abrir GitHub Pages o ejecutar localmente con `python3 -m http.server 8000`. |
| Prototipo final revisado | `05_MVP/MediCita_prototipo_final_actualizado.html` | Abrir el HTML directamente en el navegador. |
| Evidencia de campo | `02_Evidencias/` | Revisar consentimientos, transcripciones, codificación y sesiones de validación walkthrough. |
| Evidencia restringida (audio/video originales) | `02_Evidencias/00_Restringido/` | Requiere contraseña autorizada para los contenedores cifrados. |
| Análisis experimental reproducible | `06_Experimento/scripts_analisis/run_all.py` | `cd 06_Experimento/scripts_analisis && python3 run_all.py` |
| Protocolo y registro OSF | `06_Experimento/` | Abrir `protocolo.pdf`, `osf_registration.pdf` y `osf_deviations.pdf`. |
| Manuscrito de publicación | `07_Publicacion/manuscrito_final.tex` | Ver "Cómo compilar el manuscrito" abajo. |
| Documentación ética | `08_Etica/` | Ver `08_Etica_.md` y los anexos A1–A13. |
| Defensa | `09_Defensa/` | Actualmente solo contiene `defensa.md`; faltan los materiales finales. |
| Integridad de archivos | raíz | `sh GENERA_CHEDKSUMS.sh`; luego verificar con `sha256sum --check checksums.sha256`. |

### Cómo compilar el ERS/SRS

```bash
cd 01_ERS

xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
bibtex ERS_SRS_2B_V2.0
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
```

Usa `xelatex`, no `pdflatex` (el documento requiere `fontspec`). Las carpetas de imágenes ya están presentes en `01_ERS/`, por lo que el pendiente de esta sección es compilar correctamente y subir el PDF final del ERS 2B.

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

