# Justificación del cálculo de tamaño muestral

**Archivo que documenta:** `power_calculation.csv`

## Aclaración sobre su relación con el prerregistro OSF

Este cálculo de potencia estadística (Cohen's d, alfa, potencia, n por
grupo) **no forma parte del contenido prerregistrado en OSF**
(DOI 10.17605/OSF.IO/DTYNC, 27/08/2026). La evidencia conservada de ese
prerregistro (`06_Experimento/osf_registration.pdf`) documenta un tamaño
de muestra planificado de **ocho participantes** — las mismas personas de
la primera ronda de levantamiento — como decisión práctica y cualitativa
del diseño del walkthrough, **no** un cálculo formal de potencia
estadística. Ninguna captura del prerregistro menciona Cohen's d, nivel
de significancia, potencia estadística, ni un tamaño de 64 o 128.

Este cálculo se realizó y documentó por separado, como referencia
metodológica estándar, con fecha real de incorporación al repositorio
entre el 01/09/2026 y el 03/09/2026. Se documenta aquí con esa fecha real,
sin atribuirlo al prerregistro de OSF.

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
no una meta que el proyecto haya alcanzado, y no reemplaza ni reinterpreta
el tamaño de muestra de 8 participantes que sí fue prerregistrado en OSF
por razones prácticas y cualitativas del diseño del walkthrough.

## Relación honesta con la muestra real obtenida

La muestra real del componente empírico (ronda de elicitación +
validación walkthrough) es sustancialmente menor a los 128 participantes
que este cálculo de referencia indicaría como necesarios para una
comparación de dos grupos con potencia convencional. Esto es consistente
con lo que ya declara el análisis estadístico del proyecto
(`06_Experimento/resultados/resultados_estadisticos.json`): el resultado
de la prueba de permutación no fue estadísticamente significativo
(p = 0,413086), un resultado que se reporta tal cual, sin buscar
significancia mediante manipulación de la muestra o del análisis.

Este cálculo de potencia no convierte la muestra disponible en una
muestra suficiente para detectar el efecto hipotetizado, y su fecha real
de documentación (01–03/09/2026) es posterior a la ejecución de las
sesiones de validación. Se declara así explícitamente, sin presentarlo
como parte del prerregistro OSF, para no sobrestatuar su valor
metodológico frente a lo que exige la Sección 5.1 de la Guía de
Desarrollo.
