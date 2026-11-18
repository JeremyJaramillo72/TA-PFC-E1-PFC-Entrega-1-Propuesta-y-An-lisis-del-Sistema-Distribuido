# ADR-001: Selección del estilo de arquitectura distribuida

- **Estado:** Aceptado
- **Fecha:** 2026-11-17
- **Autor:** Luis Jeremy Jaramillo Acosta (Arquitecto)

## Contexto
La plataforma **Bolsa de Empleos para Graduados de la UTEQ** debe sostener simultáneamente dos cargas de trabajo con comportamiento operativo opuesto:
1. **Operaciones transaccionales interactivas:** gestión de perfiles académicos de graduados, revisión y validación administrativa de vacantes por parte de la coordinación de carrera y registro de postulaciones directas, flujos que exigen baja latencia y alta disponibilidad durante el periodo académico.
2. **Ingesta periódica desde portales externos (Web Scraping):** recolección automatizada y verificación de vigencia de ofertas laborales externas, tarea intensiva en entrada/salida de red y sujeta a latencias variables o bloqueos por parte de servidores de terceros.

## Opciones consideradas
1. **Arquitectura monolítica en capas con base de datos única:** una sola unidad desplegable. Se descarta porque un pico de consumo de recursos o bloqueo durante la sincronización de ofertas externas degrada el tiempo de respuesta de las postulaciones en vivo y obliga a redesplegar todo el sistema ante cambios en los extractores.
2. **Arquitectura orientada a servicios (SOA) con ESB centralizado:** introduce un bus empresarial pesado que incrementa la complejidad operativa y crea un punto único de fallo para un equipo de cuatro integrantes.
3. **Arquitectura de microservicios desacoplados orientados a dominio:** divide el sistema en servicios independientes (`Perfiles`, `Ofertas y Validación`, `Postulaciones`, `Ingesta Externa` y `Notificaciones`), cada uno con persistencia propia y despliegue aislado.

## Decisión tomada
Adoptar una **arquitectura de microservicios desacoplados orientados a dominio**, desplegados como contenedores independientes detrás de un *API Gateway*.

## Consecuencias
- **Positivas:** aislamiento de fallos entre el módulo de ingesta externa y el flujo crítico de postulaciones, escalado horizontal selectivo según demanda y despliegue modular en las entregas E2 a E4.
- **Negativas:** exige gestionar consistencia eventual para las ofertas importadas y las notificaciones por correo, además de mantener contratos de interfaz estrictos entre servicios.
