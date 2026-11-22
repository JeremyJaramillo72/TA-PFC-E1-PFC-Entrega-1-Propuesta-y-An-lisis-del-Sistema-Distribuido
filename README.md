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
| Luis Alberto Paca Pilataza | Responsable de Documentación |

> **Nota de autoría en GitHub:** la cuenta principal de **Luis Alberto Paca Pilataza** es `@Luis-paca`. El commit `395b1ad` (19/11/2026, Issue `#16`) también corresponde a su autoría y se registró puntualmente bajo su cuenta personal secundaria `@Luispaca2002` debido a una configuración previa en el `.gitconfig` local, corregida posteriormente a `@Luis-paca`.

## Video de presentación
Video de presentación del proyecto (5–7 min) correspondiente a la entrega `TA-PFC-E1` de **Aplicaciones Distribuidas (`ISR-701`)**.

- **Enlace:** pendiente de publicación.
- **Fecha planificada de grabación:** por definir.

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
```

## Ejecución del esqueleto gRPC (E1)
El esqueleto está formado por dos procesos que se comunican mediante gRPC según el contrato `proto/bolsa_uteq.proto` (ver `docs/adr/ADR-002-mecanismo-comunicacion.md`):

| Proceso | Archivo | Rol gRPC |
| :--- | :--- | :--- |
| `servicio-perfiles` | `src/servicio_perfiles/servidor_perfiles.py` | Servidor de `PerfilService` en el puerto `50051` |
| `servicio-postulaciones` | `src/servicio_postulaciones/cliente_postulaciones.py` | Cliente que invoca `VerificarElegibilidad` y registra postulaciones |

> **Datos de prueba:** el padrón en memoria usa solo identificadores ficticios (`GRAD-TEST-001`, `GRAD-TEST-002`, `GRAD-TEST-003`). El servidor rechaza con `INVALID_ARGUMENT` cualquier ID vacío o que no siga el formato `GRAD-XXXX-NNN`; nunca se usan números de cédula reales.

### 1. Clonar el repositorio
```bash
git clone https://github.com/JeremyJaramillo72/TA-PFC-E1-PFC-Entrega-1-Propuesta-y-An-lisis-del-Sistema-Distribuido.git
cd TA-PFC-E1-PFC-Entrega-1-Propuesta-y-An-lisis-del-Sistema-Distribuido
```

### 2. Instalar dependencias
Requiere Python 3.10 o superior.
```bash
pip install -r requirements.txt
```

### 3. Compilar `proto/bolsa_uteq.proto` hacia `src/generated/`
Los stubs ya están versionados en `src/generated/`; este paso es obligatorio solo si se modifica el `.proto`.
```bash
python scripts/generar_stubs.py
```
Comando equivalente sin el script:
```bash
python -m grpc_tools.protoc -I proto --python_out=src/generated --grpc_python_out=src/generated proto/bolsa_uteq.proto
```

### 4. Terminal 1: iniciar `servicio-perfiles`
```bash
python src/servicio_perfiles/servidor_perfiles.py
```
Salida esperada: `[servicio-perfiles] Escuchando gRPC en puerto 50051 | Equipo=... | PID=...`. Dejar esta terminal abierta.

### 5. Terminal 2: ejecutar `servicio-postulaciones`
```bash
python src/servicio_postulaciones/cliente_postulaciones.py
```
El cliente ejecuta estos casos y muestra un resumen al final:

| Caso | ID enviado | Resultado esperado |
| :--- | :--- | :--- |
| (a) Postulación válida | `GRAD-TEST-002` → `OF-2026-001` | `ACEPTADA` |
| (b) Reintento duplicado (RNF-05) | `GRAD-TEST-002` → `OF-2026-001` | `DUPLICADA` (no se registra dos veces) |
| (c) ID mal formado | `ID-INVALIDO` | `RECHAZADA` por `INVALID_ARGUMENT` |
| (c) ID vacío | `""` | `RECHAZADA` por `INVALID_ARGUMENT` |
| (d) ID válido no registrado | `GRAD-TEST-999` | `RECHAZADA` (`NO ELEGIBLE`) |

Cada llamada usa un *deadline* de 2 s. Los errores `UNAVAILABLE` (servidor apagado), `DEADLINE_EXCEEDED` (servidor lento) e `INVALID_ARGUMENT` se informan por consola sin detener el script.

Para apuntar a `servicio-perfiles` en otro equipo de la red, definir `PERFILES_ADDR` antes de ejecutar el cliente:
- Bash: `export PERFILES_ADDR=<ip>:50051`
- PowerShell: `$env:PERFILES_ADDR="<ip>:50051"`

### 6. Pruebas de contrato e integración
```bash
python -m unittest discover -s tests -v
```

## Compilación del informe técnico (LaTeX)
- **Compilador y procesador bibliográfico:** `pdflatex` (TeX Live 2023+ o MiKTeX) y `biber` (para `biblatex` con estilo `ieee`).
- **Archivo principal:** `docs/main.tex` (usa `docs/referencias.bib`, las figuras en `docs/figuras/` y las capturas en `evidencias/`).
- **Dependencias de paquetes LaTeX:** `inputenc`, `fontenc`, `babel` (`spanish`, `es-tabla`), `geometry`, `amsmath`, `graphicx`, `booktabs`, `tabularx`, `xurl`, `hyperref`, `biblatex` y `biber`.

Orden exacto de comandos desde la raíz del repositorio:
```bash
cd docs
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```
Al finalizar se genera `docs/main.pdf` con tabla de contenido, referencias cruzadas y bibliografía IEEE resueltas.
