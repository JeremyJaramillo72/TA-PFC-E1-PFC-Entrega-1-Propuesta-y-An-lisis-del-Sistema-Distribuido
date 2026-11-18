# Bitácora del equipo

Proyecto: **Bolsa de Empleos para Graduados UTEQ — Sistema Distribuido (PFC)**
Asignatura: Aplicaciones Distribuidas (ISR-701) — SPA 2026-2027

| Integrante | Rol |
| :--- | :--- |
| Luis Jeremy Jaramillo Acosta | Arquitecto |
| Kenny Isaías España Vera | Líder de Desarrollo |
| Heiner Ariel Zambrano Ronquillo | Responsable de Calidad |
| Luis Paca | Responsable de Documentación |

---

## Sesión 1 — 17/11/2026

- **Hora:** 22:15 – 00:05 (aprox.)
- **Modalidad:** _(completar: presencial / virtual — plataforma)_
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
- _(completar: otros problemas que surgieron en la sesión, p. ej. al generar el código desde el `.proto` o al levantar el servidor)_

### Pendientes para la próxima sesión
- [ ] Implementar `servicio_postulaciones` como cliente gRPC del servicio de perfiles.
- [ ] Coordinar la entrevista con un responsable real del dominio (UTEQ) y preparar el acta.
- [ ] Elaborar los diagramas C4 (nivel 1 y 2) en draw.io.
- [ ] Completar el README con las instrucciones de ejecución y de compilación.
- [ ] Crear los issues restantes de E1 y E2 en el tablero.

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
