<div align="center">

# 🤖 A9 — Declaración de Uso de IA

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completado-Green?style=for-the-badge)
![Herramientas](https://img.shields.io/badge/Herramientas-GPT--5.6_Sol_%2B_Claude_Sonnet_5-6e56cf?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-12/09/2026-informational?style=for-the-badge)

</div>

---

## 📌 Cómo leer esta tabla

- **Herramienta:** nombre y modelo exacto usado.
- **Para qué:** tarea concreta realizada.
- **Quién verificó:** integrante humano responsable de revisar el resultado antes de aceptarlo.
- **Método de verificación:** cómo se confirmó que el resultado era correcto antes de incorporarlo.

> ✅ **Nota de confirmación:** la ejecución de los 12 usos de ChatGPT registrados en `registro_uso_llm.csv` fue confirmada directamente por Paul Alexander Tigasi Sampedro como propia, dado que comparten la misma marca de tiempo (`2026-08-29T19:44:50+00:00`) correspondiente a su sesión de corrección documental de esa fecha.

---

## 1️⃣ Revisión documental asistida por IA — ChatGPT / GPT-5.6 Sol 

Fuente: [`06_Experimento/prompst_LLm/registro_uso_llm.csv`](../06_Experimento/prompst_LLm/registro_uso_llm.csv) (registro completo con prompt, respuesta y hash SHA-256 por cada uso).

| Sección/artefacto revisado | Para qué se usó | Quién verificó | Método de verificación |
|---|---|---|---|
| ERS/SRS 2B — identificadores RF/RNF | Detectar contradicciones internas de conteos y definiciones | Paul Alexander Tigasi Sampedro | Revisión manual de los identificadores señalados antes de aceptar el cambio |
| Matriz de trazabilidad | Contrastar relaciones RF/RNF contra el catálogo vigente | Paul Alexander Tigasi Sampedro | Revisión manual de las filas corregidas |
| Ficha de observación → trazado a requisitos | Relacionar observaciones con RF/RNF sin inventar datos | Paul Alexander Tigasi Sampedro | Contraste contra las transcripciones originales |
| Control de integridad de métricas (SUS, IA) | Verificar que umbrales no se presenten como resultados medidos | Paul Alexander Tigasi Sampedro | Revisión cruzada contra el protocolo registrado |
| Control metodológico de SUS | Verificar si SUS fue realmente aplicado | Paul Alexander Tigasi Sampedro | Revisión de la ficha de observación disponible |
| Separación de líneas base 2B y PE5 | Evitar fusión silenciosa de líneas base distintas | Paul Alexander Tigasi Sampedro | Revisión manual de ambas líneas base |
| Revisión de requisitos de IA (equidad, monitoreo, explicabilidad) | Distinguir especificación de evidencia experimental real | Paul Alexander Tigasi Sampedro | Revisión manual de cada RNF de IA |
| Supervisión humana de IA | Identificar controles a verificar cuando exista implementación | Paul Alexander Tigasi Sampedro | Revisión manual del listado de controles |
| Control de procedencia de evidencia | Evitar mezclar elicitación (ELI-\*) con validación (OBS-\*) | Paul Alexander Tigasi Sampedro | Revisión cruzada contra el manifiesto de evidencia |
| Control de sesiones pendientes | Evitar completar observaciones sin evidencia real | Paul Alexander Tigasi Sampedro | Revisión contra el manifiesto de transcripciones |
| Rol de la IA en el experimento | Definir si la revisión cuenta como participante/entrevista | Paul Alexander Tigasi Sampedro | Decisión documentada: no cuenta como participante ni minutos humanos |
| Integridad de archivos LLM | Generar SHA-256 de los registros de uso de IA | Paul Alexander Tigasi Sampedro | Verificación de que los hashes coinciden con los archivos actuales |

> Ninguno de estos 12 usos cuenta como participante, entrevista o minutos humanos — son revisión documental de consistencia, no generación de datos de campo ni de resultados experimentales (declarado así en el registro original).

---

## 2️⃣ Redacción de documentos y análisis de datos recolectados — uso combinado GPT-5.6 Sol + Claude Sonnet 5

| Actividad | Herramientas usadas | Quién participó / verificó | Método de verificación |
|---|---|---|---|
| Redacción y elaboración de documentos | ChatGPT (GPT-5.6 Sol) y Claude Sonnet 5 (Anthropic) | Los 5 integrantes del equipo (Paul Alexander Tigasi Sampedro, Steven Santiago Díaz Pontón, Jamileth Estefanía Gamarra Zárate, Thais Melanie Herrera Ramos, Mayummy Jailly Trujillo Vega) | No aplica (actividad de redacción, no de verificación) |
| Verificación y análisis de coherencia de los datos generados | ChatGPT (GPT-5.6 Sol) y Claude Sonnet 5 (Anthropic) | Steven Santiago Díaz Pontón (principal) y Paul Alexander Tigasi Sampedro | Se revisó lo que ya se tenía contra lo que generaba cada herramienta, verificando si existía coherencia o relación exacta con los datos originales. Adicionalmente, se contrastó cruzando la respuesta de una herramienta contra la opinión de la otra (de ChatGPT a Claude y viceversa) antes de aceptar cualquier contenido. |

---

## 3️⃣ Asistencia de IA en la corrección final del repositorio — Claude Sonnet 5 (Anthropic), agosto-septiembre 2026

> **Sobre la columna "Quién verificó":** la interacción directa con la IA la realizó Paul Alexander Tigasi Sampedro. Sin embargo, los cambios propuestos no se aceptaron de forma unilateral: cada integrante revisaba el repositorio en sus propios días, se discutían los cambios en conjunto y se comparaban criterios entre todos antes de darlos por definitivos. Por eso cada fila indica ambos niveles: quién interactuó directamente con la IA, y que la validación final fue colectiva.

| Tarea | Para qué se usó | Quién verificó | Método de verificación |
|---|---|---|---|
| Auditoría del repositorio contra la Guía de Desarrollo | Contrastar el estado real del repositorio contra la guía y el informe del docente | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Verificación directa sobre el repositorio clonado (conteos, hashes, compilación real del LaTeX) |
| Redacción de RNF-19 (equidad) y RNF-20 (monitoreo) | Especificar dos requisitos no funcionales exigidos por la guía, no declarados previamente | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Revisión de que la métrica y el umbral fueran razonables para el dominio del proyecto; compilación real del documento sin errores |
| Corrección de rutas en `run_all.py` | Reparar el pipeline tras mover archivos de `06_Experimento` a `07_Datos` | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Ejecución real del script, confirmando que reproduce las mismas cifras ya publicadas en el manuscrito |
| Migración de evidencia audiovisual a GitHub Release | Reducir el peso de clonado del repositorio sin eliminar evidencia | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Verificación de que los hashes SHA-256 del Release coinciden con `fichas_tecnicas.csv` |
| Redacción de plantillas de `10_Autoria/` (A8, A9, A10) | Generar el formato exigido por la guía, con datos reales del historial de Git y de los documentos de correspondencia | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste de las cifras (commits, fechas) contra `git log` y contra los PDF originales directamente |
| Redacción de oficios corregidos (Oficio de Respaldo, Aval CategoriaA_A3) | Actualizar los 5 integrantes del equipo y corregir la inconsistencia de nombre de firmante | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste línea por línea contra el texto original antes de aceptar cada cambio |

---

## 4️⃣ Secciones/artefactos donde NO se usó ninguna herramienta de IA

| Actividad | Responsable(s) |
|---|---|
| Recolección de datos en campo (entrevistas, observación del walkthrough) | Equipo completo, en persona |
| Firma de consentimientos y trámites institucionales (solicitudes, avales) | Paul Alexander Tigasi Sampedro,  Steven Santiago Díaz Pontón ,Thais Melanie Herrera Ramos |

---

## 5️⃣ Corrección final del repositorio tras la revisión de cierre — Claude Sonnet 5 (Anthropic), 09-12/09/2026

> **Sobre la columna "Quién verificó":** igual que en la sección 3️⃣, la interacción directa con la IA la realizó Paul Alexander Tigasi Sampedro; los cambios se discutieron y validaron en conjunto con el equipo antes de aceptarlos como definitivos.

| Tarea | Para qué se usó | Quién verificó | Método de verificación |
|---|---|---|---|
| Redacción de la sección "Alcance del componente de IA y requisitos que no aplican" | Declarar explícitamente que RF-02/RF-13 no son un componente de IA y que el requisito de "asignación/recomendación automática de cita" no aplica al sistema | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Revisión línea por línea de RF-02 y RF-13 contra la especificación real, sin modelo ni métrica de acierto |
| Redacción de RNF-21 (supervisión humana) y RNF-22 (clasificación del nivel de riesgo) | Completar los seis requisitos del componente inteligente exigidos por la guía de cierre | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Revisión de que la métrica y el umbral fueran razonables para el dominio; compilación real del documento sin errores (xelatex + bibtex, 3 pasadas) |
| Reescritura de RNF-19 (equidad), re-enfocado de RF-02/RF-13 a RF-16 | Corregir la referencia errónea a un componente que no es de IA | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste contra el único componente de IA real del sistema (RF-16) |
| Corrección de un `\begin{quote}` sin cerrar en `ERS_SRS_2B_V2.0.tex` | Reparar una falla de compilación que afectaba la reproducibilidad documental (P2) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Recompilación real del documento, confirmando 0 errores |
| Corrección de las filas 71, 73 y 74 de `matriz_trazabilidad_ACTUALIZADA.csv` | Sincronizar la matriz con la corrección de RNF-19 y agregar RNF-21/RNF-22 | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste manual contra la tabla equivalente ya corregida dentro del ERS |
| Redacción de finalidad y plazo de conservación en `CategoriaA_A4_Referencia_LOPDP.pdf` | Completar los cuatro elementos exigidos por el ítem B6 (base de licitud, finalidad, plazo, responsable) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Revisión de que el plazo declarado (6 meses tras la defensa) fuera razonable para el equipo |
| Diseño de las plantillas y el script de la doble observación independiente (`10_Autoria/doble_observacion_sesiones/`) | Cubrir el ítem B4 (kappa entre dos observadores independientes sobre el 20% de las sesiones de validación) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | El script se probó verificando que se niega a calcular el Kappa si falta algún juicio del segundo observador |
| Cálculo de la tabla de duración por sesión en `ficha_observacion.csv` y del perfil agregado de participantes (`perfil_agregado_participantes.csv`) | Completar los datos de duración y el perfil agregado exigidos por B3, cruzando `fuente_evidencia` contra `fichas_tecnicas.csv` ya verificado | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Cruce por nombre de archivo contra el inventario técnico ya verificado con hash SHA-256; dos asignaciones de menor certeza (VAL-COORD, VAL-PAC) quedaron marcadas para confirmación del equipo |

> **Nota importante:** el contenido observacional en sí (qué se completó, qué incidente se registró en cada tarea del walkthrough, el juicio del segundo observador) fue producido por integrantes del equipo viendo directamente los videos de validación — la IA no generó, sugirió ni completó ningún juicio de observación de campo.

---

## ✍️ Firma de los integrantes



| Integrante | Firma | Fecha |
|---|---|---|
| Paul Alexander Tigasi Sampedro | Alexander Sampedro | 03/09/2026 17:29 |
| Steven Santiago Díaz Pontón | Steven Diaz | 12/09/2026 0:14 |
| Jamileth Estefanía Gamarra Zárate | Jamileth Gamarra | 12/09/2026 0:17 |
| Thais Melanie Herrera Ramos | Herrera Thais | 12/09/2026 0:16|
| Mayummy Jailly Trujillo Vega |Trujillo Mayummy |12/09/2026 0:15 |
