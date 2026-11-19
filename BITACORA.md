``# Bitácora del equipo

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

- **Hora:** 20:00 – 22:30 (aprox.)
- **Modalidad:** Virtual — Discord / WhatsApp
- **Presentes:** Luis Jeremy Jaramillo Acosta, Kenny Isaías España Vera, Heiner Ariel Zambrano Ronquillo, Luis Alberto Paca Pilataza

### Temas tratados
1. Configuración de permisos de escritura en el tablero público de GitHub Projects para todos los colaboradores.
2. Planificación de tareas restantes de E1 y creación de los primeros issues de E2 con etiquetas y responsables (#6, #7, #8 y #10).
3. Inicio del diagrama de contexto C4 Nivel 1 en `draw.io` (issue #8).
4. Creación de la plantilla base compilable del informe técnico en `docs/main.tex` vinculada a `docs/referencias.bib` (issue #10).
5. Revisión del avance del cliente gRPC (`servicio_postulaciones`) y coordinación del levantamiento real de información.

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
``