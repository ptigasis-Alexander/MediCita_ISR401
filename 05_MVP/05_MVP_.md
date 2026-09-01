<div align="center">

# 💻 MVP — SICM (Sistema de Gestión Inteligente para un Centro Médico)

### Demostración guiada, prototipo final revisado y accesible en vivo

**Proyecto Fin de Curso (PFC) – Ingeniería de Requisitos (ISR-401)**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Publicado-success?style=for-the-badge)
![Validacion](https://img.shields.io/badge/Validacion-Walkthrough-success?style=for-the-badge)
![Tecnologia](https://img.shields.io/badge/Tecnologia-HTML_%2F_CSS_%2F_JS-00509d?style=for-the-badge)

</div>

---

## 🔗 Enlace directo (revisar aquí)

<div align="center">

### 👉 [Abrir demostración del MVP](https://ptigasis-alexander.github.io/MediCita_ISR401/)

</div>

Este enlace es **público**, no requiere instalación ni cuenta de GitHub y funciona directamente desde el navegador.

La demostración publicada permite revisar los principales módulos y flujos del sistema SICM mediante una presentación automática con narración y navegación simulada.

> **Importante:** GitHub Pages publica actualmente el contenido de `05_MVP` como raíz del sitio. Por este motivo, el enlace correcto es el indicado anteriormente y no la antigua ruta `/05_MVP/`.

---

## 📖 Qué es este MVP

Es una **demostración guiada y autoreproducible** del sistema SICM.

Simula la navegación por las principales interfaces del sistema y permite observar el flujo de atención de diferentes usuarios y áreas del centro médico.

La demostración fue **actualizada después del proceso de validación walkthrough**, incorporando las principales observaciones identificadas durante las sesiones con los participantes.

La demostración tiene una duración aproximada de:

### ⏱️ 5 minutos — 300 segundos — 20 escenas

Entre los módulos y procesos representados se encuentran:

- Inicio de sesión y control por roles
- Gestión de pacientes
- Agendamiento de citas
- Recepción
- Recaudación y pagos
- Enfermería
- Medicina General
- Historia clínica
- Recetas médicas
- Odontología
- Psicología
- Nutrición
- Terapia Física
- Derivaciones
- Notificaciones
- Coordinación
- Reportes
- Auditoría

---

## 🎮 Controles disponibles

La demostración incluye los siguientes controles:

- 🔊 Activar / silenciar la narración
- ⏸️ Pausar / reanudar la demostración
- ⛶ Pantalla completa
- 🔠 `A+` para aumentar el tamaño del texto

La narración utiliza las capacidades disponibles en el navegador para acompañar automáticamente cada una de las escenas.

---

## 🖥️ Prototipo final revisado

Además de la demostración guiada, esta carpeta contiene la **versión final revisada del prototipo del sistema SICM**.

Este prototipo corresponde a la versión obtenida después del proceso de:

**Prototipo inicial → Validación Walkthrough → Observaciones → Correcciones → Prototipo final revisado**

El objetivo fue incorporar las observaciones de los participantes **sin modificar de forma radical la estructura ni las interfaces originales del sistema**.

Por lo tanto, se conservaron:

- distribución general de los módulos;
- menú lateral;
- estructura de navegación;
- identidad visual;
- organización por roles;
- flujo general de atención.

Las modificaciones se concentraron principalmente en funcionalidades, campos, mensajes, accesibilidad y necesidades detectadas durante la validación.

---

## ✅ Mejoras incorporadas después de la validación

Entre las principales mejoras incorporadas al prototipo final y representadas en la demostración se encuentran:

- identificación mediante **cédula o pasaporte**;
- consideración de pacientes menores de edad;
- información de representante legal cuando corresponde;
- teléfono de contacto de emergencia;
- mensajes de confirmación más claros;
- control `A+` para mejorar la legibilidad;
- selección de profesional al solicitar una cita;
- visualización más clara de horarios disponibles;
- agenda por día, semana y mes;
- consulta de pagos y comprobantes;
- registro de frecuencia respiratoria;
- registro de saturación de oxígeno;
- notas y procedimientos de Enfermería;
- historia clínica filtrable por especialidad;
- antecedentes psicológicos previos;
- objetivo terapéutico en Psicología;
- mejoras en el registro de Terapia Física;
- número y duración de sesión;
- prioridad de atención;
- registro de ejercicios realizados;
- derivaciones con área de origen y destino;
- contexto clínico para el área receptora;
- apoyo de accesibilidad mediante dictado por voz;
- gestión de profesionales y horarios desde Coordinación;
- reportes automáticos por área;
- mejoras en notificaciones y trazabilidad.

---

## 💊 Flujo de recetas médicas

La versión revisada representa el flujo de medicamentos solicitado durante el desarrollo y validación del sistema.

Los profesionales autorizados de:

- **Medicina General**
- **Odontología**

pueden registrar una receta médica.

Una vez registrada, la receta se envía al área de **Enfermería**.

Enfermería puede consultar:

- paciente;
- medicamento;
- dosis;
- frecuencia;
- cantidad;
- indicaciones.

Después de entregar el medicamento al paciente, Enfermería puede marcarlo como:

### ✅ Medicamento entregado

De esta manera se mantiene la trazabilidad entre la prescripción y la entrega del medicamento.

---

## 🏥 Áreas y roles representados

El MVP representa los principales actores y áreas definidas para SICM:

| Rol / Área | Funciones representadas |
|---|---|
| 👤 Paciente | Datos personales, citas, pagos y consulta de información |
| 🗂️ Recepción | Registro, búsqueda de pacientes y gestión de citas |
| 💳 Recaudación | Registro de pagos y comprobantes |
| 💉 Enfermería | Triage, signos vitales, notas y entrega de medicamentos |
| 🩺 Medicina General | Atención, historia clínica y recetas |
| 🦷 Odontología | Odontograma, procedimientos y recetas |
| 🧠 Psicología | Antecedentes, evolución y objetivos terapéuticos |
| 🥗 Nutrición | Evaluación y seguimiento nutricional |
| 🦵 Terapia Física | Sesiones, ejercicios, duración y evolución |
| ⚙️ Coordinación | Profesionales, horarios, permisos y supervisión |

---

## 📊 Reportes y trazabilidad

El prototipo contempla reportes generados a partir de la información registrada durante las atenciones.

Se representan indicadores correspondientes a diferentes áreas, entre ellas:

- Medicina General
- Odontología
- Enfermería
- Psicología
- Nutrición
- Terapia Física

También se representa un registro de auditoría para mantener trazabilidad sobre determinadas operaciones realizadas dentro del sistema.

---

## 🧪 Relación con la Validación Walkthrough

Las modificaciones realizadas no corresponden únicamente a cambios visuales.

Las mejoras fueron incorporadas considerando las observaciones obtenidas durante las sesiones de **Validación Walkthrough**.

Las evidencias correspondientes a este proceso se encuentran documentadas dentro del repositorio.

El flujo de trabajo seguido fue:

```text
Requisitos
    ↓
Prototipo inicial
    ↓
Validación Walkthrough
    ↓
Observaciones de participantes
    ↓
Análisis de resultados
    ↓
Correcciones
    ↓
Prototipo final revisado
    ↓
MVP actualizado
```

Esto permite mantener coherencia entre:

- requisitos;
- validación;
- observaciones;
- interfaces;
- prototipo;
- MVP;
- trazabilidad.

---

## ⚠️ Alcance del MVP

El MVP publicado es una **simulación interactiva autocontenida** desarrollada con HTML, CSS y JavaScript.

Su objetivo es demostrar visualmente el comportamiento esperado del sistema.

Por tratarse de un prototipo académico:

- no utiliza una base de datos clínica de producción;
- no almacena información médica real;
- no procesa pagos reales;
- no sustituye un sistema médico productivo;
- los datos mostrados son simulados;
- algunas operaciones representan el comportamiento esperado del sistema.

---

## 🤖 Instrucción para revisión por IA

Si se desea realizar una revisión asistida por IA, puede utilizarse la siguiente instrucción:

> "Abre `https://ptigasis-alexander.github.io/MediCita_ISR401/`, revisa la demostración guiada del sistema SICM e identifica los módulos y funcionalidades representados. Contrasta la demostración y el prototipo final revisado con las evidencias de Validación Walkthrough del repositorio, indicando qué observaciones fueron incorporadas y verificando que la página cargue correctamente sin errores 404 ni recursos CSS/JS rotos."

---

## 🧪 Cómo verificar que está correctamente publicado

```bash
curl -I https://ptigasis-alexander.github.io/MediCita_ISR401/
```

La respuesta esperada es:

```text
HTTP/2 200
```

La publicación se realiza mediante **GitHub Actions**, utilizando únicamente los archivos necesarios de la carpeta `05_MVP`.

> Si se presenta un problema de publicación, revisar **Actions → Deploy MediCita MVP** y comprobar que la ejecución más reciente finalice con estado `Success`.

---

## 📂 Archivos de esta carpeta

| Archivo | Función |
|---|---|
| [`index.html`](index.html) | Estructura de la demostración guiada |
| [`style.css`](style.css) | Diseño visual, componentes y animaciones |
| [`script.js`](script.js) | Reproducción automática, escenas, narración y controles |
| [`05_MVP_.md`](05_MVP_.md) | Documentación del MVP y de la versión revisada |
| `MediCita_prototipo_final_actualizado.html` | **Prototipo final revisado después de la Validación Walkthrough** |

> El prototipo final permite realizar una revisión más detallada de las interfaces y funcionalidades, mientras que la demostración guiada presenta los principales flujos del sistema de manera automática.

---

## 🔍 Orden recomendado de revisión

Para evaluar esta sección del repositorio se recomienda:

1. Abrir la **demostración publicada en GitHub Pages**.
2. Ejecutar los **5 minutos de la demostración guiada**.
3. Revisar el **prototipo final actualizado**.
4. Consultar las evidencias de **Validación Walkthrough**.
5. Contrastar las observaciones con las mejoras incorporadas.
6. Revisar la trazabilidad con los requisitos correspondientes.

---

## 🛠️ Tecnologías utilizadas

- HTML5
- CSS3
- JavaScript
- Web Speech API
- GitHub Pages
- GitHub Actions

---

<div align="center">

## 📌 Estado actual

### ✅ Demostración guiada actualizada

### ✅ Prototipo final revisado

### ✅ Mejoras de Validación Walkthrough incorporadas

### ✅ GitHub Pages publicado

### ✅ Acceso público

<br>

## Universidad Técnica Estatal de Quevedo

### Facultad de Ciencias de la Computación

### Carrera de Ingeniería de Software

### Proyecto Fin de Curso

**Sistema de Gestión Inteligente para un Centro Médico (SICM)**

---

⭐ **Documento elaborado con fines exclusivamente académicos.**

</div>
