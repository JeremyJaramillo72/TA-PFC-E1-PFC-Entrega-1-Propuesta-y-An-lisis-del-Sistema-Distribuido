# Sesión de Verificación de Requisitos (Product Owner) — Levantamiento real (TA-PFC-E1)

- **Fecha:** 30/08/2025 *(sesión de revisión y validación de requisitos funcionales y no funcionales del dominio Bolsa de Empleos UTEQ)*
- **Modalidad / Lugar:** Presencial — Universidad Técnica Estatal de Quevedo (UTEQ)
- **Revisor / Product Owner:** Ing. Washington Casanova — Docente de la Carrera de Ingeniería en Software (UTEQ) *(sin datos sensibles)*
- **Participantes del equipo:** Integrantes del equipo de Ingeniería en Software UTEQ
- **Audios originales en Google Drive (alojados externamente por privacidad y control de acceso):**
  - `Requisitos_01.opus` (duración `11:06`, peso `1,3 MB`): https://drive.google.com/file/d/17MKYZayc_iERsr9lUNRc5uDa7jDjezb2/view?usp=sharing
  - `Requisitos_02.opus` (duración `04:20`, peso `479 KB`): https://drive.google.com/file/d/1wpTEugagQTxoI7Ha1EZukZhhtNbJNWuz/view?usp=sharing
- **Confirmación verbal de grabación:** En `Requisitos_02.opus`, marcas `[01:28–01:36]`:
  > *Ing. Washington Casanova:* «¿Ya está grabando, sí?»
  > *Estudiante:* «Sí, estoy grabando.»
  > *Ing. Washington Casanova:* «Arriba no lo veía, pero acá ya lo veo.»
- **Enlaces públicos adicionales verificados en incógnito (Google Drive):**
  - Carpeta completa de validación PO: https://drive.google.com/drive/folders/1f9duhgVlw0f6uexOz3nxi4n83_o8gerG?usp=sharing
  - Transcripción PDF original 1 (`Requisitos 01.pdf`): https://drive.google.com/file/d/1MuHEVVtZEQK20lqwajgcxrzjQJ4ppfe_/view?usp=sharing
  - Transcripción PDF original 2 (`Requisitos 02.pdf`): https://drive.google.com/file/d/1ZvSws1L7_H0uPaqh4vVpW7nJLaXYhy-C/view?usp=sharing

---

## Resumen de hallazgos y ajustes validados con el Product Owner

1. **Separación estricta de requisitos de seguridad (`RNF-04`):** en `Requisitos_01.opus` (`[02:13–03:32]`), el revisor solicita separar explícitamente **autenticación** (acceso con correo y contraseña), **cifrado** y **autorización** (control de acceso a las opciones permitidas por rol — RBAC).
2. **Terminología institucional correcta:** en `[04:10–04:19]`, establece emplear **graduado** en lugar de *egresado*.
3. **Flujo completo de empresas y gestión de ofertas (`RF-07`, `RF-08`):** en `Requisitos_01.opus` (`[06:50–08:35]`) y `Requisitos_02.opus` (`[00:00–00:50]`), exige que la empresa cuente explícitamente con requisitos para **publicar ofertas**, **dar de baja/cancelar o marcar como contratada** una oferta, y **visualizar, contactar y seleccionar postulantes**.
4. **Control de usuarios y caducidad del correo institucional (`RF-01`, `RF-02`, `RF-09`):** en `Requisitos_02.opus` (`[00:50–02:35]`), señala que el administrador debe poder admitir y dar de baja cuentas no autorizadas y advierte que **los correos estudiantiles UTEQ suelen darse de baja aproximadamente a los 5 años**, lo que refuerza validar la elegibilidad contra el padrón institucional.
5. **Automatización del *web scraping* y de las notificaciones (`RF-10`, `RNF-02`):** en `Requisitos_01.opus` (`[05:13–05:38]`) y `Requisitos_02.opus` (`[03:11–04:15]`), corrige la redacción del extractor externo (el sistema *importa/trae* ofertas externas) y define que **las notificaciones por correo ante nuevas ofertas compatibles deben ejecutarse automáticamente por el sistema** y no manualmente por el administrador.

---

## Transcripción fiel con marcas de tiempo (auditada contra los audios originales)

### Parte 1 — `Requisitos_01.opus` (`11:06`)

- **[02:13–03:32] Seguridad — Autenticación, cifrado y autorización (`RNF-04`):**
  - **Ing. Washington Casanova:** En la tabla de autenticación y autorización dice: *"El sistema permite que los usuarios se autentiquen mediante correo electrónico y contraseña"* y luego repite *"además debe contar con autenticación para mayor seguridad"*; es redundante. Lo que falta es dividirlo bien: **autenticación** es un requisito (para entrar al sistema), **cifrado** es otro, y **autorización** es otro, donde los usuarios solo acceden a las opciones para las cuales les está permitido según su rol.
- **[04:10–04:19] Terminología institucional:**
  - **Ing. Washington Casanova:** Usan la palabra *egresado* como sinónimo de *graduado*; no es correcto, el término correcto es **graduado**.
- **[04:33–04:55] Acceso del administrador (`RF-09`):**
  - **Ing. Washington Casanova:** En las historias de usuario de administrador solo tienen crear, editar y validar ofertas internas; también debe contemplarse el inicio de sesión y gestión completa del administrador.
- **[05:13–05:38] Redacción de importación por *web scraping* (`RF-10`):**
  - **Ing. Washington Casanova:** En la historia de usuario de *web scraping*, no es que el sistema externo exporte; en realidad **nuestro sistema importa/trae** esas ofertas externas hacia el aplicativo.
- **[06:15–07:20] Publicación de ofertas por parte de la empresa (`RF-07`):**
  - **Ing. Washington Casanova:** En la postulación a ofertas internas está el graduado, pero ¿dónde está el requisito de la empresa para crear la oferta? Cuando se publica una disponibilidad de empleo, la hace la empresa con sus requisitos; falta que la empresa cree la oferta antes de que el graduado postule.
- **[07:50–08:35] Baja, cancelación y cierre de ofertas (`RF-06`, `RF-07`):**
  - **Ing. Washington Casanova:** También hace falta dar de baja o desactivar la publicación por parte de la empresa misma, por dos motivos: porque ya logró contratar a los postulantes requeridos (estado *contratados*) o porque desistió y cancela la oferta.
- **[08:50–09:05] Disponibilidad y preferencias de alertas del graduado (`RF-01`, `RF-10`):**
  - **Ing. Washington Casanova:** Asumo que en la gestión del perfil el graduado indica si está disponible o no; por ejemplo, si ya está trabajando y no quiere recibir notificaciones.
- **[09:15–10:35] Revisión de requisitos no funcionales (`RNF-01`, `RNF-04`, `RNF-06`):**
  - **Ing. Washington Casanova:** Eviten requisitos no funcionales repetitivos; la interfaz debe ser rápida, intuitiva, con *feedback* y control de errores claro, y separar claramente los requisitos de seguridad.

### Parte 2 — `Requisitos_02.opus` (`04:20`)

- **[00:00–00:50] Revisión y selección de postulantes por empresa (`RF-08`):**
  - **Ing. Washington Casanova:** En los requisitos funcionales de la empresa sí tienen registrar ofertas laborales, pero falta seleccionar postulantes: visualizar postulantes, contactar con los elegidos y aceptar postulaciones.
- **[00:50–01:25] Control administrativo de usuarios (`RF-09`):**
  - **Ing. Washington Casanova:** Además de validar ofertas y generar reportes, el administrador debe tener control de usuarios para admitir o dar de baja a alguien que se registre indebidamente o realice mal uso del sistema.
- **[01:28–01:36] Confirmación de grabación:**
  - **Ing. Washington Casanova:** ¿Ya está grabando, sí? — *Estudiante:* Sí, estoy grabando. — *Ing. Casanova:* Arriba no lo veía, pero acá ya lo veo.
- **[01:45–02:35] Cuentas UTEQ y caducidad del correo institucional (`RF-01`, `RF-02`):**
  - **Ing. Washington Casanova:** Como esto está enfocado en graduados de la universidad, el administrador debe poder dar de baja a quien no corresponda a la UTEQ. Y tomen en cuenta que **los correos institucionales de estudiantes se dan de baja normalmente después de cinco años**, por lo que no se puede depender indefinidamente solo del correo estudiantil activo.
- **[03:11–04:15] Notificaciones automáticas sobre ofertas externas (`RF-10`, `RNF-02`):**
  - **Ing. Washington Casanova:** En el proceso automatizado de recolección faltan las notificaciones: si el sistema importa una oferta externa compatible (por ejemplo, de programador), ¿cómo se le notifica al graduado? No puede hacerlo manualmente el administrador revisando una por una; tiene que hacerlo **automáticamente el propio sistema** enviándole el aviso por correo al graduado.
