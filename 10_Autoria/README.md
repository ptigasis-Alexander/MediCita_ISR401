
# 10_Autoria — Evidencia de autoría y trabajo propio

Índice del estado real de cada elemento exigido por la Sección 6 de la
Guía de Desarrollo del 02/09/2026. Ningún elemento marcado como
"pendiente" contiene contenido inventado — se deja vacío hasta que el
equipo aporte la evidencia real correspondiente.

| Cód. | Elemento | Estado | Notas |
|---|---|---|---|
| A1 | `bitacora_sesiones.csv` | **Generado parcialmente** | 16 filas, una por cada día real con commits en el historial (21/07/2026 a 03/09/2026), con participantes y hashes de commit reales extraídos de `git log`. Las columnas `hora_inicio`, `hora_fin`, `modalidad` y `decisiones_tomadas` quedan como `PENDIENTE` — eso solo lo puede completar el equipo, no se puede derivar del historial de Git. |
| A2 | `capturas/` | **Pendiente** | Requiere que cada integrante tome mínimo 3 capturas de pantalla propias con el formato `AAAA-MM-DD_usuario_artefacto.png`, mostrando la herramienta abierta, el reloj del sistema y el nombre de sesión de usuario. |
| A3 | Fuentes editables de diagramas | **Pendiente de verificar** | Revisar que `03_Modelado/Diagramas_UML_Corregidos/` y `03_Modelado/Mockups_Prototipo_Final/` contengan el archivo fuente editable (no solo la imagen exportada) de cada diagrama. |
| A4 | `grabaciones/` | **Pendiente** | Requiere al menos 2 grabaciones reales de 10 a 15 minutos de sesión de trabajo en equipo, con pantalla compartida. |
| A5 | `notas_campo/` | **Pendiente** | Requiere notas manuscritas escaneadas de cada sesión de elicitación, con fecha visible. |
| A6 | `fotos_equipo/` | **Pendiente** | Requiere fotografías del equipo en la organización, con al menos 2 integrantes identificables y metadatos de fecha conservados. |
| A7 | `doble_codificacion/` | **Pendiente** | Requiere las dos hojas de codificación de dos integrantes distintos sobre el mismo subconjunto del corpus, más el coeficiente de acuerdo con intervalo de confianza calculado por script. |
| A8 | `correspondencia/` | **Pendiente de verificar** | Puede existir ya contenido reutilizable en `08_Etica/` (ej. `A6_Declaracion_Conflicto_Intereses.pdf`, `Oficio_Respaldo_Institucional_DGDS.pdf`) — revisar si corresponde copiarlo aquí o si falta correspondencia adicional fechada. |
| A9 | `declaracion_uso_ia.md` | **Pendiente** | Debe cubrir todas las secciones del documento, incluidas aquellas donde no se usó ninguna herramienta de IA. |
| A10 | `aporte_individual.md` | **Pendiente** | Debe estar firmado por los 5 integrantes. Puede apoyarse en el conteo real de commits por autor ya verificado (ver tabla abajo). |
| A11 | `exif_inventario.csv` | **Pendiente** | Requiere nombre, fecha de captura (de metadatos EXIF reales), dispositivo y hash por cada fotografía del proyecto. |
| A12 | `.mailmap` | **✅ Completo** | Ya existe en la raíz del repositorio, con la atribución de los 8 commits de `MediCita Team` a Thais Melanie Herrera Ramos. |

## Dato de referencia para A10 (aporte_individual.md)

Conteo real de commits por autor, con `.mailmap` ya aplicado (ventana
completa del historial):

| Integrante | Commits |
|---|---|
| Paul Alexander Tigasi Sampedro | 278 |
| Mayummy Jailly Trujillo Vega | 236 |
| Steven Santiago Díaz Pontón | 214 |
| Jamileth Estefanía Gamarra Zárate | 204 |
| Thais Melanie Herrera Ramos | 203 (195 propios + 8 atribuidos vía `.mailmap`) |
