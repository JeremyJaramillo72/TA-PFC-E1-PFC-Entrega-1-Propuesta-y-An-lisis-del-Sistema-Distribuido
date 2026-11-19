# Bolsa de Empleos para Graduados UTEQ — Sistema Distribuido (PFC)

Proyecto Fin de Curso — Entrega 1 (`TA-PFC-E1`), asignatura **Aplicaciones Distribuidas (`ISR-701`)**, Universidad Técnica Estatal de Quevedo (UTEQ), SPA 2026-2027.

## Descripción del proyecto
Plataforma distribuida basada en microservicios para gestionar la inserción laboral de los graduados de la UTEQ, integrando validación administrativa de vacantes publicadas por empresas colaboradoras, importación periódica de ofertas externas mediante *web scraping* y alertas personalizadas.

## Integrantes y roles
| Integrante | Rol en el proyecto  |
| :--- | :--- |
| Luis Jeremy Jaramillo Acosta | Arquitecto |
| Kenny Isaías España Vera | Líder de Desarrollo |
| Heiner Ariel Zambrano Ronquillo | Responsable de Calidad |
| Luis Paca | Responsable de Documentación |

## Estructura del repositorio
```text
├── proto/                  # Contratos de interfaz Protocol Buffers (.proto)
├── src/                    # Código fuente de los microservicios del esqueleto
├── docs/
│   ├── adr/                # Registros de decisiones de arquitectura (ADR)
│   ├── diagramas/          # Diagramas editables (.drawio)
│   ├── figuras/            # Exportaciones gráficas para el informe
│   ├── main.tex            # Documento LaTeX principal
│   ├── referencias.bib     # Bibliografía en formato IEEE
│   └── main.pdf            # Informe técnico compilado
├── scripts/                # Utilidades (regeneración de stubs gRPC)
├── tests/                  # Pruebas de contrato e integración gRPC
├── evidencias/             # Actas/encuestas, fotografías de diseño y capturas
├── requirements.txt        # Dependencias de Python
├── BITACORA.md             # Registro cronológico de sesiones del equipo
└── README.md               # Guía general y de compilación

## Ejecución del esqueleto gRPC (E1)
El esqueleto está formado por dos procesos que se comunican mediante gRPC según el contrato `proto/bolsa_uteq.proto` (ver `docs/adr/ADR-002-mecanismo-comunicacion.md`):

| Proceso | Archivo | Rol gRPC |
| :--- | :--- | :--- |
| `servicio-perfiles` | `src/servicio_perfiles/servidor_perfiles.py` | Servidor de `PerfilService` en el puerto `50051` |
| `servicio-postulaciones` | `src/servicio_postulaciones/cliente_postulaciones.py` | Cliente que invoca `VerificarElegibilidad` |

1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. (Solo si se modifica el `.proto`) regenerar los stubs en `src/generated/`:
   ```bash
   python scripts/generar_stubs.py
   ```
3. Iniciar el servidor de perfiles en una terminal:
   ```bash
   python src/servicio_perfiles/servidor_perfiles.py
   ```
4. Ejecutar el cliente de postulaciones en otra terminal. Consulta un graduado habilitado y una cédula no registrada:
   ```bash
   python src/servicio_postulaciones/cliente_postulaciones.py
   ```
   Para apuntar a otro equipo de la red: `PERFILES_ADDR=<ip>:50051` (en PowerShell: `$env:PERFILES_ADDR="<ip>:50051"`).
5. Ejecutar las pruebas de contrato e integración:
   ```bash
   python -m unittest discover -s tests -v
   ```
