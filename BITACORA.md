# Bitácora del equipo

Proyecto: **Bolsa de Empleos para Graduados UTEQ — Sistema Distribuido (PFC)**
Asignatura: Aplicaciones Distribuidas (ISR-701) — SPA 2026-2027

| Integrante | Rol |
| :--- | :--- |
| Luis Jeremy Jaramillo Acosta | Arquitecto |
| Kenny Isaías España Vera | Líder de Desarrollo |
| Heiner Ariel Zambrano Ronquillo | Responsable de Calidad |
| Luis Alberto Paca Pilataza | Responsable de Documentación |

---

## Sesión 1 — 17/11/2026

- **Hora:** 22:15 – 00:05 (aprox.)
- **Modalidad:** Virtual — Discord / WhatsApp
- **Presentes:** Luis Jeremy Jaramillo Acosta, Kenny Isaías España Vera, Heiner Ariel Zambrano Ronquillo, Luis Paca

### Temas tratados
1. Creación del repositorio público en GitHub y de la estructura base de carpetas (`src/`, `docs/`, `docs/adr/`, `docs/diagramas/`, `evidencias/`, `proto/`).
2. Búsqueda de referencias para trabajos relacionados (sistemas de recomendación de empleo), microservicios/comunicación y decisiones de arquitectura.
3. Elección del estilo de arquitectura del sistema.
4. Elección del mecanismo de comunicación entre servicios.
5. Primer contrato gRPC y primer servicio del esqueleto.
6. Creación del tablero en GitHub Projects y de los primeros issues (#1 a #4).

### Decisiones tomadas
| # | Decisión | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |
| D1 | Usar **microservicios orientados a dominio** (Perfiles, Ofertas y Validación, Postulaciones, Ingesta Externa, Notificaciones) detrás de un API Gateway, en lugar de un monolito o SOA con ESB. | Jeremy (Arquitecto) | `docs/adr/ADR-001-estilo-arquitectura.md` — issue #1 |
| D2 | Usar **gRPC (HTTP/2 + Protocol Buffers)** para la comunicación síncrona interna, **REST/JSON** solo hacia el cliente web y **mensajería AMQP** para notificaciones e ingesta de ofertas externas. | Kenny (Líder de Desarrollo) | `docs/adr/ADR-002-mecanismo-comunicacion.md` — issue #4 |
| D3 | Primer contrato: `PerfilService.VerificarElegibilidad`, que el servicio de postulaciones consultará antes de registrar una postulación. | Luis Paca | `proto/bolsa_uteq.proto` — issue #2 |
| D4 | El esqueleto se implementa en **Python** con `grpcio`; los datos del padrón van en memoria (solo para la demo de E1). | Heiner | `src/servicio_perfiles/servidor_perfiles.py`, `requirements.txt` — issue #3 |
| D5 | Las referencias se guardan en `docs/referencias.bib` (formato biblatex), según la estructura mínima exigida. | Kenny | issue #5 |

### Problemas resueltos
- `referencias.bib` se había creado en la raíz del repositorio; se movió a `docs/` para cumplir la estructura pedida (commit `6bb3142`).
- Los primeros commits se subieron antes de abrir los issues en GitHub; se vincularon manualmente los hashes en cada issue para conservar la trazabilidad.
  
### Pendientes para la próxima sesión
- [ ] Implementar `servicio_postulaciones` como cliente gRPC del servicio de perfiles.
- [ ] Coordinar la entrevista con un responsable real del dominio (UTEQ) y preparar el acta.
- [ ] Elaborar los diagramas C4 (nivel 1 y 2) en draw.io.
- [ ] Completar el README con las instrucciones de ejecución y de compilación.
- [ ] Crear los issues restantes de E1 y E2 en el tablero.

---

## Sesión 2 — 18/11/2026

- **Hora:** 19:15 – 22:30 (aprox.)
- **Modalidad:** Virtual — Discord (sala de estudio 3) / WhatsApp y Excalidraw
- **Presentes:** Luis Jeremy Jaramillo Acosta, Kenny Isaías España Vera, Heiner Ariel Zambrano Ronquillo, Luis Alberto Paca Pilataza

### Temas tratados
1. Sesión colaborativa de bosquejo arquitectónico inicial en Excalidraw (captura a las `19:20` en `evidencias/sesion_diseno_01.jpeg`), debatiendo base de datos única vs. base de datos por servicio, uso de `gRPC` y cifrado `TLS`.
2. Configuración de permisos de escritura en el tablero público de GitHub Projects para todos los colaboradores.
3. Planificación de tareas restantes de E1 y creación de los primeros issues de E2 con etiquetas y responsables (#6, #7, #8 y #10).
4. Inicio del diagrama de contexto C4 Nivel 1 en `draw.io` (issue #8).
5. Creación de la plantilla base compilable del informe técnico en `docs/main.tex` vinculada a `docs/referencias.bib` (issue #10).
6. Revisión del avance del cliente gRPC (`servicio_postulaciones`) y coordinación del levantamiento real de información.

### Decisiones tomadas
| # | Decisión | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |
| D6 | Habilitar permisos de escritura (*Write*) en el tablero público de GitHub Projects para todo el equipo y clasificar los issues con etiquetas (`E1`, `[E2]`). | Jeremy (Arquitecto) | Tablero `TA-PFC-E1 - Bolsa de Empleos UTEQ` — issues #6, #7, #8, #10 |
| D7 | Estandarizar el flujo de trabajo creando siempre el issue antes del `commit` para incluir `(Refs #N)` o `(Closes #N)` en el mensaje y automatizar la trazabilidad. | Todo el equipo | Issue #10 |
| D8 | Estructurar el informe técnico principal en `docs/main.tex` con `biblatex` (estilo IEEE) enlazado a `docs/referencias.bib`, incluyendo portada oficial, roles y cronograma E1–E4. | Luis Paca | `docs/main.tex` — issue #10 |
| D9 | Planificar en el tablero las tareas base de Docker y pruebas de integración para la Entrega 2 (E2) en estado `Todo`. | Jeremy y Heiner | Issues #6 y #7 |

### Problemas resueltos
- Los colaboradores no visualizaban el tablero `TA-PFC-E1 - Bolsa de Empleos UTEQ` en el selector *Projects* al abrir un issue; se habilitaron los permisos en el tablero y se enlazó el proyecto al repositorio, logrando vincular correctamente el issue #10.
- Se verificó el remoto configurado en Git (`git remote -v`) para evitar confusión entre el repositorio de `PE-U1` (`Heiner-ZZZ`) y el repositorio del proyecto `TA-PFC-E1` (`JeremyJaramillo72`).

### Pendientes para la próxima sesión
- [ ] Completar y exportar el diagrama C4 Nivel 1 (issue #8) y elaborar el diagrama C4 Nivel 2 (Contenedores).
- [ ] Implementar `servicio_postulaciones` (cliente gRPC) y obtener las 3 capturas de ejecución con usuario, equipo y fecha/hora visibles.
- [ ] Recolectar y subir la evidencia de levantamiento real (acta firmada de entrevista o resultados de encuesta a >= 15 personas) en `evidencias/`.
- [ ] Realizar la sesión de bosquejo arquitectónico en equipo y subir las 2 fotografías en `evidencias/`.
- [ ] Crear los issues pendientes de E2 en el tablero para Kenny y Luis Paca.

---

## Sesión 3 — 19/11/2026

- **Hora:** 09:30 – 11:30 (aprox.)
- **Modalidad:** Virtual — Discord / WhatsApp
- **Presentes:** Luis Jeremy Jaramillo Acosta, Kenny Isaías España Vera, Heiner Ariel Zambrano Ronquillo, Luis Alberto Paca Pilataza

### Temas tratados
1. Integración en `docs/main.tex` de la vista de contexto C4 Nivel 1 (`docs/figuras/c4-nivel1-contexto.png`), el modelo híbrido de comunicación (ADR-002) y el análisis CAP/PACELC.
2. Síntesis formal de `ADR-001` y `ADR-002` y documentación del contrato `proto/bolsa_uteq.proto` junto con las 3 capturas reales del esqueleto gRPC.
3. Compilación verificada de `docs/main.pdf` con `pdflatex` + `biber` (estilo IEEE).
4. Coordinación de entregables del Día 3 (C4 Nivel 2, manejo de fallos/duplicados gRPC y pruebas automatizadas con medición de latencia).

### Decisiones tomadas
| # | Decisión | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |
| D10 | Consolidar las secciones de arquitectura (C4-N1, comunicación, CAP/PACELC, ADR) y el esqueleto funcional con sus evidencias dentro de `docs/main.tex`, compilando `docs/main.pdf` para validación continua. | Luis Paca | `docs/main.tex`, `docs/main.pdf` — issue #16 |
| D11 | Mantener consistencia fuerte (`CP / PC-EC`) para Perfiles y Postulaciones y consistencia eventual (`AP / PA-EL`) para Catálogo de Ofertas/Scraping y Notificaciones. | Todo el equipo | `docs/main.tex` (Tabla 3) — issue #16 |
| D12 | Avanzar en paralelo el Día 3 con C4 Nivel 2 (Jeremy), manejo de fallos gRPC y control de duplicados (Kenny) y suite de pruebas automatizadas con medición de latencia (Heiner). | Todo el equipo | Tablero `TA-PFC-E1 - Bolsa de Empleos UTEQ` |

### Problemas resueltos
- Al compilar `docs/main.tex` con `pdflatex` + `babel-spanish`, `\,\%` dentro del modo matemático en `RNF-02` generaba errores `Incompatible glue units` y la columna `ISO/IEC 25010` provocaba un desbordamiento en la Tabla 1; se movió `\,\%` fuera del modo matemático y se fijó ancho explícito (`p{3.6cm}`), logrando 0 errores y 9/9 citas IEEE resueltas.

### Pendientes para la próxima sesión
- [ ] Integrar el diagrama C4 Nivel 2 (Contenedores) y los resultados de pruebas unitarias y de latencia en `docs/main.tex`.
- [ ] Completar el levantamiento real de información (encuesta o entrevista UTEQ) y subir la evidencia correspondiente en `evidencias/`.
- [ ] Realizar la sesión de bosquejo colaborativo y cargar las 2 fotografías del bosquejo en `evidencias/`.

---

## Sesión 4 — 19/11/2026

- **Hora:** 19:45 – 20:35
- **Modalidad:** Trabajo técnico en repositorio local y seguimiento en GitHub Projects
- **Presentes:** Heiner Ariel Zambrano Ronquillo

### Temas tratados
1. Auditoría de avance del repositorio `origin/main` frente a los requisitos de `TA-PFC-E1` tras el cierre de los issues `#14`, `#15` (capturas gRPC subidas a las `00:41`, commit `e7b9a68`) y `#16`.
2. Apertura del Issue `#17` en estado `In Progress` para ampliar la validación de resiliencia/carga gRPC e integrar las secciones arquitectónicas pendientes de E1.
3. Implementación de pruebas de carga concurrente (`50` clientes simultáneos frente a `RNF-01`), tolerancia a fallos (`UNAVAILABLE` y `DEADLINE_EXCEEDED`) y entradas borde en `tests/test_integracion_perfiles_grpc.py`.
4. Ejecución y captura verificada de la suite completa (`14/14` pruebas `OK`) en `evidencias/captura_pruebas_unitarias.png`.

### Decisiones tomadas
| # | Decisión | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |
| D13 | Ampliar el módulo existente `tests/test_integracion_perfiles_grpc.py` (sin duplicar archivos de prueba) para validar `RNF-01` bajo 50 clientes concurrentes (`p95 = 227.031 ms <= 300 ms`), tolerancia a fallos (`UNAVAILABLE` en servidor y cliente, `DEADLINE_EXCEEDED` a `100 ms`) y entradas vacías. | Heiner | `tests/test_integracion_perfiles_grpc.py`, `evidencias/captura_pruebas_unitarias.png` — commit `c47aae1`, issue #17 |
| D14 | Unificar por completo los identificadores sintéticos (`0000000001`–`0000000003`) en `src/servicio_perfiles/servidor_perfiles.py` para garantizar consistencia con `cliente_postulaciones.py` y las pruebas automatizadas sin usar numeración similar a cédulas reales. | Heiner | `src/servicio_perfiles/servidor_perfiles.py` — commit `c47aae1`, issue #17 |

### Problemas resueltos
- Al ejecutar `unittest` sobre `origin/main`, `test_consulta_graduado_habilitado` fallaba con `KeyError: '0000000001'` debido a que en `src/servicio_perfiles/servidor_perfiles.py` aún quedaba `"1207458912"`; se corrigió a `"0000000001"` y pasaron los `14/14` casos (`OK` en `2.890 s`).
- Se ajustó el servidor local de pruebas con `max_workers=50` y una llamada previa de calentamiento (*warm-up*) para medir de forma estable la latencia concurrente sin sesgo de inicialización en frío del *thread pool*.

### Pendientes para la próxima sesión
- [ ] Completar la segunda parte del issue `#17`: integrar C4 Nivel 2, *Justificación de la arquitectura distribuida*, *Trabajos relacionados* y métricas reales de pruebas en `docs/main.tex`, además de corregir el formato y añadir la guía de compilación LaTeX en `README.md`.
- [ ] Coordinar con el equipo las evidencias y secciones restantes de E1 (levantamiento real, 2 fotografías con bosquejo de arquitectura, análisis de riesgos con `FORM-AC-01`, declaración de uso de IA, tabla de aportes, compilación final de `docs/main.pdf` y video).

---

## Sesión 5 — 19/11/2026

- **Hora:** 22:20 – 23:45 (captura de evidencia a las `23:38`, 1 h 14 min de sesión activa)
- **Modalidad:** Virtual — Discord (videollamada en sala de estudio 3) y pizarra compartida Excalidraw
- **Presentes:** Luis Jeremy Jaramillo Acosta, Kenny Isaías España Vera, Heiner Ariel Zambrano Ronquillo, Luis Alberto Paca Pilataza

### Temas tratados
1. Sesión colaborativa de refinamiento del bosquejo arquitectónico hacia el Diagrama C4 Nivel 2 (Contenedores) en Excalidraw (`evidencias/sesion_diseno_02.jpeg`, `19/11/2026 23:38`).
2. Delimitación del límite del sistema distribuido (`Bolsa de Empleo UTEQ`), definiendo `App Web (SPA)` → `HTTPS/TLS` → `API Gateway (REST/Enrutamiento/RBAC)`.
3. Definición de los contenedores de microservicios (`Servicio Perfiles`, `Servicios Postulaciones` en `Python/gRPC` y `Servicios Ofertas Scraping`), cada uno con su almacén `PostgreSQL` aislado (`DB Perfiles`, `DB Postulación`, `DB Ofertas`).
4. Integración del `Broker AMQP (RabbitMQ)` conectado hacia `Servicios Notificaciones (Consumidor Asíncrono)` y enlaces con los tres sistemas externos (`Padrón / Identidad UTEQ`, `Servicio de Correo SMTP` y `Portales Externos`).

### Decisiones tomadas
| # | Decisión | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |
| D14b | Aprobar en equipo el bosquejo refinado de contenedores C4 Nivel 2 con bases `PostgreSQL` por dominio, `gRPC/TLS` interno y mensajería asíncrona `RabbitMQ/AMQP`, consolidando las dos fotografías de diseño colaborativo para el repositorio. | Todo el equipo | `evidencias/sesion_diseno_01.jpeg` (`18/11 19:20`), `evidencias/sesion_diseno_02.jpeg` (`19/11 23:38`) — issue #19, commit `0948b75` |

### Problemas resueltos
- Se resolvieron en vivo las dudas planteadas en el bosquejo del `18/11` (base de datos aislada por microservicio en lugar de BD única, separación del `API Gateway`, uso de `gRPC` interno y cifrado `TLS`), alineando el diseño antes de su exportación definitiva en `draw.io`.

### Pendientes para la próxima sesión
- [ ] Subir ambas fotografías de sesiones de diseño a `evidencias/` (issue #19) e integrar el Diagrama C4 Nivel 2 en `docs/main.tex`.

---

## Sesión 6 — 20/11/2026

- **Hora:** 16:00 – 16:20
- **Modalidad:** Trabajo técnico en repositorio local y verificación QA sobre `origin/main`
- **Presentes:** Heiner Ariel Zambrano Ronquillo

### Temas tratados
1. Revisión de los últimos avances del equipo en `origin/main`: robustecimiento gRPC con `INVALID_ARGUMENT`, formato `GRAD-TEST-NNN` e idempotencia `RNF-05` (commit `fcd9b07`, issue `#18`) y carga de fotografías de sesiones de diseño con bosquejo C4 (commit `0948b75`, issue `#19`).
2. Redacción en `docs/main.tex` de *Trabajos relacionados* (4 estudios del `.bib`), *Justificación de la arquitectura distribuida* (monolito vs. microservicios frente a `RNF-01`–`RNF-06`), integración del *Diagrama de Contenedores C4 Nivel 2* (`docs/figuras/c4-nivel2-contenedores.png`) y subsección de resultados medidos de la suite `unittest` (`evidencias/captura_pruebas_unitarias.png`).
3. Auditoría de los 11 DOIs de `docs/referencias.bib` contra Crossref y prueba de compilación limpia de `docs/main.tex` (`pdflatex -> biber -> pdflatex -> pdflatex`) sin generar aún el `docs/main.pdf` definitivo.
4. Corrección del formato en `README.md` e incorporación de la guía de compilación LaTeX para cierre del issue `#17`.

### Decisiones tomadas
| # | Decisión | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |
| D15 | Integrar en `docs/main.tex` la vista de contenedores C4 Nivel 2, la justificación distribuida, los cuatro trabajos relacionados y los resultados reales de `unittest`, manteniendo coherencia directa con `ADR-001/002`, la Tabla de comunicación y `CAP/PACELC`. | Heiner | `docs/main.tex` — issue #17 |
| D16 | Corregir el bloque de código sin cerrar en `README.md` y documentar la secuencia exacta `pdflatex -> biber -> pdflatex -> pdflatex` con dependencias, dejando la generación y subida final de `docs/main.pdf` para cuando el equipo cierre todas las secciones pendientes. | Heiner | `README.md` — issue #17 |

### Problemas resueltos
- En `README.md`, el bloque ` ```text ` de la estructura de carpetas no tenía cierre y rompía la visualización de toda la guía de ejecución del esqueleto; se corrigió el cierre y se añadió la sección de compilación LaTeX.
- Durante la compilación de prueba en carpeta temporal se detectaron desbordamientos horizontales (`Overfull \hbox`) en expresiones `\texttt{...}` largas de C4-N2 y justificación; se ajustó el formato y separación silábica logrando `0` errores y `11/11` citas IEEE verificadas por Crossref.

### Pendientes para la próxima sesión
- [ ] Completar las secciones restantes de `docs/main.tex`: *Resumen ejecutivo*, *Objetivos*, *Análisis de riesgos técnicos* (con `FORM-AC-01`), *Tabla de aportes individuales* y *Declaración de uso de IA*.
- [ ] Incorporar la evidencia de levantamiento real de información (entrevista o encuesta UTEQ) en `evidencias/` y vincularla con los requisitos del informe.
- [ ] Grabar y enlazar en `README.md` el video de presentación (5–7 min), compilar el `docs/main.pdf` definitivo y preparar el PDF de una sola página para el SGA.

---

## Sesión 7 — 20/11/2026

- **Hora:** 20:45 – 23:45 (aprox., ~3 horas de trabajo técnico y documentación)
- **Modalidad:** Trabajo técnico en repositorio local y seguimiento en GitHub Projects
- **Presentes:** Luis Alberto Paca Pilataza

### Temas tratados
1. Sincronización del repositorio local con `origin/main` (commit `fb5933f`), apertura y vinculación del **Issue `#23`** en el tablero público `TA-PFC-E1 - Bolsa de Empleos UTEQ`.
2. Corrección de la portada oficial de `docs/main.tex`: actualización del nombre oficial de la facultad (`Facultad de Ciencias de la Computación`), verificación del código unificado de la asignatura (`ISR-701` coincidente con `README.md` y `BITACORA.md`) y establecimiento de la fecha exacta de entrega (`29 de noviembre de 2026`).
3. Elaboración completa de la **Sección 3 (`Objetivos`)** en `docs/main.tex`: redacción del objetivo general del sistema distribuido y estructuración de cuatro objetivos específicos medibles (`OE-01` a `OE-04`) con sus indicadores cuantitativos de verificación al cierre del periodo en la tabla `tab:objetivos` (`tabularx` + `booktabs`), alineados con los 10 RF, los 6 RNF (ISO/IEC 25010) y el cronograma de entregas E1–E4.
4. Redacción y ajuste de la sección **Declaración de uso de inteligencia artificial** en `docs/main.tex`, detallando el empleo de Google Gemini (versión Gemini 4, noviembre de 2026) como apoyo editorial y de formato (detección de faltas ortográficas, signos de puntuación, claridad de redacción, revisión de sintaxis LaTeX y alineación de tablas y matrices).
5. Validación iterativa de compilación completa en `docs/` mediante `pdflatex -> biber -> pdflatex -> pdflatex`, verificando `0` errores, `11/11` citas IEEE resueltas, ausencia de desbordes horizontales en las secciones redactadas y limpieza de archivos temporales.
6. Auditoría y saneamiento de `BITACORA.md`: eliminación de dobles acentos graves sueltos en la primera y última línea del archivo, revisión de las marcas de tiempo reales en `evidencias/sesion_diseno_01.jpeg` (`18/11/2026 19:20`) y `evidencias/sesion_diseno_02.jpeg` (`19/11/2026 23:38`), ajuste cronológico de las sesiones de diseño y registro detallado de la jornada de documentación para el cierre del Issue `#23`.

### Decisiones tomadas
| # | Decisión | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |
| D17 | Actualizar la portada oficial (`Facultad de Ciencias de la Computación`, `29 de noviembre de 2026`), incorporar la Sección 3 (`Objetivo general` y `OE-01`–`OE-04` con indicadores cuantitativos en `tab:objetivos`) y redactar la `Declaración de uso de inteligencia artificial` en `docs/main.tex`. | Luis Paca | `docs/main.tex` — issue #23 |
| D18 | Sanear el formato Markdown de `BITACORA.md`, alinear las horas de las sesiones de diseño colaborativo con las evidencias fotográficas (`18/11 19:20` y `19/11 23:38`) y consolidar el cierre del Issue `#23` en un commit atómico junto con `docs/main.tex`. | Luis Paca | `BITACORA.md`, `evidencias/sesion_diseno_01.jpeg`, `evidencias/sesion_diseno_02.jpeg` — issue #23 |

### Problemas resueltos
- Se eliminaron los dobles acentos graves sueltos al inicio (línea 1) y al final (línea 193) de `BITACORA.md`, que impedían el renderizado correcto del encabezado H1 y del cierre del documento en GitHub.
- Se corrigió el desfase horario de la Sesión 2 (`18/11`) y se incorporó la sesión nocturna de diseño colaborativo del `19/11` (`22:20 – 23:45`) para guardar correspondencia exacta con las horas visibles en `evidencias/sesion_diseno_01.jpeg` (`19:20`) y `evidencias/sesion_diseno_02.jpeg` (`23:38`).
- Se verificó mediante compilación completa (`pdflatex -> biber -> pdflatex -> pdflatex`) que `docs/main.tex` compila con `0` errores y `11/11` referencias IEEE resueltas tras las adiciones del Issue `#23`.

### Pendientes para la próxima sesión
- [ ] Completar las secciones restantes de `docs/main.tex`: *Resumen ejecutivo*, *Análisis de riesgos técnicos* (con `FORM-AC-01`) y *Tabla de aportes individuales*.
- [ ] Incorporar la evidencia de levantamiento real de información (entrevista o encuesta UTEQ) en `evidencias/` y vincularla con los requisitos del informe.
- [ ] Grabar y enlazar en `README.md` el video de presentación (5–7 min), compilar el `docs/main.pdf` definitivo para entrega y preparar el PDF de una sola página para el SGA.

---

<!-- Plantilla para nuevas sesiones (copiar debajo)

## Sesión N — DD/MM/2026

- **Hora:**
- **Modalidad:**
- **Presentes:**

### Temas tratados
1.

### Decisiones tomadas
| # | Decisión | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |

### Problemas resueltos
-

### Pendientes para la próxima sesión
- [ ]

-->