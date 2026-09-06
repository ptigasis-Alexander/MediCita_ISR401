<div align="center">

# 🧾 10_Autoria — Evidencia de Autoría y Trabajo Propio

### Proyecto MediCita (SICM) — ISR-401

![Progreso](https://img.shields.io/badge/Progreso-11_de_12_completos-green?style=for-the-badge)
![Criterio](https://img.shields.io/badge/Criterio_de_piso-P7-yellow?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-06/09/2026-informational?style=for-the-badge)

</div>

---

## 📌 Sobre este índice

Índice del estado real de cada elemento exigido por la Sección 6 de
la Guía de Desarrollo del 02/09/2026. **Ningún elemento marcado como
pendiente contiene contenido inventado.**

---

## 📋 Estado por elemento

| Cód. | Elemento | Estado | Notas |
|---|---|:---:|---|
| A1 | [`bitacora_sesiones.csv`](bitacora_sesiones.csv) | 🟡 Parcial | 16 filas reales de `git log`. Faltan `hora_inicio`, `hora_fin`, `modalidad`, `decisiones_tomadas`. |
| A2 | [`Capturas/`](Capturas/Capturas.md) | 🟡 En progreso | 12 capturas subidas. sdiazp3 y jgamarraz ya llegan a 3; therrerar, mtrujillov y ptigasis tienen 2, falta 1 cada uno. |
| A3 | Fuentes editables de diagramas | 🟢 Completo | `.drawio` + `.png` para todo el UML; mockups con fuente real en `05_MVP/`. |
| A4 | [`grabaciones/`](grabaciones/grabaciones.md) | 🟢 Completo | 2 de 2 grabaciones mínimas. |
| A5 | [`notas_campo/`](notas_campo/notas_campo.md) | 🟢 Completo | 8 de 8 notas manuscritas escaneadas, una por entrevista de elicitación. |
| A6 | [`Fotos_equipos/`](Fotos_equipos/Fotos_equipos.md) | 🟢 Completo | 3 fotos con EXIF real verificado, 2 integrantes identificables. |
| A7 | [`doble_codificacion/`](doble_codificacion/) | 🟢 Completo | 38 segmentos codificados por 2 integrantes independientes. **Kappa = 0,6997 (acuerdo sustancial)**, IC 95% [0,53–0,87]. |
| A8 | [`correspondencia/README.md`](correspondencia/README.md) | 🟢 Completo | Las 4 comunicaciones confirmadas y firmadas. |
| A9 | [`declaracion_uso_ia.md`](declaracion_uso_ia.md) | 🟢 Completo | Firmado por los 5 integrantes (03-05/09/2026). |
| A10 | `aporte_individual.md` | 🔴 Vacío | Pendiente de subir con contenido real (commits ya verificados; detalle cualitativo puede quedar `PENDIENTE` y completarse después). |
| A11 | [`exif_inventario.csv`](exif_inventario.csv) | 🟢 Completo | Fotos con EXIF real, inferido por contexto, o marcado explícitamente sin dato. |
| A12 | `.mailmap` | 🟢 Completo | Atribuye los 8 commits de `MediCita Team` a Thais Melanie Herrera Ramos. |

**Leyenda:** 🟢 Completo · 🟡 En progreso · 🔴 Pendiente/vacío

---

## 📊 Resultado de la doble codificación (A7)

| Indicador | Valor |
|---|---:|
| Segmentos codificados | 38 |
| Cohen's Kappa | 0,6997 |
| Intervalo de confianza 95% | [0,5255 – 0,8739] |
| Interpretación (Landis & Koch, 1977) | Sustancial |

---

## 📊 Dato de referencia para A10 — commits reales por integrante

Fuente: vista de "Contributors" de GitHub (historial completo del repositorio).

| Integrante | Commits |
|---|---:|
| Paul Alexander Tigasi Sampedro (ptigasis-Alexander) | 287 |
| Jamileth Estefanía Gamarra Zárate (Jami1405) | 260 |
| Mayummy Jailly Trujillo Vega (mtrujillov-sys) | 249 |
| Thais Melanie Herrera Ramos (Melanie-G23) | 248 |
| Steven Santiago Díaz Pontón (sdiazp3) | 241 |
| **Total** | **1.285** |

> **Nota de verificación pendiente:** confirmar con `git shortlog -sne HEAD` (ejecutado en un clon completo, no superficial) si estos números ya reflejan el `.mailmap` aplicado — en la vista de Contributors de GitHub, "Melanie-G23" seguía apareciendo como identidad separada al momento de esta revisión.

---

## ✅ Próximos pasos recomendados

1. **Subir `aporte_individual.md`** con el contenido real de arriba, aunque el detalle cualitativo quede `PENDIENTE` por ahora.
2. Therrerar, mtrujillov y ptigasis: 1 captura más cada uno (A2).
3. Completar `hora_inicio`, `hora_fin`, `modalidad` y `decisiones_tomadas` en A1.
4. Confirmar los commits reales con `git shortlog -sne HEAD` sobre un clon completo.
5. **Al final de todo:** regenerar `checksums.sha256` sobre el estado definitivo.
