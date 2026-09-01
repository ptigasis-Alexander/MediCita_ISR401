<div align="center">

# 🔍 Guía de Verificación — Carpeta Cuestionario

### Sistema de Gestión Inteligente para un Centro Médico (SICM)

**Proyecto Fin de Curso (PFC) – Ingeniería de Requisitos**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Carpeta](https://img.shields.io/badge/Carpeta-02__Evidencias%2FCuestionario-00509d?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Checklist_de_Verificacion-2e7d32?style=for-the-badge)
![Uso](https://img.shields.io/badge/Uso-Revision_Manual_o_IA-orange?style=for-the-badge)
</div>

---

## 🎯 Propósito de este documento

Guía paso a paso para confirmar que la evidencia del **cuestionario aplicado a usuarios y pacientes** está completa, bien organizada y sin errores antes de la entrega. Pensada para que la siga un revisor humano o un asistente de IA.

---

## 📁 Estructura verificada

```
02_Evidencias/
└── Cuestionario/
    ├── Cuestionario_.md                        ← este documento
    ├── Fotos_Aplicacion/
    │   └── 5 capturas de aplicación en campo
    └── Respuestas/
        ├── Resultado_Cuestionario_IR_SGICM.csv   ← datos crudos (66 filas, 35 columnas)
        └── Respuestas_cuestionario.md            ← resumen y análisis de resultados
```

Estado verificado el 01/09/2026: `Fotos_Aplicacion/` y `Respuestas/` **ya están correctamente anidadas** dentro de `Cuestionario/`, no como carpetas hermanas. La jerarquía cumple con la estructura obligatoria de la Sección 9.1 de la guía.

---

## 🧪 Verificación realizada sobre el CSV real

Se abrió `Resultado_Cuestionario_IR_SGICM.csv` con el módulo `csv` de Python (delimitador `;`, codificación `utf-8-sig`) y se confirmó:

| Verificación | Resultado |
|---|---|
| Codificación del archivo | UTF-8 real (verificado con `file`), sin símbolos rotos |
| Filas de datos | 66 (coincide con lo declarado en `Respuestas_cuestionario.md`) |
| Columnas totales | 35 (`Marca temporal`, `Codigo_Participante` + 33 preguntas) |
| Rango de fechas | 13/06/2026 – 29/07/2026, coincide con lo declarado |
| Preguntas con 0 respuestas | 5 (dispositivo, conexión a internet, seguro médico, uso de apps similares, comodidad con apps) — correctamente marcadas como n=0 en el resumen, no se inventó ningún valor para ellas |
| Preguntas con muy pocas respuestas | 2 ("interfaces intuitivas" n=6, "recomendaría el centro" n=1) — marcadas con advertencia explícita en el resumen por su tamaño de muestra insuficiente |

### Cómo repetir esta verificación

```bash
cd 02_Evidencias/Cuestionario/Respuestas
python3 -c "
import csv
with open('Resultado_Cuestionario_IR_SGICM.csv', encoding='utf-8-sig') as f:
    r = list(csv.reader(f, delimiter=';'))
print('Filas de datos:', len(r)-1)
print('Columnas:', len(r[0]))
"
```

---

## ⚠️ Pendiente real (no de formato, de verificabilidad)

El enlace al formulario de Google Forms que respalda este cuestionario está en modo `/edit`, lo que **requiere iniciar sesión con la cuenta propietaria**. Ni el tribunal ni un tercero pueden abrirlo para confirmar las preguntas exactas del instrumento. Se recomienda exportar el formulario a PDF (Google Forms → menú ⋮ → Imprimir formulario, o Ctrl+P desde la vista previa) y guardarlo en `06_Experimento/instrumentos/cuestionario_SGICM.pdf`, de forma que el instrumento quede archivado de forma independiente y verificable sin depender de una cuenta de Google.

---

## ✅ Checklist de Aprobación

- [x] `Fotos_Aplicacion/` y `Respuestas/` están anidadas dentro de `Cuestionario/`
- [x] El CSV y el `.md` de resultados están en UTF-8 real, verificado
- [x] `Fotos_Aplicacion/` contiene 5 imágenes reales
- [x] El número de filas del CSV (66) coincide con lo declarado en `Respuestas_cuestionario.md`
- [x] Las preguntas con 0 o muy pocas respuestas están marcadas explícitamente, no omitidas ni infladas
- [ ] **Pendiente:** copia en PDF del instrumento (formulario) archivada en `06_Experimento/instrumentos/`, independiente del enlace de Google Forms

---

<div align="center">

## Universidad Técnica Estatal de Quevedo

### Facultad de Ciencias de la Computación

### Carrera de Ingeniería de Software

### Proyecto Fin de Curso

**Sistema de Gestión Inteligente para un Centro Médico (SICM)**

---

⭐ **Documento elaborado con fines exclusivamente académicos.**

</div>

