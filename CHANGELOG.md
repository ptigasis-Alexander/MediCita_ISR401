# Historial de cambios

Todos los cambios relevantes del proyecto se documentan en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto utiliza [versionado semántico](https://semver.org/lang/es/).

## [No publicado]

### Pendiente

- Corrección de la pixelación de las firmas de P02, P06 y P07 en
  `Acta_MemberChecking_MediCita.pdf` (sigue con desenfoque débil, aún legible).
- Repositorio espejo (`MediCita_ISR401-archive`) y archivado en Software
  Heritage; incorporación del SWHID real en `CITATION.cff` (solicitud enviada,
  en trámite).
- Completar el campo de número de cédula (CI) en `C_Enfermería.pdf` y
  `C_Paciente_Simulado.pdf` (firma y nombre ya completos).

### Nota sobre firmas del expediente ético

`A13_Participantes_Externos_MediCita.pdf`, `Adenda_Segunda_Ronda.pdf` y
`Adenda_Validacion_Walkthrough_corregida.pdf` permanecen sin firma del
docente responsable por decisión explícita de este, comunicada al equipo:
sirven como constancia del proceso realizado, ya que los documentos
originales firmados se conservan en el comité de ética. No se trata de un
pendiente.

## [4.0.0] - 2026-09-07 — Entrega 4 (2B) / Defensa Final

### Añadido

- RNF-19 (equidad en el acceso a la cita) y RNF-20 (monitoreo posterior al
  despliegue del componente de IA) en el ERS/SRS, con métrica, umbral y
  responsable definidos.
- Paquete de datos reproducible completo en `07_Datos/` (datos crudos,
  procesados, resultados, diccionario de datos, licencia CC BY 4.0, script
  orquestador `generar_paquete_datos.py`).
- Evidencia de autoría completa en `10_Autoria/`: bitácora de sesiones (19
  días, historial completo del repositorio), capturas de pantalla de los 5
  integrantes, grabaciones de sesión de equipo, notas de campo manuscritas
  de las 8 entrevistas de elicitación, fotos del equipo en la organización
  (con EXIF verificado), doble codificación con cálculo de Cohen's Kappa
  (0,6997, acuerdo sustancial), declaración de uso de IA firmada por los 5
  integrantes, aporte individual con conteo real de commits, `.mailmap`.
- Sesión de member checking (04/09/2026) con 3 participantes previos del
  estudio, documentada en `02_Evidencias/Member_Checking/` (guion, resumen,
  registro estructurado por bloque y acta de conformidad).
- Despliegue reproducible del MVP mediante Docker y Docker Compose
  (`05_MVP/Dockerfile`, `docker-compose.yml`).
- Workflow de GitHub Actions para publicación automática del MVP en GitHub
  Pages (`.github/workflows/pages.yml`).
- Migración de la evidencia audiovisual restringida a un GitHub Release
  (`evidencia-restringida-v1`), para reducir el peso de clonado del
  repositorio.

### Cambiado

- Manuscrito final actualizado: se incorporaron los resultados del acuerdo
  intercodificador y de la sesión de member checking (antes reportados como
  trabajo futuro), y se corrigieron las secciones de "Amenazas a la validez"
  y "Conclusiones y trabajo futuro" en consecuencia.
- Los 8 commits históricos de la identidad genérica `MediCita Team` fueron
  atribuidos a Thais Melanie Herrera Ramos mediante `.mailmap`.
- Catálogo de requisitos no funcionales activos: de 17 a 19.
- Script de generación de checksums renombrado de `GENERA_CHEDKSUMS.sh` a
  `generar_checksums.sh`.
- Corrección de la referencia cruzada de número de oficio institucional
  (DGDS-069-2026) en `CategoriaA_A3_Aval_Establecimiento.pdf`, y actualización
  de los avales institucionales para reflejar a los 5 integrantes del equipo.

### Eliminado

- Carpeta de práctica independiente de Unidad V
  (`PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO/`), ajena a la estructura
  obligatoria del PFC.
- Matriz de trazabilidad duplicada (`matriz_trazabilidad.csv`), quedando
  `matriz_trazabilidad_ACTUALIZADA.csv` como única versión vigente.

## [3.0.0] - 2026-08-02 — Entrega 3 / corte actual

### Añadido

- Interfaces y mockups para los roles de paciente, recepción, enfermería,
  odontología, psicología y nutrición.
- Diagramas de casos de uso en PlantUML y sus exportaciones PNG.
- Diagrama general, diagramas de datos y diagramas complementarios del sistema.
- Archivos raíz para citación, licenciamiento y control de integridad.

### Cambiado

- Ampliación de la cobertura funcional del MVP y de los módulos clínicos.
- Normalización de nombres de mockups y organización del modelado UML.
- Actualización de los metadatos de citación a la versión 3.0.0.

### Corregido

- Relaciones, actores y distribución visual de los casos de uso.
- Correspondencia entre roles, módulos, requisitos e interfaces.

## [2.0.0] - 2026-07-28 — Entrega 2

### Añadido

- Evidencias del entorno del centro médico y registros de recolección.
- Transcripciones anonimizadas de participantes y áreas clínicas.
- Codificación inicial y categorías temáticas de la investigación.
- Diagramas UML, datos de trazabilidad y priorización de requisitos.
- Documentación ética, consentimientos y documentos organizacionales.

### Cambiado

- Reorganización de evidencias por tipo y nivel de acceso.
- Separación del material restringido en `02_Evidencias/00_Restringido/`.

### Corregido

- Nombres y ubicación de archivos de evidencias y modelado.
- Contenido de la codificación temática y de las transcripciones.

## [1.0.0] - 2026-07-21 — Entrega 1A

### Añadido

- Estructura inicial del repositorio.
- Especificación de Requisitos de Software.
- Directorios de evidencias, modelado, trazabilidad, MVP, experimento,
  publicación y ética.
- Archivos README iniciales para documentar el contenido de cada sección.

[No publicado]: https://github.com/ptigasis-Alexander/MediCita_ISR401/compare/v4.0.0...HEAD
[4.0.0]: https://github.com/ptigasis-Alexander/MediCita_ISR401/releases/tag/v4.0.0
[3.0.0]: https://github.com/ptigasis-Alexander/MediCita_ISR401/releases/tag/v3.0.0
[2.0.0]: https://github.com/ptigasis-Alexander/MediCita_ISR401/releases/tag/v2.0.0
[1.0.0]: https://github.com/ptigasis-Alexander/MediCita_ISR401/releases/tag/v1.0.0
