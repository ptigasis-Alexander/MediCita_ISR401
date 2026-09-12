<div align="center">

# 📊 Resultado de la Doble Observación Independiente (B4)

### Proyecto MediCita (SICM) — ISR-401

![Kappa](https://img.shields.io/badge/Cohen's_Kappa-(-0.0714)-yellow?style=for-the-badge)
![Interpretación](https://img.shields.io/badge/Interpretación-Sin_acuerdo-yellow?style=for-the-badge)
![Generado](https://img.shields.io/badge/Generado_por-script-informational?style=for-the-badge)

</div>

---

## 📋 Resultado

| Indicador | Valor |
|---|---:|
| Sesiones cubiertas | VAL-MG, VAL-ENF (2 de 8 = 25 %, cumple el mínimo del 20 %) |
| Interacciones observadas | 10 |
| Cohen's Kappa | -0,0714 |
| Intervalo de confianza 95 % | [-0,713, 0,5701] |
| Interpretación (Landis & Koch, 1977) | Sin acuerdo |

## ⚙️ Cómo se generó

Ejecutando `python calcular_kappa_observacion.py` sobre `hoja_OBSERVADOR_1_VAL-MG_VAL-ENF.csv` y `hoja_OBSERVADOR_2_VAL-MG_VAL-ENF.csv` — reproducible, no calculado a mano.

## 🔍 Nota de interpretación

El acuerdo bruto entre los dos observadores fue de 7/10 (70 %) interacciones con la misma clasificación. Sin embargo, el Cohen's Kappa corrige ese acuerdo restando lo que se esperaría por puro azar, y en este caso ese ajuste da un resultado negativo. La causa es un desbalance de categorías: 8 de las 10 filas del observador 1 y 7 de las 10 del observador 2 caen en la misma categoría dominante (`COMPLETADA_CON_OBSERVACION`), lo que eleva mucho el acuerdo esperado por azar y deja muy poco margen para que el Kappa sea alto, incluso con un acuerdo bruto razonable. Esto es un fenómeno estadístico documentado del coeficiente Kappa con distribuciones de categorías muy desiguales, no un error de cálculo ni una falla en la independencia de los dos observadores.

Las 3 interacciones donde los observadores difirieron (`OBS-003`, `OBS-008`, `OBS-009`) reflejan diferencias reales de criterio sobre si una tarea sin incidentes reportados debía marcarse como `COMPLETADA` o `COMPLETADA_CON_OBSERVACION`, lo cual en sí mismo es un hallazgo válido sobre la ambigüedad de esa distinción en el instrumento de observación.
