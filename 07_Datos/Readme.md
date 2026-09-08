
# 07_Datos — Paquete de datos del componente empírico MediCita/SICM

## Nota sobre la numeración de carpetas

`07_Datos/` coexiste con `07_Publicacion/`. El prefijo "07" de esta
carpeta corresponde a la numeración exigida por la Sección 7 de la Guía
de Desarrollo del 02/09/2026, independiente de la numeración secuencial
01–09 de las entregas del PFC. No hay conflicto de nombres ni de
contenido entre ambas.

## Qué contiene

- `datos_crudos/`: exactamente como salieron del instrumento, sin
  ninguna edición manual. Incluye la ficha de observación (formato
  vacío/plantilla usado en campo) y el manifiesto de transcripciones de
  validación con su hash SHA-256 por archivo.
- `datos_procesados/`: obtenido únicamente mediante los scripts
  versionados (ver "Cómo se generó" abajo). Nunca editado a mano.
- `resultados/`: tablas y cifras finales generadas por script,
  incluyendo la cobertura de RF Must, los resultados estadísticos
  (chi-cuadrado, prueba de permutación, V de Cramer) y el cálculo de
  potencia con su justificación en prosa.
- `diccionario_datos.csv`: descripción columna por columna de cada
  archivo de este paquete.
- `checksums_datos.sha256`: hash SHA-256 de cada archivo de este
  paquete, para verificar integridad tras la descarga.

## Cómo se generó

Todos los datos de `datos_procesados/` y `resultados/` provienen del
pipeline real del proyecto, en
`06_Experimento/scripts_analisis/run_all.py` (y
`verificar_rf_must.js` para la verificación técnica de RF Must). Este
paquete **no reimplementa** ese análisis: lo ejecuta y sincroniza sus
salidas hacia esta carpeta, para que exista una única fuente de verdad.

## Cómo se reproduce

Desde la raíz del repositorio, con Python 3 y las dependencias del
proyecto instaladas (`matplotlib`, `scipy`):

```bash
python 07_Datos/scripts/generar_paquete_datos.py
```

Esto ejecuta el pipeline real y sincroniza sus salidas hacia
`07_Datos/datos_procesados/` y `07_Datos/resultados/`. Los archivos de
`datos_crudos/` no se regeneran (son el punto de partida, no una
salida del análisis).

## Licencia de los datos

Ver `LICENSE-DATA.txt` — distinta de la licencia del código del
repositorio.

## Desviaciones respecto del protocolo

Ver `desviaciones.md`.

## Identificador persistente del depósito

Ver `registro_deposito.md`.
