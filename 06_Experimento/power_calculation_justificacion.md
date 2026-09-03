# Justificación del cálculo de tamaño muestral

**Archivo que documenta:** `power_calculation.csv`
**Calculado antes de analizar los resultados** (no ex-post), como parte
del protocolo registrado en OSF (DOI 10.17605/OSF.IO/DTYNC).

## Parámetros usados y por qué

| Parámetro | Valor | Justificación |
|---|---|---|
| Tamaño de efecto (Cohen's d) | 0,5 | Efecto mediano según las convenciones de Cohen (1988). Se eligió un efecto mediano, no pequeño ni grande, por ausencia de estudios previos específicos sobre percepción de requisitos en sistemas clínicos similares en el contexto ecuatoriano que permitieran estimar un tamaño de efecto esperado con mayor precisión. |
| Nivel de significancia (alfa) | 0,05 | Estándar convencional en ciencias sociales y de la computación aplicada. |
| Potencia estadística | 0,80 | Estándar convencional (80% de probabilidad de detectar un efecto real si existe). |
| n por grupo | 64 | Resultado del cálculo de potencia para una prueba de dos proporciones/medias independientes con los parámetros anteriores. |
| n total | 128 | 64 × 2 grupos. |

## Qué significa este cálculo para el proyecto

Este cálculo establece cuántos participantes **serían necesarios** para
detectar, con confianza estadística convencional, un efecto mediano en
una comparación entre dos grupos. Es un cálculo de referencia estándar,
no una meta que el proyecto haya alcanzado.

## Relación honesta con la muestra real obtenida

La muestra real del componente empírico (ronda de elicitación +
validación walkthrough) es sustancialmente menor a los 128 participantes
que este cálculo indicaría como necesarios para una comparación de dos
grupos con potencia convencional. Esto es consistente con lo que ya
declara el análisis estadístico del proyecto
(`06_Experimento/resultados/resultados_estadisticos.json`): el resultado
de la prueba de permutación no fue estadísticamente significativo
(p = 0,413086), un resultado que se reporta tal cual, sin buscar
significancia mediante manipulación de la muestra o del análisis.

Este cálculo de potencia no convierte la muestra disponible en una
muestra suficiente para detectar el efecto hipotetizado; se declara así
explícitamente para cumplir con el principio de justificar el tamaño
muestral por escrito antes de analizar, no después de ver los resultados
(Sección 5.1 de la Guía de Desarrollo).
