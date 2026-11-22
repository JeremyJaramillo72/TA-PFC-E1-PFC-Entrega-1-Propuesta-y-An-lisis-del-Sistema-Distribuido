# Entrevista 01 — Levantamiento real de información (TA-PFC-E1)

- **Fecha y hora:** 26/06/2025 — 15:48 *(levantamiento inicial del dominio Bolsa de Empleos UTEQ retomado como base verificable del PFC)*
- **Modalidad / Lugar:** Presencial — Universidad Técnica Estatal de Quevedo (UTEQ)
- **Entrevistado:** Ing. Washington Casanova — Docente de la Carrera de Ingeniería en Software (UTEQ) y revisor académico del dominio *(sin datos sensibles)*
- **Entrevistadores:** Integrantes del equipo de Ingeniería en Software UTEQ
- **Archivo original en Drive:** `AUDIO-2025-06-26-15-48-02.m4a` (duración `13:42`, peso `6,4 MB`; alojado externamente en Google Drive por privacidad y control de acceso)
- **Consentimiento de grabación:** Confirmado al inicio del audio en `[00:02]` (*"¿Ya está?" / "Sí"*) y reiterado verbalmente en la sesión posterior de verificación de requisitos con el mismo entrevistado (`Requisitos_02.opus`, `[01:28–01:36]`: *"¿Ya está grabando, sí? ... Sí, lo está grabando"*).
- **Enlace público al audio original (verificado en incógnito):** https://drive.google.com/file/d/1wLVgo2Ycx9ftMxjBgh1ZEE-gRthrDFOE/view?usp=sharing
- **Enlace público a la transcripción PDF original en Drive:** https://drive.google.com/file/d/1tAjtKsFfzgdbqO3BdWTKOAsj2tjuugdg/view?usp=sharing
- **Carpeta pública de entrevistas:** https://drive.google.com/drive/folders/1Tuj7LALrMUyvxrVDbiNIE_z8ARsqIixv?usp=sharing

---

## Resumen de hallazgos medibles (según lo dicho en la entrevista)

- **Cómo resuelven hoy el problema:**
  - Las empresas envían únicamente folletos informales solicitando comunicarse por correo (`[01:14–01:23]`).
  - Los propios graduados difunden vacantes de manera informal en un **grupo de WhatsApp de graduados** (`[09:30–09:57]`).
  - Al buscar en la web de forma general, se encuentran noticias sobre demanda laboral pero muy rara vez la vacante concreta de una empresa (`[02:15–02:27]`).
- **Consecuencias medibles (tiempos, errores y credibilidad):**
  - **Desajuste perfil–oferta:** en redes externas llegan avisos sin relación con la carrera (p. ej., vacantes de arquitecto enviadas a un ingeniero en software, `[04:12–04:29]`).
  - **Subempleo sin visibilidad institucional:** graduados de software trabajando fuera de su área (p. ej., de cajero en un centro comercial) sin métricas institucionales claras de inserción o salario promedio (`[06:02–06:29]`, `[12:47–13:15]`).
  - **Saturación de postulantes sin filtro:** cuando una empresa solicita programadores puede recibir ~20 carpetas sin priorización ni verificación académica, lo que hace perder credibilidad y desalienta futuras publicaciones (`[09:05–09:20]`, `[10:06–10:44]`).
  - **Desactualización de perfiles:** los graduados abandonan plataformas que les piden reingresar sus datos repetidamente; solo conviene solicitar actualización incremental cuando llevan tiempo sin actualizar (p. ej., tras 2 años, o al completar una maestría o certificación, `[07:38–08:24]`).
- **Expectativas frente a la plataforma:**
  - Registro y hoja de vida claros con filtrado por carrera, áreas de interés adicionales y experiencia (`[00:16–00:59]`, `[04:32–05:37]`).
  - Validación obligatoria de toda oferta publicada por un administrador (coordinador de carrera) para garantizar autenticidad (`[10:58–11:10]`).
  - Validación de graduados reales mediante padrón institucional extraído del **SGA** al cierre de cada periodo académico (`[11:30–12:19]`).
  - Reportes institucionales de empleabilidad (porcentaje trabajando, sueldo promedio, situación laboral) y notificaciones por correo de ofertas/capacitaciones (`[02:53–03:11]`, `[06:45–07:17]`, `[12:47–13:15]`).

---

## Transcripción fiel con marcas de tiempo (auditada contra el audio original)

- **[00:02] Entrevistador / Entrevistado:** "¿Ya está?" — "Sí."
- **[00:06] Entrevistador:** Bueno, la primera pregunta sería: ¿qué es lo primero que usted espera encontrar al ingresar a una bolsa de empleo como usuario, como un graduado?
- **[00:16] Ing. Washington Casanova:** Si fuera un graduado, esperaría poder visualizar qué oportunidades laborales se me están ofreciendo dentro de mi perfil laboral. Por ejemplo, si soy graduado de software, quisiera ver si hay empresas que están pidiendo contratos de software, de ingenieros de software.
- **[00:36] Entrevistador:** Que se filtren sobre las ofertas laborales debido a su perfil.
- **[00:39] Ing. Washington Casanova:** Sí.
- **[00:41] Entrevistador:** ¿Qué funcionalidades considera usted que sean indispensables para que realmente sirva una bolsa de empleo universitaria?
- **[00:50] Ing. Washington Casanova:** Tendría que haber un buen registro y perfil de cada alumno, donde esté su hoja de vida claramente establecida. Otra cosa importante sería que obviamente las empresas conozcan ese sitio web y pongan sus requerimientos allí, o haya un encargado de poner los requerimientos de contratación en la aplicación. A veces las empresas nos envían solo un folleto: *"Se requiere contratar ingeniero de software, comunicarse a tal correo"*, y nos mandan así nada más los requerimientos.
- **[01:24] Entrevistador:** En ese caso tengo una duda: ¿es recomendable tener abierta esa parte para que las empresas ingresen al sistema y publiquen sus ofertas laborales, o recopilar todas las ofertas laborales con el método de *web scraping*? ¿Cuál sería más recomendable?
- **[01:49] Ing. Washington Casanova:** El *web scraping* es una alternativa que te hace escanear una página web, pero es solo una página web. Tendrías que tener un método para buscar a nivel de toda la web esas ofertas laborales; por eso normalmente no se logra mucho. Si tú buscas en internet ofertas laborales de ingenieros de software, vas a encontrar noticias de que se requiere contratar muchos y que hay alta demanda, pero específicamente la empresa que está contratando muy rara vez vas a encontrar algo.
- **[02:30] Ing. Washington Casanova:** Lo que sí existe son redes como LinkedIn —y hay otras tres más conocidas— donde la gente sube su hoja de vida y las empresas que necesitan contratar publican en LinkedIn. LinkedIn es un programa que se encarga de ver: este es ingeniero de software y acá están solicitando ingenieros de software, los ubica y te manda un correo diciendo *"acá están ofreciendo trabajo"*. Tú con tu correo entras, te sale una lista de ofertas y dices *"ah, me gusta esta, me gusta esta"*; entras y ves la información. La información tiene que ser clara: te tiene que decir, por ejemplo, cuántas horas vas a trabajar, si vas a estar asegurado. Normalmente no ponen el sueldo por competitividad, pero funciona como red social. Acá, como bolsa de empleo, buscar en internet siempre es una alternativa, y también existen redes como LinkedIn que ofrecen APIs (de pago) para acceder a sus bases de datos y agregarlas a tu software.
- **[04:03] Entrevistador:** Desde su experiencia, ¿qué errores comunes ve en plataformas similares que deberíamos evitar?
- **[04:12] Ing. Washington Casanova:** Justamente el cruce entre oferta y tipo de graduado; el perfil del graduado es lo que muchas veces falla. Me llega por ejemplo un mensaje de LinkedIn diciendo que solicitan arquitecto, pero yo soy de software, no me interesa. Además, yo puedo ser ingeniero de software, pero no tendría problemas si me ofrecen una oportunidad laboral como profesor porque soy capaz de enseñar programación, arquitectura o matemáticas. Cuando me registre como graduado, pongo mi profesión pero también qué intereses tengo y en qué áreas; no puedo restringirme solo al título. Cuando haya una oferta de profesor de matemáticas me debe llegar la noticia. En eso suelen fallar las redes: solamente ponen el perfil profesional y no intereses adicionales.
- **[05:25] Entrevistador:** Por ejemplo, filtrar por carrera, por intereses o experiencia. ¿Qué sensación o experiencia debería tener un graduado al usar la plataforma para que realmente quiera volver a usarla?
- **[05:48] Ing. Washington Casanova:** El software de seguimiento a graduados tiene dos enfoques. El primero es saber cómo le va al graduado y en qué está desempeñándose: nos interesa saber si está trabajando o no, dónde trabaja, qué tan bueno es su sueldo, qué niveles jerárquicos tiene la empresa, si tiene su propia empresa, o si es graduado de software pero está trabajando de cajero en el *shopping*. Eso es importante por un lado: conocer la realidad del graduado.
- **[06:31] Ing. Washington Casanova:** Al graduado le interesaría registrar sus datos siempre que reciba algo que lo motive: por ejemplo, la bolsa de trabajo (recibir constantemente ofertas laborales), cursos de capacitación gratuita, participación en conferencias y noticias actualizadas. Por un lado está el interés de que pongan sus datos y por otro usar la bolsa de empleo para mantenerlo en contacto con la universidad. Si le llega una oferta laboral y no ha ingresado datos desde hace dos años, al hacer clic le dice *"actualiza tus datos"*, igual que pasa en LinkedIn —siempre que no sea muy recurrente, porque a los graduados les molesta que a cada rato les pregunten información que ya ingresaron—. Solo interesa que actualice si hizo una maestría o un curso de capacitación (p. ej., Cisco); si no ha cambiado nada, puede dejarlo así.
- **[08:28] Entrevistador:** ¿Qué papel debería tener la universidad dentro de esta plataforma: solo como respaldo o también como guía activa?
- **[08:38] Ing. Washington Casanova:** La universidad siempre tiene que estar activa, justamente para que el graduado sienta que está en contacto e incluso reciba noticias interesantes de la UTEQ.
- **[08:51] Entrevistador:** ¿Cómo se manejaría la transparencia respecto a las empresas que publican ofertas y qué deberíamos evitar para no perder credibilidad?
- **[09:05] Ing. Washington Casanova:** Las empresas también tienen que tener la seguridad de que la información que ponen está enfocada a lo que quieren. Si una empresa se da cuenta de que le enviamos hojas de vida que no son apropiadas, ya no le va a interesar volver a publicar. El software debería tener una especie de enfoque de red social para que haya participación. Así nos pasa en el grupo de WhatsApp de los graduados: un graduado que ascendió y se convirtió en jefe publica *"necesito programadores"* y pide graduados nuestros porque son buenos; los mismos graduados se convierten en difusores de ofertas laborales a sus propios compañeros.
- **[10:06] Ing. Washington Casanova:** Para mantener la seguridad de las empresas, siempre deben ser filtradas las propuestas. Si solicitan programadores, a lo mejor habrá 20 carpetas pidiendo ese cargo; la universidad debería filtrar o dar prioridad por categoría (por ejemplo, quien tiene maestría o buen promedio y recomendaciones). Esas valoraciones son importantes para que la empresa se mantenga.
- **[10:46] Entrevistador:** En cuanto a las ofertas publicadas, ¿quién se encargaría de administrar y verificar si son ofertas reales de empresas reales?
- **[10:58] Ing. Washington Casanova:** Toda oferta tiene que ser validada. Alguien tiene que encargarse de la administración del sistema y validar que esas ofertas sean creíbles; normalmente lo hace el coordinador de la carrera.
- **[11:20] Entrevistador:** ¿Lo mismo pasaría con quienes se van a postular, que pasen por un administrador que vea que sí son graduados de la universidad?
- **[11:30] Ing. Washington Casanova:** Sí, pero eso lo podríamos hacer directamente con información extraída del SGA. Cada periodo que termina, una vez que los alumnos cumplen los requisitos, sacamos la lista de graduados y esa lista debe subirse al sistema como carga masiva: sacamos del SGA todos los graduados con sus datos de identificación, carrera y promedios, y con un clic (cargando el archivo Excel) se sube a la base de datos del sistema de graduados.
- **[12:21] Entrevistador:** Por último, si usted diseñara la plataforma desde cero, ¿qué funcionalidad innovadora incluiría?
- **[12:33] Ing. Washington Casanova:** Se podría aplicar minería de datos e inteligencia artificial para cotejar la compatibilidad entre participantes y ofertas laborales. También interesa mucho analizar la situación de los graduados: tener todos los graduados de software y sacar estadísticas de cuántos están trabajando, cuál es su sueldo promedio y su situación laboral. Eso se aplica en un nivel superior cuando ya se tienen los datos capturados por la aplicación.
- **[13:30] Entrevistador:** Muchas gracias ingeniero por su tiempo.
- **[13:37] Ing. Washington Casanova:** Gracias a ustedes.
