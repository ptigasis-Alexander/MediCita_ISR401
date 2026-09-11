<div align="center">

# 📝 Consentimientos — Ronda de Elicitación (P01–P08)

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-yellow?style=for-the-badge)
![Firmas](https://img.shields.io/badge/Firmas-8_de_8-success?style=for-the-badge)
![CI](https://img.shields.io/badge/Campo_CI-2_sin_completar_por_el_firmante-orange?style=for-the-badge)

</div>

---

## 📌 Sobre esta carpeta

Copias **públicas y enmascaradas** de los consentimientos informados firmados por las 8 personas que participaron en la ronda de elicitación de requisitos, correspondientes a las transcripciones de `02_Evidencias/Transcripcion/`.

En cada archivo se tapó el nombre, la firma, el nombre y apellido, y el número de cédula. Los originales sin tapar se conservan únicamente en la zona restringida cifrada del repositorio (`02_Evidencias/00_Restringido/`), nunca en esta carpeta.

## 📋 Correspondencia con las transcripciones de elicitación

| Consentimiento | Código de transcripción | Área |
|---|---|---|
| `C_Enfermería.pdf` | P06 | Enfermería |
| `C_Fisioterapeuta.pdf` | P03 | Terapia Física |
| `C_MedicinaGeneral.pdf` | P02 | Medicina General |
| `C_Nutricion.pdf` | P04 | Nutrición |
| `C_Odontologia.pdf` | P05 | Odontología |
| `C_Paciente_Simulado.pdf` | P08 | Paciente / usuario |
| `C_Psicologia.pdf` | P01 | Psicología |
| `C_Recepcionista.pdf` | P07 | Recepción y Recaudación |

**Total: 8 consentimientos, uno por persona entrevistada (P01–P08).**

## ⚠️ Nota de honestidad: campo de cédula (CI) sin completar en 2 documentos

En `C_Enfermería.pdf` y `C_Paciente_Simulado.pdf`, la **firma y el nombre completo sí están presentes**, pero la persona firmante dejó en blanco el campo del número de cédula (CI) al momento de firmar. No se completó ese dato de forma retroactiva ni por el equipo, para no comprometer la integridad del documento original tal como fue firmado.

La identidad de ambas personas queda de todos modos verificable mediante:
- La firma manuscrita (conservada sin enmascarar en la zona restringida `02_Evidencias/00_Restringido/`).
- El nombre y apellido completos.
- El código de sesión que vincula cada consentimiento con su transcripción correspondiente (P06 y P08 respectivamente).

Se prefirió documentar esta omisión con transparencia antes que ocultarla o completarla sin respaldo real.


## 🔗 Relación con la ronda de validación

Los consentimientos de la ronda de validación del prototipo (walkthrough, agosto 2026) — un grupo de participantes externos distinto, sin superposición con estos 8 — van en `02_Evidencias/Validacion_Walkthrough/Consentimientos_validacion/consentimientos_validacion.md`. No deben confundirse ni sumarse ambas rondas como si fueran las mismas personas — ver `02_Evidencias/Readme.md` para el conteo total confirmado de 16 participantes externos distintos.

## 🔒 Zonas de evidencia

Conforme al protocolo ético del proyecto (Categoría A):
- **Zona pública [P]:** esta carpeta — copias enmascaradas, sin nombre, firma ni cédula visibles.
- **Zona restringida [R]:** originales firmados completos, en `02_Evidencias/00_Restringido/`, cifrados con AES-256, contraseña entregada únicamente al docente.
