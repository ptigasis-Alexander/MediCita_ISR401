# Consentimientos — Ronda de validación walkthrough (V01–V10)

Esta carpeta contiene las copias **públicas y enmascaradas** de los consentimientos informados correspondientes a la tercera ronda de campo del proyecto MediCita (SICM): la validación guiada del prototipo mediante la técnica *walkthrough*, realizada el **28 de agosto de 2026**.

Esta ronda es diferente de las entrevistas de elicitación de requisitos P01–P08. En el *walkthrough*, cada participante navegó el prototipo desde el rol asignado y comunicó dificultades, funciones no comprendidas y recomendaciones de mejora.

Las transcripciones anonimizadas se encuentran en:

`02_Evidencias/Validacion_Walkthrough/`

## Correspondencia entre consentimientos y sesiones

| Consentimiento público enmascarado | Sesión | Rol o área validada | Transcripción relacionada |
|---|---|---|---|
| `consentimiento_Enfermeria_pixelado.png` | V01 | Enfermería | `01_V_Enfermeria.txt` |
| `consentimiento_Medico_General_pixelado.png` | V02 | Medicina General | `02_V_Medicina_General.txt` |
| `consentimiento_Nutricion_pixelado.png` | V03 | Nutrición | `03_V_Nutricion.txt` |
| `consentimiento_Odontologia_Coordinacion_pixelado.png` | V04 y V05 | Coordinación y Odontología/Coordinación | `04_V_Coordinacion.txt` y `05_V_Odontologia_Coordinacion.txt` |
| `consentimiento_Recepcion_pixelado.png` | V06 | Recepción y Recaudación | `06_V_Recepcion.txt` |
| `consentimiento_Simulacion_Paciente__pixelado.png` | V07 | Paciente simulado; corresponde a la misma persona identificada como P08 en la elicitación | `07_V_Simulador_(Paciente).txt` |
| `consentimiento_Fisioterapeuta_pixelado.png` | V08 | Terapia Física | `08_V_TerapiaFisica.txt` |
| `consentimiento_Psicologia_pixelado.png` | V09 | Psicología | `09_V_Psicologia.txt` |
| `consentimiento_SimulacionPaciente02_pixelado.png` | V10 | Segunda persona interpretando el rol de paciente | `10_V_Simulador_Paciente02.txt` |

**Total de esta ronda: 9 consentimientos públicos enmascarados que respaldan 10 sesiones de validación.**

El consentimiento de Odontología/Coordinación corresponde a la persona que intervino en las sesiones V04 y V05. Por ello existen 10 transcripciones y 9 archivos de consentimiento, sin que esto represente una evidencia faltante.

## Relación con las rondas anteriores

Los consentimientos P01–P08 ubicados en `02_Evidencias/Consentimientos/` pertenecen a las entrevistas de levantamiento o elicitación de requisitos.

Estos consentimientos no deben confundirse con los consentimientos de la ronda de validación V01–V10 almacenados en esta carpeta.

Sin embargo, la persona que participó como P08, paciente simulado durante la elicitación, es la misma que intervino en la sesión V07 del *walkthrough*. Esta persona participó en dos etapas, pero debe contabilizarse una sola vez al calcular el número de participantes diferentes.

## Consolidado del trabajo de campo

| Etapa | Registros de consentimiento asociados | Sesiones |
|---|---:|---:|
| Elicitación de requisitos (P01–P08) | 8 | 8 |
| Validación walkthrough (V01–V10) | 9 | 10 |
| **Total de registros y sesiones** | **17** | **18** |

## Conteo de participantes diferentes

El total no se obtiene sumando directamente 8 + 9, porque P08 y V07 corresponden a la misma persona.

```text
8 personas de elicitación
+ 9 personas de validación
- 1 persona repetida entre P08 y V07
= 16 personas diferentes
```

**Total acumulado: 16 participantes diferentes, 17 registros de consentimiento asociados a las dos etapas y 18 sesiones documentadas.**

## Fundamento ético

La ronda fue registrada previamente mediante:

`08_Etica/Adenda_Validacion_Walkthrough_corregida.pdf`

Este archivo corresponde al documento A.13.3 del expediente ético. La adenda tiene fecha del **27 de agosto de 2026**, anterior a las sesiones realizadas el **28 de agosto de 2026**.

MediCita está clasificado como proyecto de **Categoría A**, debido a que su dominio involucra información clínica y datos sensibles de salud.

Por esta razón:

- Las dos validaciones del rol de paciente fueron realizadas por personas que interpretaron un papel mediante simulación y datos controlados.
- No participaron pacientes reales en las sesiones V07 y V10.
- No se publican historias clínicas reales, diagnósticos reales ni imágenes clínicas identificables.
- Los consentimientos autorizan el uso de datos anonimizados en el proyecto académico y en publicaciones científicas.
- La firma, la cédula, el nombre, el rostro y la voz permanecen protegidos.
- Ningún dato personal identificable se publica en la zona abierta del repositorio.

## Zonas de evidencia

Conforme al plan de gestión de datos y al expediente ético del proyecto, la evidencia está separada en dos zonas.

### Zona pública [P]

Esta carpeta contiene únicamente copias enmascaradas de los consentimientos.

Antes de publicar los archivos se cubrieron:

- nombres y apellidos;
- números de cédula;
- firmas;
- teléfonos;
- correos electrónicos;
- cualquier otro identificador personal directo.

### Zona restringida [R]

Los consentimientos originales completos se conservan dentro del archivo cifrado multipartes ubicado en:

`02_Evidencias/00_Restringido/Consentimientos_Validacion.7z.*`

El contenedor está protegido mediante cifrado AES-256. La contraseña se entrega exclusivamente al docente responsable mediante el SGA y nunca se almacena dentro del repositorio GitHub.

Ningún archivo de esta carpeta autoriza ni contiene la publicación de datos personales identificables.
