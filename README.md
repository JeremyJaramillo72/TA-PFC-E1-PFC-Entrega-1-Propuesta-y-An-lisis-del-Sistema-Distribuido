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
├── evidencias/             # Actas/encuestas, fotografías de diseño y capturas
├── requirements.txt        # Dependencias de Python
├── BITACORA.md             # Registro cronológico de sesiones del equipo
└── README.md               # Guía general y de compilación
