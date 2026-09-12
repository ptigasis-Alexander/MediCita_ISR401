# 06_Experimento/scripts_analisis/

Cadena de análisis cuantitativo de MediCita, dividida en tres etapas independientes más un orquestador, tal como exige la guía de cierre del PFC.

## Etapas

| Archivo | Responsabilidad |
|---|---|
| `leer_datos.py` | Abre los CSV de `07_Datos/datos_procesados/` y `07_Datos/resultados/`, comprueba que tengan las columnas obligatorias y que no estén vacíos. No transforma ni calcula nada. |
| `procesar_datos.py` | Clasifica las observaciones por grupo de área, calcula la prueba de chi-cuadrado con permutación Monte Carlo (100.000 réplicas, semilla 42), el intervalo de confianza bootstrap de V de Cramér, la cobertura de RF Must y el cálculo de potencia estadística de referencia. No escribe ningún archivo. |
| `generar_resultados.py` | Toma los valores ya calculados y escribe `resultados_estadisticos.json`, los CSV de resumen (`resumen_descriptivo.csv` ×2, `resumen_validacion.csv`, `power_calculation.csv`) y las dos figuras PNG (`estado_tareas_validacion.png`, `cobertura_rf_must.png`). No calcula nada nuevo. |
| `run_all.py` | Orquestador único. Importa las tres etapas anteriores y las ejecuta en orden. No contiene ninguna lógica propia de lectura, cálculo o escritura. |
| `verificar_rf_must.js` | Suite de verificación técnica independiente de los RF Must (no forma parte de esta cadena de tres etapas; es un script aparte). |

## Cómo correr

Desde esta carpeta, con las dependencias del proyecto instaladas (`scipy`, `matplotlib`):

```bash
python run_all.py
```

Esto reproduce exactamente `resultados_estadisticos.json`, los CSV y las figuras que respaldan el manuscrito y los resultados presentados en la defensa — verificado byte por byte contra la versión anterior de un solo archivo.

Cada etapa también puede correrse por separado para depurar un paso puntual sin rehacer todo el pipeline:

```bash
python leer_datos.py        # solo lee y valida
python procesar_datos.py    # lee, valida y calcula (usa leer_datos.py)
python generar_resultados.py  # ejecuta las tres etapas completas
```
