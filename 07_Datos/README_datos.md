<div align="center">

# 📦 07_Datos — Paquete de Datos del Componente Empírico

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![Reproducible](https://img.shields.io/badge/Reproducible-Sí-success?style=for-the-badge)
![Licencia](https://img.shields.io/badge/Licencia-CC_BY_4.0-informational?style=for-the-badge)

</div>

---

## 📌 Nota sobre la numeración de carpetas

`07_Datos/` coexiste con `07_Publicacion/`. El prefijo "07" de esta carpeta corresponde a la numeración exigida por la Sección 7 de la Guía de Desarrollo del 02/09/2026, independiente de la numeración secuencial 01–09 de las entregas del PFC. No hay conflicto de nombres ni de contenido entre ambas.

---

## 🔓 Capa pública vs. capa restringida

Este paquete es **capa pública anonimizada**: todo archivo de `datos_crudos/`, `datos_procesados/` y `resultados/` usa exclusivamente códigos de participante (P01–P08, PS-XX, MG-XX) y códigos de sesión (VAL-MG, ELIC-P01, etc.), nunca nombres reales, cédulas, ni datos de contacto. Ningún archivo de esta carpeta permite reidentificar a un paciente o miembro del personal por sí solo.

La **capa restringida** —grabaciones originales, consentimientos sin pixelar, y cualquier archivo que sí pueda vincularse a una identidad real— vive exclusivamente en `02_Evidencias/00_Restringido/` (cifrada en volúmenes `.7z`, publicada como GitHub Release aparte) y en `08_Etica/`. Nada de esa capa se mezcla con este paquete de datos abierto.

---

## 📋 Qué contiene

| Carpeta/archivo | Descripción |
|---|---|
| `datos_crudos/` | Exactamente como salieron del instrumento, sin ninguna edición manual. Incluye la ficha de observación y el manifiesto de transcripciones de validación con su hash SHA-256 por archivo. |
| `datos_procesados/` | Obtenido únicamente mediante los scripts versionados. Nunca editado a mano. |
| `resultados/` | Tablas y cifras finales generadas por script: cobertura de RF Must, resultados estadísticos (chi-cuadrado, prueba de permutación, V de Cramér) y cálculo de potencia con su justificación. |
| `scripts/` | Script orquestador único que reproduce todo el paquete. |
| `diccionario_datos.csv` | Descripción columna por columna de cada archivo de este paquete. |
| `checksums_datos.sha256` | Hash SHA-256 de cada archivo, para verificar integridad tras la descarga. |

---

## ⚙️ Cómo se generó

Todos los datos de `datos_procesados/` y `resultados/` provienen del pipeline real del proyecto, en `06_Experimento/scripts_analisis/run_all.py` (y `verificar_rf_must.js` para la verificación técnica de RF Must). Este paquete **no reimplementa** ese análisis: lo ejecuta y sincroniza sus salidas hacia esta carpeta, para que exista una única fuente de verdad.

## 🔁 Cómo se reproduce

Desde la raíz del repositorio, con Python 3 y las dependencias del proyecto instaladas (`matplotlib`, `scipy`):

```bash
python 07_Datos/scripts/generar_paquete_datos.py
```

Esto ejecuta el pipeline real y sincroniza sus salidas hacia `07_Datos/datos_procesados/` y `07_Datos/resultados/`. Los archivos de `datos_crudos/` no se regeneran (son el punto de partida, no una salida del análisis).

## 📄 Licencia de los datos

Ver `LICENSE-DATA.txt` — distinta de la licencia del código del repositorio.

## 📝 Desviaciones respecto del protocolo

Ver `desviaciones.md`.

## 🔗 Identificador persistente del depósito

Ver `registro_deposito.md`.
