# Dataset de replicación — MediCita

## Contenido
- `observaciones_validacion_procesadas.csv`: 46 observaciones derivadas de la evidencia de validación disponible.
- `observacion_requisito_long.csv`: 72 relaciones normalizadas entre observaciones y requisitos.
- `resumen_descriptivo.csv`: conteos regenerables de estados, áreas y requisitos.
- `cobertura_RF_Must_final.csv`: matriz de cierre técnico de los 22 RF Must.
- `verificacion_tecnica_RF_Must.json`: salida de la verificación técnica reproducible del MVP.
- `resultados_estadisticos.json`: prueba de permutación Monte Carlo (chi-cuadrado 1,9921, V de Cramér 0,1663, p=0,4131) y cálculo de potencia, ambos regenerables con `06_Experimento/scripts_analisis/run_all.py`.
- `run_all_output.json`: salida íntegra de la última ejecución del script anterior, para verificación de reproducibilidad.

## Alcance temporal del corte
Primera ronda: 8 entrevistas de levantamiento realizadas.
Segunda ronda: 10 sesiones de validación con transcripción disponible (incluye Psicología y el paciente simulado 02). Ninguna sesión queda pendiente en este corte.

## Resultado técnico reproducible
Cobertura de RF Must: 20/22 = 90,91 %. Este porcentaje es cobertura técnica del MVP y no representa satisfacción, SUS ni aprobación de participantes.

De las 46 observaciones: 39 completadas con observación de mejora, 5 no completadas, 2 completadas sin observaciones.

## Reutilización
El conjunto está preparado para licencia CC BY 4.0 una vez se realice el depósito abierto correspondiente. No se inventa ni se anticipa un DOI de Zenodo.

## Exclusiones
No contiene audio, video, consentimientos firmados, identificadores directos ni la clave de reidentificación.
