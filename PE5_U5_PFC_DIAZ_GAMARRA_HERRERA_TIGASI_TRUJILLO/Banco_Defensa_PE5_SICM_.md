# 🏥 Banco de Defensa PE5 — SICM

> **Sistema de Gestión Inteligente para un Centro Médico (SICM)**  

> **Proyecto:** PE5 — Ingeniería de Requisitos  

> **Propósito:** Preparación para la defensa del proyecto

---

## 📌 Índice

1. [Frontera y contexto del sistema](#1-frontera-y-contexto-del-sistema)

2. [Proceso de desarrollo](#2-proceso-de-desarrollo)

3. [Requisitos y trazabilidad](#3-requisitos-y-trazabilidad)

4. [Verificación y defectos](#4-verificación-y-defectos)

5. [Impacto y línea base](#5-impacto-y-línea-base)

6. [Inteligencia Artificial](#6-inteligencia-artificial)

7. [Equidad y métricas](#7-equidad-y-métricas)

8. [Datos personales y asistencia de IA](#8-datos-personales-y-asistencia-de-ia)

---

# 1. 🌐 Frontera y contexto del sistema

## 1.1 ¿Cuál es la frontera del sistema?

### 💬 Respuesta

El **SICM incluye la gestión clínica y administrativa** del centro médico.

Quedan fuera de su alcance:

- ❌ Diagnóstico autónomo.

- ❌ Prescripción automática.

- ❌ Triaje de emergencia.

- ❌ Decisiones de acceso basadas en IA.

### 📚 Evidencia

- **Sección 3.1**

- **Sección 7**

---

## 1.2 ¿Qué diferencia hay entre contexto y límite?

### 💬 Respuesta

El **contexto** identifica los actores, procesos y entorno que interactúan con el sistema.

El **límite** determina qué responsabilidades pertenecen al SICM y cuáles quedan fuera de él.

### 🔑 Idea clave

| Concepto | ¿Qué define? |

|---|---|

| **Contexto** | Actores, procesos y entorno |

| **Límite** | Responsabilidades dentro y fuera del SICM |

### 📚 Evidencia

- **Secciones 1 y 3**

---

# 2. 🔄 Proceso de desarrollo

## 2.1 ¿Qué modelo de proceso siguieron?

### 💬 Respuesta

Se siguió un **proceso incremental PE1–PE5**, compuesto por:

1. **Elicitación**

2. **Especificación**

3. **Modelado**

4. **Validación**

5. **Gestión**

6. **Cierre cuantitativo**

### 📊 Resumen

```text
PE1
↓
Elicitación
↓
PE2
↓
Especificación
↓
PE3
↓
Modelado
↓
PE4
↓
Validación y gestión
↓
PE5
↓
Cierre cuantitativo
```
---

# 3. 🧩 Requisitos y trazabilidad

## 3.1 ¿Cómo garantizan que la matriz de trazabilidad esté completa end-to-end?

### 💬 Respuesta

La matriz PE5 registra, para cada uno de los **73 requisitos activos**, la cadena completa **Fuente → RF → CU → Clase UML → Proceso DFD → Estado → BDD → CP → Historia**. Las 73 filas quedan marcadas con "Estado de la traza: Completa"; no hay enlaces "por si acaso" ni celdas vacías. La matriz heredada de PE3 solo llegaba hasta CU y no registraba Clase, DFD, Estado ni CP, por lo que M4ade (trazabilidad adelante) partía de 0%.

### 📚 Evidencia

- **Sección 6.3** — Matriz end-to-end PE5
- **Anexo A.3** — Matriz de trazabilidad completa
- `matriz_trazabilidad_PE5.csv`

---

## 3.2 ¿Qué se hizo con los requisitos huérfanos y las cadenas rotas?

### 💬 Respuesta

Se identificaron cuatro patologías y se cerraron todas con causa y acción documentada (Tabla 7):

| Identificador | Causa inicial | Acción tomada |
|---|---|---|
| RF-16 | No tenía CU formal | Se creó CU-34, enlazado a US-35, clases de IA, P11, BDD y CP |
| RNF sin BDD | Solo se expresaban como métrica | Se creó un escenario BDD conceptual por RNF con su CP |
| RF de IA nuevos | No existían en la versión previa | Se añadieron con fuente explícita y trazas a RF/CU existentes |
| Matriz PE3 | Sin Clase, DFD, Estado ni CP | Se migró a la estructura PE5 completa |

### 📚 Evidencia

- **Sección 6.4** — Huérfanos y cadenas rotas (Tabla 7)
- **Sección 8.3** — Tabla de auditoría antes/después (M4ade, M4atr)

---

# 4. 🔍 Verificación y defectos

## 4.1 ¿Qué método de re-inspección aplicaron?

### 💬 Respuesta

Cada requisito se revisó contra cuatro preguntas fijas: (1) ¿existe un resultado observable o umbral?, (2) ¿está definida la unidad o el estado esperado?, (3) ¿hay un escenario o método de comprobación?, y (4) ¿podrían dos revisores llegar a interpretaciones distintas del mismo texto? Este método es el que sustenta M3 (verificabilidad) y M6 (corrección).

### 📚 Evidencia

- **Sección 5.1** — Método de re-inspección PE5
- **Sección 5.3** — Criterio de verificabilidad

---

## 4.2 ¿Qué defectos residuales encontraron y cómo los cerraron?

### 💬 Respuesta

La re-inspección encontró **diez defectos residuales de especificación**, principalmente solapamientos de alcance (textos que declaraban fusiones mientras mantenían identificadores activos, p. ej. RF-01/RF-14, RF-02/RF-36, RF-15/RF-31/RF-32) y RNF sin contabilizar correctamente. Antes de la corrección, M6 = 10/57 = 0,1754; después de cerrar los diez defectos y re-inspeccionar, M6 = 0/73 = 0,0000, cumpliendo el umbral ≤0,05. De forma similar, M2 (consistencia) pasó de 0,9937 —que numéricamente superaba 0,98 pero aún tenía 10 conflictos abiertos, por lo que **no podía declararse línea base final**— a 1,0000 con 0 conflictos abiertos.

### 📚 Evidencia

- **Sección 5.2** — Resultado de la re-inspección
- **Sección 8.3** — Tabla de auditoría antes/después (M2, M6)
- `instrumento_auditoria_PE5.csv`

---

# 5. 📊 Impacto y línea base

## 5.1 ¿Cómo se declara y controla la línea base PE5?

### 💬 Respuesta

La línea base PE5 es la **versión 4.0**, fechada 16/08/2026, que integra las cinco entregas previas (PE1 a PE5 + revisión 3.1). Se etiqueta en el repositorio como `baseline-pe5-v4.0`. El hash real de commit se registra una vez que estos archivos quedan publicados en el repositorio; no se declara un identificador antes de que exista el commit correspondiente.

### 📚 Evidencia

- **Historial de versiones** (carátula del informe)
- **Sección 6.1** — Línea base y control de cambios

---

## 5.2 ¿Qué mide M5 (modificabilidad) y por qué importa?

### 💬 Respuesta

M5 estima cuántos requisitos se ven afectados, en promedio, cuando cambia uno representativo. Se tomó una muestra de cinco requisitos de dominios distintos —RF-02 (citas), RF-09 (autenticación), RF-15 (inventario), RF-26 (signos vitales) y RF-16 (asistente IA)— con impactos de 3, 3, 2, 2 y 4 requisitos respectivamente: (3+3+2+2+4)/5 = **2,8**, por debajo del umbral ≤3,0. Esto respalda que la especificación no genera cambios en cascada descontrolados.

### 📚 Evidencia

- **Sección 8.3** — Tabla de auditoría antes/después (M5)
- `instrumento_auditoria_PE5.csv`

---

# 6. 🤖 Inteligencia Artificial

## 6.1 ¿Qué componentes de IA tiene el SICM y qué NO hacen?

### 💬 Respuesta

Hay dos componentes, ambos limitados a **apoyo administrativo**:

- **IA-01 — Asistente virtual administrativo**: responde preguntas frecuentes (horarios, servicios, ubicación, uso del sistema) y deriva a recepción cuando la consulta es clínica, ambigua o requiere historial.
- **IA-02 — Predictor de riesgo de inasistencia**: estima un puntaje de riesgo (0-1) para adaptar la intensidad de los recordatorios de citas.

Ninguno diagnostica, prescribe, hace triaje de emergencia ni decide si una persona recibe atención. El resultado de IA-02 nunca cancela una cita ni reduce su prioridad clínica.

### 📚 Evidencia

- **Sección 7.1** — Principio de diseño
- **Sección 7.3 / 7.4** — IA-01 / IA-02

---

## 6.2 ¿Cómo se garantiza la supervisión humana?

### 💬 Respuesta

Cada componente tiene un mecanismo de *fallback* a una persona: IA-01 deriva a recepción ante baja confianza o consulta fuera de alcance; IA-02 permite que recepción visualice el nivel de riesgo, lo desactive para una cita puntual y aplique manualmente una estrategia de recordatorio, dejando registro de auditoría (RF-IA2-03). Ambos se monitorean mensualmente (macro-F1, F1, latencia, brechas de equidad) con umbrales que, si se incumplen, activan revisión o reentrenamiento.

### 📚 Evidencia

- **Sección 7.3 / 7.4** — Monitoreo de IA-01 e IA-02
- **Sección 7.5** — Privacidad, ética y supervisión humana

---

# 7. ⚖️ Equidad y métricas

## 7.1 ¿Cómo definieron los umbrales de equidad?

### 💬 Respuesta

Para IA-01: la diferencia de tasa de resolución correcta entre usuarios de 18-35 años y mayores de 60, y entre usuarios de baja y alta familiaridad digital, no debe superar **5 puntos porcentuales** (RNF-IA1-E01/E02). Para IA-02: la diferencia de sensibilidad por grupo etario y la diferencia de falsos positivos entre pacientes nuevos y recurrentes tampoco deben superar 5 puntos porcentuales (RNF-IA2-E01/E02). La explicabilidad se exige en ambos: IA-01 debe justificar una derivación en ≤40 palabras y ≤2 s con al menos 80% de aprobación de usuarios (RNF-18); IA-02 debe mostrar al menos dos factores administrativos ante un riesgo medio/alto (RNF-IA2-X01).

### 📚 Evidencia

- **Tabla 9** — Requisitos y umbrales de IA-01
- **Tabla 10** — Requisitos y umbrales de IA-02

---

## 7.2 ¿Los valores de F1, macro-F1 y disponibilidad ya se midieron?

### 💬 Respuesta

No. La PE5 distingue explícitamente entre dos tipos de valor: **M1-M6 son resultados reales de auditoría documental** (se calculan sobre el ERS, la matriz y la re-inspección, y sí están medidos). En cambio, macro-F1 ≥0,90, F1 ≥0,80, latencia y disponibilidad son **umbrales de aceptación** que los componentes de IA deberán alcanzar cuando se implementen y prueben; se declaran como "especificado, pendiente de validación experimental" y no se atribuye a ningún modelo un desempeño que aún no se ha medido.

### 📚 Evidencia

- **Sección 7.2** — Criterio de interpretación de métricas y evidencia (Tabla 8)
- **Sección 8.1** — Distinción entre auditoría documental y pruebas del producto

---

# 8. 🔐 Datos personales y asistencia de IA

## 8.1 ¿Qué datos usa cada componente de IA y bajo qué marco legal?

### 💬 Respuesta

IA-01 se entrena solo con horarios, catálogo de servicios y preguntas frecuentes aprobadas; **no usa historias clínicas**, y los registros de conversación para mejora deben anonimizarse o seudonimizarse. IA-02 usa únicamente variables administrativas (anticipación de reserva, historial de asistencia, área, franja horaria, confirmación del recordatorio); diagnósticos y notas clínicas quedan fuera del conjunto de características. El marco legal aplicado es la **LOPDP de Ecuador** (finalidad, minimización, seguridad, trazabilidad) y el **Reglamento (UE) 2024/1689**, cuyo Artículo 50 exige que un sistema que interactúa directamente con personas se identifique como IA — por eso el asistente debe declararse como tal ante el usuario.

### 📚 Evidencia

- **Sección 7.3 / 7.4** — Datos de IA-01 / IA-02
- **Sección 7.5** — Privacidad, ética y supervisión humana

---

## 8.2 ¿Cómo declararon el uso de IA en la elaboración del propio informe?

### 💬 Respuesta

El Anexo E documenta, por sección, qué se usó asistencia de IA y qué validación exige cada uso: reorganización de la estructura (validada contra la Guía y Rúbrica PE5), corrección de redacción del ERS (validada contra RF/RNF y evidencia originales), construcción de columnas de trazabilidad (cada enlace debe confirmarse contra UML/DFD/estados reales antes de etiquetar la línea base), propuesta de los dos componentes de IA (el equipo valida alcance y que los umbrales sean probables), aritmética de métricas (recontar los 57/73 requisitos antes de entregar) y revisión de claridad de las conclusiones. En ningún caso la IA sustituye el análisis o la decisión del equipo.

### 📚 Evidencia

- **Anexo E** — Referencias y declaración de uso de IA
