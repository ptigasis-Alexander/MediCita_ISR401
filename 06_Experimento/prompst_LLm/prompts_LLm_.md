
# 06_Experimento/prompst_LLm/

Registro de las 12 revisiones asistidas por IA (ChatGPT, GPT-5.6 Sol) ejecutadas sobre la documentación del proyecto, con su prompt, su respuesta y el registro estructurado que las vincula.

## Qué contiene

- `registro_uso_llm.csv` — tabla estructurada con las 12 revisiones: fecha, herramienta, modelo, actividad, fuentes consultadas, objetivo, archivos de prompt/salida, resultado resumido y estado.
- `LLM-P##_prompt.txt` — el prompt exacto usado en cada revisión (12 archivos).
- `LLM-P##_respuesta.txt` — la respuesta/resultado documentado de cada revisión (12 archivos).

## Índice de revisiones

| ID | Actividad | Estado |
|---|---|---|
| LLM-P01 | Revisión de consistencia del ERS/SRS | CORREGIDO_DOCUMENTALMENTE |
| LLM-P02 | Revisión de matriz de trazabilidad | CORREGIDO_DOCUMENTALMENTE |
| LLM-P03 | Trazado de observaciones a requisitos | EJECUTADO_CON_REVISION_HUMANA |
| LLM-P04 | Control de integridad de métricas | EJECUTADO |
| LLM-P05 | Control metodológico de SUS | NO_MEDIDO |
| LLM-P06 | Separación de líneas base 2B y PE5 | CONTROL_REQUERIDO |
| LLM-P07 | Revisión de requisitos de IA | VALIDACION_PENDIENTE |
| LLM-P08 | Revisión de supervisión humana de IA | VERIFICACION_FUTURA |
| LLM-P09 | Control de procedencia de evidencia | EJECUTADO |
| LLM-P10 | Control de sesiones pendientes | EJECUTADO |
| LLM-P11 | Control de rol de la IA en el experimento | EJECUTADO |
| LLM-P12 | Integridad verificable de archivos LLM | EJECUTADO |

## Nota de interpretación (según LLM-P11)

Estas revisiones se clasifican como **evidencia secundaria de proceso**: no cuentan como participante humano, entrevista ni minutos humanos del componente empírico. Cada archivo de respuesta incluye su propio control de interpretación: *"Este registro documenta una acción de revisión asistida por IA. No sustituye evidencia primaria ni demuestra por sí solo cumplimiento experimental."*
