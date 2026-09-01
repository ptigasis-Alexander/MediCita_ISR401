<div align="center">

# 🏥 SICM — Sistema de Gestión Inteligente para un Centro Médico

### MediCita_ISR401

**Proyecto Fin de Curso (PFC) – Ingeniería de Requerimientos (ISR-401)**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Carrera](https://img.shields.io/badge/Carrera-Ingeniería_de_Software-00509d?style=for-the-badge)
![Norma](https://img.shields.io/badge/ISO-29148:2018-orange?style=for-the-badge)
![Licencia](https://img.shields.io/badge/Licencia-MIT_%2B_CC_BY_4.0-2e7d32?style=for-the-badge)
![Entrega](https://img.shields.io/badge/Entrega-4_(2B)_Defensa_Final-success?style=for-the-badge)

</div>

---

## 📌 Entrega vigente y alcance de la evaluación

Este repositorio corresponde a la **Entrega 4 (2B / Defensa Final)** del Proyecto Fin de Curso de la asignatura **Ingeniería de Requerimientos (ISR-401)** de la Universidad Técnica Estatal de Quevedo (UTEQ).

La evaluación de esta entrega debe considerar los artefactos correspondientes al PFC organizados principalmente en las carpetas `01_ERS/` a `09_Defensa/`, junto con los archivos de documentación, integridad y reproducibilidad ubicados en la raíz del repositorio.

El repositorio integra la línea base final del proyecto **SICM / MediCita**, incluyendo:

- ERS/SRS.
- Evidencias de elicitación y validación.
- Modelado UML.
- Trazabilidad.
- MVP funcional.
- Componente empírico reproducible.
- Documentación de publicación.
- Documentación ética.
- Materiales de defensa final.

> **Importante:** para la evaluación de la Entrega 4 (2B) debe prevalecer la documentación final y vigente del PFC.

---

## ⚠️ Práctica V5 — material no evaluable en esta entrega

La **Práctica V5 no forma parte de los artefactos que deben evaluarse para la Entrega 4 (2B / Defensa Final)**.

El material correspondiente a dicha práctica se conserva únicamente como **evidencia académica independiente** y cuenta con documentación separada que permite identificarlo.

Su presencia dentro del repositorio o de su historial **no implica que forme parte de la línea base evaluable de la Entrega 4 (2B)**.

Por tanto, para la calificación de esta entrega debe tomarse como referencia la documentación final del Proyecto Fin de Curso contenida en las carpetas `01_ERS/` a `09_Defensa/` y no utilizar la Práctica V5 como sustituto, complemento obligatorio o artefacto evaluable de la Entrega 4 (2B).

---

## 🗃️ Historial de repositorios del proyecto

Los avances **1A y 1B** se desarrollaron y conservaron en el repositorio histórico del mismo proyecto:

**Repositorio histórico — Avances 1A y 1B:**

https://github.com/ptigasis-Alexander/PFC_IR_AVANCES_TIGASI_GAMARRA-ZARATE_DIAZ_THAIS_TRUJILLO

A partir del avance **2A**, el proyecto adoptó una nueva estructura de organización y continuó su desarrollo en el repositorio actual:

**Repositorio vigente — desde 2A hasta Entrega 4 (2B):**

https://github.com/ptigasis-Alexander/MediCita_ISR401

Ambos repositorios corresponden a la misma línea de desarrollo del Proyecto Fin de Curso.

Para la **Entrega 4 (2B / Defensa Final)** prevalece el contenido vigente de este repositorio.

---

## ⚙️ Clonar el repositorio

El repositorio puede ocupar varios gigabytes debido principalmente a las evidencias audiovisuales y a los contenedores de evidencia restringida.

### Clonación completa

```bash
git clone https://github.com/ptigasis-Alexander/MediCita_ISR401.git
cd MediCita_ISR401
```

### Clonación parcial

Si inicialmente solo se desea revisar documentación y código sin descargar todos los objetos pesados:

```bash
git clone --filter=blob:none https://github.com/ptigasis-Alexander/MediCita_ISR401.git
cd MediCita_ISR401
```

> Algunos artefactos audiovisuales o restringidos pueden requerir una descarga posterior debido a su tamaño.

---

## ✅ Estado de la Entrega 4 (2B)

| Sección / artefacto | Contenido principal | Estado |
|---|---|:---:|
| `01_ERS/` | ERS/SRS, fuentes LaTeX, bibliografía y figuras | 🟢 Completo |
| `02_Evidencias/` | Entrevistas, consentimientos, transcripciones, codificación temática, cuestionario, walkthrough y evidencia restringida | 🟢 Completo |
| `03_Modelado/` | Diagramas UML y mockups/interfaces finales | 🟢 Completo |
| `04_Trazabilidad/` | Matrices de trazabilidad y priorización de requisitos | 🟢 Completo |
| `05_MVP/` | Prototipo funcional y demo mediante GitHub Pages | 🟢 Completo |
| `06_Experimento/` | Protocolo, OSF, instrumentos, datos, scripts, resultados y desviaciones | 🟢 Completo |
| `07_Publicacion/` | Manuscrito, bibliografía, figuras, tablas y paquete de publicación | 🟢 Completo |
| `08_Etica/` | Documentación ética y anexos correspondientes | 🟢 Completo |
| `09_Defensa/` | Presentación, guion, folleto y video de defensa final | 🟢 Completo |
| Práctica V5 | Material académico independiente | ⚪ No evaluable en 2B |
| Registro OSF | DOI `10.17605/OSF.IO/DTYNC` | 🟢 Público |
| Depósito Zenodo | DOI `10.5281/zenodo.22236373` | 🟢 Publicado |
| Software Heritage | Intento de archivado realizado; SWHID no obtenido | 🟠 No obtenido |
| Integridad SHA-256 | Comprobación de integridad de archivos | 🟡 Regenerar después del último cambio |
| Autoevaluación FAIR | Evaluación de principios FAIR | 🟡 Verificar versión final |

> **Nota:** si se modifica, agrega o elimina cualquier archivo después de generar `checksums.sha256`, los hashes deben regenerarse antes del cierre definitivo.

---

# 📖 Descripción del proyecto

**SICM — Sistema de Gestión Inteligente para un Centro Médico**, denominado también **MediCita**, es una propuesta de sistema orientada a centralizar y apoyar los principales procesos clínicos y administrativos de un centro médico ambulatorio.

El proyecto fue desarrollado a partir de evidencia de campo obtenida durante el proceso de Ingeniería de Requisitos.

Las áreas consideradas incluyen:

- Medicina General.
- Enfermería.
- Odontología.
- Psicología.
- Nutrición.
- Terapia Física.
- Recepción y Recaudación.
- Coordinación.
- Paciente.

El sistema contempla procesos relacionados con:

- Registro de pacientes.
- Gestión de citas.
- Agenda profesional.
- Historia clínica.
- Signos vitales.
- Atención por especialidad.
- Recetas médicas.
- Entrega de medicamentos.
- Derivaciones.
- Pagos y comprobantes.
- Inventario.
- Notificaciones.
- Gestión de personal.
- Reportes.
- Auditoría.
- Control de acceso basado en roles.

---

# 👥 Equipo

| Integrante | Rol | Correo institucional | ORCID |
|---|---|---|:---:|
| Paul Alexander Tigasi Sampedro | Líder | ptigasis@uteq.edu.ec | [0009-0005-1812-7100](https://orcid.org/0009-0005-1812-7100) |
| Steven Santiago Díaz Pontón | Técnico | sdiazp3@uteq.edu.ec | [0009-0000-6558-4930](https://orcid.org/0009-0000-6558-4930) |
| Jamileth Estefanía Gamarra Zárate | Secretaria | jgamarraz@uteq.edu.ec | [0009-0002-8916-6578](https://orcid.org/0009-0002-8916-6578) |
| Thais Melanie Herrera Ramos | Técnica | therrerar@uteq.edu.ec | [0009-0005-2666-6921](https://orcid.org/0009-0005-2666-6921) |
| Mayummy Jailly Trujillo Vega | Técnica | mtrujillov@uteq.edu.ec | [0009-0009-5157-290X](https://orcid.org/0009-0009-5157-290X) |

**Docente:** Ing. Gleiston Cicerón Guerrero Ulloa  
**Asignatura:** Ingeniería de Requerimientos (ISR-401)  
**Facultad:** Ciencias de la Computación  
**Universidad:** Universidad Técnica Estatal de Quevedo (UTEQ)

---

# 🔗 Enlaces principales

| Recurso | Enlace | Estado |
|---|---|:---:|
| 📄 ERS/SRS 2A | [`01_ERS/ERS_SRS_2A_v1.0.pdf`](01_ERS/ERS_SRS_2A_v1.0.pdf) | 🟢 |
| 📄 ERS/SRS 2B final | [`01_ERS/ERS_SRS_2B_V2.0.pdf`](01_ERS/ERS_SRS_2B_V2.0.pdf) | 🟢 |
| 📝 Fuente LaTeX ERS 2B | [`01_ERS/ERS_SRS_2B_V2.0.tex`](01_ERS/ERS_SRS_2B_V2.0.tex) | 🟢 |
| 💻 MVP funcional | [GitHub Pages](https://ptigasis-alexander.github.io/MediCita_ISR401/) | 🟢 |
| 🖥️ Prototipo final | [`05_MVP/MediCita_prototipo_final_actualizado.html`](05_MVP/MediCita_prototipo_final_actualizado.html) | 🟢 |
| 📝 Registro OSF | [10.17605/OSF.IO/DTYNC](https://doi.org/10.17605/OSF.IO/DTYNC) | 🟢 |
| 📄 Protocolo experimental | [`06_Experimento/protocolo.pdf`](06_Experimento/protocolo.pdf) | 🟢 |
| 📄 Registro OSF PDF | [`06_Experimento/osf_registration.pdf`](06_Experimento/osf_registration.pdf) | 🟢 |
| 📄 Desviaciones del protocolo | [`06_Experimento/osf_deviations.pdf`](06_Experimento/osf_deviations.pdf) | 🟢 |
| 📑 Manuscrito final | [`07_Publicacion/manuscrito_final.pdf`](07_Publicacion/manuscrito_final.pdf) | 🟢 |
| 📦 Dataset Zenodo | [10.5281/zenodo.22236373](https://doi.org/10.5281/zenodo.22236373) | 🟢 |
| 🎓 Defensa final | [`09_Defensa/`](09_Defensa/) | 🟢 |
| 📜 Citación | [`CITATION.cff`](CITATION.cff) | 🟢 |
| ⚖️ Licencia | [`LICENSE`](LICENSE) | 🟢 |

---

# 📊 Evidencia y resultados principales

## Primera ronda — elicitación

La primera ronda estuvo formada por **8 entrevistas de elicitación** correspondientes a:

1. Medicina General.
2. Enfermería.
3. Nutrición.
4. Odontología/Coordinación.
5. Terapia Física.
6. Psicología.
7. Recepción.
8. Paciente simulado.

Estas entrevistas fueron utilizadas como fuente para identificar necesidades y construir los requisitos iniciales del sistema.

---

## Segunda ronda — validación del prototipo

La segunda ronda dispone de **10 sesiones de validación del prototipo con transcripción disponible**.

Entre ellas se encuentran las sesiones correspondientes a Psicología y al paciente simulado 02.

El procesamiento de la evidencia produjo:

| Indicador | Resultado |
|---|---:|
| Entrevistas de elicitación | **8** |
| Sesiones de validación procesadas | **10** |
| Observaciones procesadas | **46** |
| Completadas con observación de mejora | **39** |
| No completadas | **5** |
| Completadas sin observación | **2** |
| Relaciones observación–requisito | **72** |

Los resultados anteriores corresponden al procesamiento de las evidencias de walkthrough.

---

# 🧪 Cobertura técnica del MVP

La cobertura del MVP se determinó mediante una **verificación técnica reproducible** de los requisitos funcionales clasificados como **Must**.

Se verificaron:

**20 de 22 RF Must**

lo que corresponde a:

## **90,91 % de cobertura técnica**

El umbral académico establecido para esta entrega es:

## **≥ 80 %**

Por tanto, la cobertura técnica obtenida supera el umbral establecido.

Los requisitos que permanecen sin cierre técnico son:

- **RF-09**
- **RF-18**

### ⚠️ Interpretación correcta del 90,91 %

El **90,91 % corresponde exclusivamente a la verificación técnica del MVP**.

No representa:

- una puntuación SUS;
- satisfacción de los participantes;
- porcentaje de aceptación de usuarios;
- precisión de una IA;
- ni una segunda revalidación humana realizada después de las correcciones.

Las sesiones de walkthrough identificaron hallazgos y necesidades.

A partir de esos hallazgos se realizaron ajustes al MVP. Las correcciones posteriores se comprobaron mediante **verificación técnica reproducible** y no se atribuyen a una nueva evaluación realizada por los participantes.

---

# 🔗 Trazabilidad

Uno de los objetivos principales del proyecto es mantener trazabilidad entre los diferentes artefactos.

De manera general, el flujo de trazabilidad utilizado es:

```text
Fuente / necesidad
        ↓
Requisito
        ↓
Caso de uso / historia
        ↓
Modelo UML
        ↓
Interfaz / MVP
        ↓
Observación de validación
        ↓
Verificación
```

Los archivos correspondientes se encuentran principalmente en:

```text
04_Trazabilidad/
```

---

# 🗂️ Organización del repositorio

```text
MediCita_ISR401/
│
├── 01_ERS/
├── 02_Evidencias/
├── 03_Modelado/
├── 04_Trazabilidad/
├── 05_MVP/
├── 06_Experimento/
├── 07_Publicacion/
├── 08_Etica/
├── 09_Defensa/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── checksums.sha256
└── fair_assessment.pdf
```

---

## 📁 `01_ERS/`

Contiene la Especificación de Requisitos de Software del proyecto.

Incluye:

- requisitos funcionales;
- requisitos no funcionales;
- reglas de negocio;
- priorización;
- historias de usuario;
- casos de uso;
- referencias;
- figuras;
- fuentes LaTeX;
- PDF de la ERS/SRS.

---

## 📁 `02_Evidencias/`

Contiene las evidencias utilizadas durante la elicitación y validación.

Incluye, según corresponda:

- consentimientos;
- transcripciones;
- codificación temática;
- cuestionario;
- fotografías de entorno;
- documentos de apoyo;
- validación walkthrough;
- evidencia restringida.

Los archivos que contienen información sensible o identificable deben permanecer en el área restringida o publicarse debidamente anonimizados.

---

## 📁 `03_Modelado/`

Contiene los modelos UML y las representaciones visuales utilizadas para describir el sistema.

Incluye diagramas y mockups/interfaces relacionados con los requisitos del proyecto.

---

## 📁 `04_Trazabilidad/`

Contiene las matrices utilizadas para relacionar requisitos, fuentes, modelos, evidencias, interfaces y elementos de verificación.

---

## 📁 `05_MVP/`

Contiene el prototipo funcional utilizado durante el proyecto.

La versión pública puede consultarse mediante GitHub Pages:

https://ptigasis-alexander.github.io/MediCita_ISR401/

---

## 📁 `06_Experimento/`

Contiene el componente empírico y reproducible del proyecto:

- protocolo;
- registro OSF;
- desviaciones;
- instrumentos;
- prompts LLM;
- datos crudos permitidos;
- datos procesados;
- resultados;
- scripts de análisis.

---

## 📁 `07_Publicacion/`

Contiene:

- manuscrito científico;
- fuente LaTeX;
- bibliografía;
- figuras;
- tablas;
- documentación del dataset;
- materiales asociados al depósito en Zenodo.

---

## 📁 `08_Etica/`

Contiene la documentación ética del proyecto y los anexos correspondientes.

Los materiales con datos identificables deben tratarse de acuerdo con su nivel de acceso y no incorporarse a datasets públicos sin anonimización.

---

## 📁 `09_Defensa/`

Contiene los materiales utilizados para la **Defensa Final de la Entrega 4 (2B)**:

- presentación de diapositivas;
- guion de exposición;
- folleto de apoyo;
- video de defensa.

Estos materiales corresponden al cierre académico del Proyecto Fin de Curso.

---

# 🔬 Reproducibilidad

## Requisitos básicos

Para documentos LaTeX que utilizan XeLaTeX:

```bash
sudo apt install texlive-xetex texlive-lang-spanish
```

Para ejecutar los scripts de análisis:

```bash
pip install scipy matplotlib
```

---

# 📄 Compilar ERS/SRS 2B

La ERS/SRS 2B utiliza XeLaTeX.

```bash
cd 01_ERS

xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
bibtex ERS_SRS_2B_V2.0
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
```

Las figuras correspondientes se encuentran en:

```text
01_ERS/Imagenes_IR_PFC/
```

---

# 📑 Compilar el manuscrito

```bash
cd 07_Publicacion

pdflatex -interaction=nonstopmode manuscrito_final.tex
bibtex manuscrito_final
pdflatex -interaction=nonstopmode manuscrito_final.tex
pdflatex -interaction=nonstopmode manuscrito_final.tex
```

Las figuras se encuentran en:

```text
07_Publicacion/figuras/
```

La bibliografía se encuentra en:

```text
07_Publicacion/referencias_manuscrito.bib
```

---

# 📊 Reproducir el análisis

```bash
cd 06_Experimento/scripts_analisis
python3 run_all.py
```

Los resultados generados mediante los scripts deben corresponder con los datos procesados y con los valores reportados en los documentos finales.

---

# 🔐 Evidencias restringidas

Los archivos audiovisuales originales o materiales que puedan contener información sensible o identificable se mantienen separados de los datos destinados a publicación abierta.

La evidencia restringida se encuentra en:

```text
02_Evidencias/00_Restringido/
```

Su acceso debe limitarse a personas autorizadas.

Los datasets públicos no deben contener identificadores directos como:

- nombres;
- cédulas;
- firmas;
- rostros;
- voces;
- teléfonos;
- correos personales;
- direcciones;
- u otros elementos que permitan identificar directamente a una persona.

---

# 🔎 Integridad mediante SHA-256

La integridad de los artefactos del repositorio se controla mediante hashes SHA-256.

Después de incorporar los archivos definitivos, especialmente los materiales de `09_Defensa/`, los hashes deben regenerarse.

```bash
sh GENERA_CHEDKSUMS.sh
```

Posteriormente pueden comprobarse mediante:

```bash
sha256sum --check checksums.sha256
```

El archivo:

```text
checksums.sha256
```

permite detectar modificaciones posteriores en los archivos incluidos en la línea base.

> **Importante:** `checksums.sha256` debe generarse después del último cambio realizado en la entrega.

---

# ♻️ Autoevaluación FAIR

La autoevaluación de los principios FAIR se documenta mediante:

```text
fair_assessment.pdf
```

La evaluación FAIR y los hashes SHA-256 son mecanismos distintos del archivado del código en Software Heritage.

---

# 🌐 Identificadores persistentes

## OSF

El protocolo de validación dispone de un registro público en OSF.

**DOI:**

```text
10.17605/OSF.IO/DTYNC
```

---

## Zenodo

El paquete de datos asociado al proyecto dispone de un depósito en Zenodo.

**DOI:**

```text
10.5281/zenodo.22236373
```

---

# 🗄️ Software Heritage

Se intentó realizar el archivado del repositorio en **Software Heritage** con el objetivo de obtener un identificador persistente **SWHID** para el código fuente del proyecto.

Sin embargo, durante el cierre de la entrega el proceso **no pudo completarse satisfactoriamente**.

El repositorio contiene una cantidad considerable de evidencia audiovisual y contenedores de gran tamaño. Esto incrementó notablemente el peso del repositorio y ocasionó inconvenientes y tiempos de carga elevados durante el intento de archivado.

Por esta razón:

## **No se obtuvo un SWHID para esta entrega.**

No se declara ni se inventa un identificador que no haya sido generado correctamente.

Esta limitación se documenta de manera transparente como un inconveniente técnico encontrado durante el proceso de preservación del repositorio.

La ausencia del SWHID no modifica los identificadores persistentes que sí fueron obtenidos para otros componentes:

| Servicio | Identificador | Estado |
|---|---|:---:|
| OSF | `10.17605/OSF.IO/DTYNC` | 🟢 Obtenido |
| Zenodo | `10.5281/zenodo.22236373` | 🟢 Obtenido |
| Software Heritage | SWHID | 🟠 No obtenido |

> El SWHID de Software Heritage no debe confundirse con los hashes SHA-256 utilizados para verificar la integridad local de los artefactos.

---

# ⚠️ Integridad académica

Los resultados reportados en el proyecto corresponden únicamente a evidencia disponible y a procedimientos efectivamente realizados.

Los criterios de aceptación definidos en la ERS que no hayan sido medidos experimentalmente se mantienen como **umbrales de aceptación** y no se presentan como resultados obtenidos.

En particular:

- No se reporta SUS si no fue aplicado.
- No se convierten criterios de aceptación en resultados experimentales.
- No se atribuyen pruebas técnicas posteriores a los participantes.
- No se presentan las correcciones del prototipo como una nueva validación humana.
- No se inventan DOI, SWHID, observaciones, participantes ni resultados.
- La validación humana y la verificación técnica del MVP se reportan de forma separada.

---

# 📚 Cómo citar el proyecto

La información bibliográfica se encuentra en:

```text
CITATION.cff
```

Para los componentes de investigación pueden utilizarse además los identificadores persistentes correspondientes:

**OSF**

```text
10.17605/OSF.IO/DTYNC
```

**Zenodo**

```text
10.5281/zenodo.22236373
```

---

# 🎓 Defensa Final

La defensa corresponde a la **Entrega 4 (2B)**.

Los materiales se encuentran en:

```text
09_Defensa/
```

La exposición se estructura alrededor de:

1. Problema y contribuciones.
2. Sistema y stakeholders.
3. Metodología del componente empírico.
4. Resultados.
5. Discusión y amenazas a la validez.
6. Conclusiones y trabajo futuro.
7. Demostración del prototipo.

Los resultados utilizados durante la defensa deben coincidir con los datos procesados y con el manuscrito final.

---

<div align="center">

## Universidad Técnica Estatal de Quevedo

### Facultad de Ciencias de la Computación
### Carrera de Ingeniería de Software

**Proyecto Fin de Curso — Ingeniería de Requerimientos (ISR-401)**

# SICM / MediCita

⭐ Repositorio elaborado con fines académicos.

</div>
