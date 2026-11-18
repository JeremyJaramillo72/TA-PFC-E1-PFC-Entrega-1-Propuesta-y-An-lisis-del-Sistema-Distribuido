# ADR-002: Mecanismo de comunicación principal entre servicios

- **Estado:** Aceptado
- **Fecha:** 2026-11-17
- **Autor:** Kenny Isaías España Vera (Líder de Desarrollo)

## Contexto
Al dividir la **Bolsa de Empleos UTEQ** en microservicios, el servicio encargado de registrar postulaciones necesita verificar de forma síncrona e inmediata que el graduado esté habilitado en el padrón y que la vacante se encuentre aprobada antes de confirmar la solicitud. Por el contrario, el envío de alertas por correo electrónico y la sincronización periódica de vacantes externas pueden ejecutarse sin bloquear la respuesta al usuario.

## Opciones consideradas
1. **REST/JSON sobre HTTP/1.1 entre todos los servicios internos:** sencillo de depurar manualmente, pero con mayor sobrecarga por serialización textual y sin validación estricta de contratos binarios en tiempo de compilación.
2. **gRPC (HTTP/2 + Protocol Buffers) para llamadas síncronas internas, REST en el borde público y mensajería asíncrona (AMQP) para eventos:** contratos fuertemente tipados definidos en archivos `.proto`, serialización binaria compacta y multiplexación sobre HTTP/2, reservando colas de mensajes para tareas en segundo plano.
3. **Mensajería asíncrona pura para todos los flujos:** desacopla los servicios, pero complica innecesariamente la validación inmediata de elegibilidad durante una postulación interactiva.

## Decisión tomada
Establecer **gRPC sobre HTTP/2 con Protocol Buffers** como mecanismo principal de comunicación síncrona interna entre microservicios, manteniendo **REST/JSON** únicamente en la fachada externa (`API Gateway` hacia el cliente web) y **mensajería asíncrona (AMQP)** para notificaciones y sincronización de ofertas externas.

## Consecuencias
- **Positivas:** contratos de interfaz explícitos y versionables en `/proto/`, menor latencia de serialización y transporte frente a JSON textual y generación automática de clientes y servidores.
- **Negativas:** requiere compilar el archivo `.proto` ante cambios de esquema y emplear clientes gRPC específicos para pruebas de integración.