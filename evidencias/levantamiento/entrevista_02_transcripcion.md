# Entrevista 02 — Levantamiento real de información (TA-PFC-E1)

- **Fecha y hora:** 28/06/2025 — 20:02 *(levantamiento real del dominio Bolsa de Empleos UTEQ retomado como base verificable del PFC)*
- **Modalidad / Lugar:** Virtual — Videollamada grabada (`2025-06-28 20-02-05.mkv`, peso `617 MB`, duración `> 30 min`)
- **Entrevistado:** Ing. Roberto Suárez — Graduado de Ingeniería en Software (UTEQ) y autor de proyecto de titulación previo de Bolsa de Empleo con *web scraping* y modelo multicriterio MCDA *(sin datos sensibles)*
- **Entrevistadores:** Luis Jeremy Jaramillo Acosta y Kenny Isaías España Vera (integrantes del equipo EJPZ)
- **Consentimiento expreso:** Confirmado verbalmente al inicio de la grabación (`[~00:35–00:50]`):
  > *Entrevistador:* «Bueno, antes de todo, queremos pedirle si podemos grabar esta conversación que tenemos con usted, antes de la pregunta.»
  > *Ing. Roberto Suárez:* **«Claro, sí. Pueden grabar, tienen mi consentimiento.»**
- **Enlace público al video original (verificado en incógnito; no se sube el `.mkv` al repositorio por exceder 100 MB):** https://drive.google.com/file/d/11yOiwRPzICeTAhPC1dNMYhxjpdF6AivO/view?usp=sharing
- **Enlace público a la transcripción PDF original en Drive:** https://drive.google.com/file/d/1-KYshqFmUTSCuAQsAzq_nu3GRfGY_xbK/view?usp=sharing

---

## Resumen de hallazgos medibles (según lo dicho en la entrevista)

- **Cómo resuelven hoy el problema:**
  - La UTEQ no dispone de una bolsa de empleo oficial implementada en producción (su proyecto de tesis anterior no fue desplegado institucionalmente).
  - La recolección manual de ofertas laborales resulta impráctica por tiempo y costo; los estudiantes y graduados buscan de forma dispersa en portales externos como CompuTrabajo y Multitrabajo.
- **Consecuencias medibles (tiempos, costos y errores):**
  - **Desfase temporal y subempleo:** muchos graduados demoran largo tiempo en conseguir su primer empleo o terminan trabajando en áreas no correlacionadas con su formación (p. ej., graduados de Administración de Empresas trabajando en ventas o marketing).
  - **Costo y tiempo de carga manual vs. automatizada:** ingresar manualmente **1.000 ofertas laborales al mes** requeriría personal dedicado con un costo estimado de **\$600 mensuales**; en contraste, un servicio automatizado de *web scraping* + ETL procesa esas **1.000 ofertas en aproximadamente 2 horas** con un costo aproximado de **\$0,10** en procesamiento asistido.
  - **Ofertas expiradas / desactualizadas:** las vacantes extraídas de portales externos caducan o desaparecen del sitio de origen (después de 2–3 meses o 1 año); si no se valida su fecha de publicación o vigencia, el portal exhibe ofertas muertas.
  - **Fallas funcionales que provocan abandono:** plataformas lentas o con restricciones rígidas (como rechazar un CV en PDF de 2 o 3 hojas por admitir solo 1 hoja) hacen que el graduado deje de usar la aplicación.
- **Expectativas frente a la plataforma:**
  - Tres roles diferenciados: graduado, empresa y administrador aprobador que certifique que la empresa es real (por correo o documentación) antes de publicar ofertas.
  - Buscador avanzado con filtros por área específica, rango salarial y empresa (no solo palabras clave).
  - Carga de currículum en PDF multipágina con margen suficiente de tamaño, interfaz rápida, eficiente y bien probada.
  - Despliegue real accesible (no solo local) e ingesta automatizada de portales externos con descarte de ofertas vencidas.

---

## Transcripción fiel (basada en el video original y documento `Entrevista Ing.Roberto Suarez.pdf`)

- **[Inicio — Presentación y consentimiento expreso]**
  - **Entrevistador (Kenny España):** Hola, buenas noches, ingeniero Roberto. Para informar un poquito, nosotros somos estudiantes de la carrera de software; aquí estamos mi compañero Jeremy Jaramillo y mi persona, Kenny España. Agradecemos por su tiempo. Actualmente estamos desarrollando una actividad enfocada a la recolección de requerimientos para un sistema de bolsa de empleo universitario y buscamos conocer antecedentes y experiencias reales. Antes de todo, queremos pedirle si podemos grabar esta conversación que tenemos con usted.
  - **Ing. Roberto Suárez:** Claro, sí. Pueden grabar, tienen mi consentimiento.

- **[Bloque 1 — Antecedentes y problema actual en la UTEQ]**
  - **Entrevistador:** Ya que sabemos que usted realizó su tesis sobre una bolsa de empleo, ¿está familiarizado con los sistemas de bolsa de empleo implementados por universidades? ¿Su proyecto corre actualmente de forma oficial en la UTEQ?
  - **Ing. Roberto Suárez:** Sí, he estado familiarizado. Cuando estuve en séptimo u octavo semestre, para prácticas preprofesionales me solicitaron hacer una bolsa de empleo y conocí la necesidad en la UTEQ: había muchos graduados sin puesto laboral y la universidad aspiraba a una herramienta para hacer una búsqueda más eficiente. Sin embargo, el proyecto que realicé no está implementado oficialmente en la UTEQ; fue únicamente un trabajo de tesis.
  - **Ing. Roberto Suárez:** Realmente es un problema que la UTEQ no cuente con una bolsa oficial: en varias carreras muchos alumnos no consiguen trabajo o se demoran muchísimo tiempo en conseguirlo. Con una bolsa oficial la universidad tendría mayor representación, abarcaría más empresas y los graduados podrían conseguir su primera oferta laboral en menos tiempo y correlacionada con lo que estudiaron. Por ejemplo, existen graduados de Administración de Empresas que terminan trabajando en ventas o marketing sin relación directa con su formación. Tanto empresas privadas como públicas se benefician al contratar profesionales calificados formados en la carrera correspondiente (por ejemplo, Ingeniería en Software para desarrollo).

- **[Bloque 2 — Flujo de actores, validación de empresas y buscador avanzado]**
  - **Entrevistador:** ¿Qué recomendaría y qué espera encontrar al ingresar a una bolsa de empleo para graduados? ¿Quién debe validar que una oferta laboral provenga de una empresa real?
  - **Ing. Roberto Suárez:** Lo principal es tener claro el escenario, los requerimientos funcionales y no funcionales, las tecnologías y el despliegue en la nube (para que no quede solo en una laptop). Deben contemplar cuentas de usuarios que buscan empleo, cuentas de empresas y un tercer actor administrador o aprobador de usuarios.
  - **Ing. Roberto Suárez:** El flujo para empresas debe ser: registrarse como empresa, pasar por validación de identidad (mediante correo corporativo o documento/credencial que certifique pertenencia a la empresa revisado por el administrador) y, una vez aprobada, poder publicar sus ofertas con todos sus detalles. Del lado del graduado, debe registrarse, iniciar sesión y contar con un buscador avanzado que no se limite a palabras clave, sino que permita filtrar por área específica, rango salarial y empresa.

- **[Bloque 3 — Experiencia de usuario, desempeño y carga de CV PDF]**
  - **Entrevistador:** ¿Qué sensación o experiencia debería tener un graduado al usar la plataforma para que realmente quiera volver a usarla?
  - **Ing. Roberto Suárez:** Es clave tener un diseño minimalista y funcional, que la plataforma sea rápida, eficiente y que las funcionalidades estén bien probadas y no fallen. Conocí una aplicación con muchos módulos, pero en la primera función que probé —subir el currículum vitae— solo permitía subir un PDF de una sola hoja. Mi CV tiene dos o tres hojas, así que no pude volver a usarla. Si la aplicación es intuitiva, permite subir un PDF de varias hojas y mayor peso y devuelve respuestas correctas, el graduado vuelve a utilizarla. En cambio, extras como chats de IA mal desarrollados o animaciones excesivas consumen tiempo de desarrollo sin aportar valor real.

- **[Bloque 4 — Ingesta externa (*Web Scraping*), impacto en costos/tiempos y caducidad de ofertas]**
  - **Entrevistador:** Si volviera a diseñar la plataforma desde cero, ¿qué funcionalidad innovadora incluiría y cómo evitaría recopilar ofertas expiradas o desactualizadas?
  - **Ing. Roberto Suárez:** En mi tesis implementé un servicio de extracción de ofertas laborales mediante *web scraping* sobre plataformas como CompuTrabajo y Multitrabajo, siguiendo un proceso ETL (*Extract, Transform, Load*) con apoyo de modelos económicos para estructurar campos faltantes de la descripción y cargarlos a la base de datos.
  - **Ing. Roberto Suárez:** Ese servicio es muy importante: si una persona quisiera ingresar **1.000 ofertas laborales al mes** manualmente, demoraría muchísimo tiempo y cobraría alrededor de **\$600 mensuales**. En cambio, el servicio automatizado tomaba aproximadamente **2 horas** para ingresar esas **1.000 ofertas** con un costo cercano a **\$0,10**. Además implementé un modelo de decisión multicriterio (MCDA) para ordenar las ofertas según las preferencias del perfil (palabras clave, rango salarial, prestigio de empresa).
  - **Ing. Roberto Suárez:** Sobre ofertas expiradas: sí me sucedió que ofertas extraídas luego expiraban o desaparecían del sitio original. Para controlarlo hay que verificar la fecha de publicación durante el *scraping* —descartando automáticamente vacantes antiguas (p. ej., de 2 o 3 meses o 1 año)— y verificar vigencia para deshabilitar las ofertas que ya no existen en el portal origen.

> *Nota de integridad:* La transcripción automática original en Drive (`Entrevista Ing.Roberto Suarez.pdf`) cubre los primeros 30 minutos del video `2025-06-28 20-02-05.mkv`. El video íntegro permanece accesible mediante el enlace público superior para verificación directa.
