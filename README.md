# SystemDSL

Compilador que genera sistemas funcionales completos a partir de modelos de dominio escritos en un lenguaje específico (DSL). A partir de un único fichero `.dsl`, el compilador produce una API REST con FastAPI, esquema de base de datos PostgreSQL, documentación OpenAPI y configuración de despliegue con Docker.

---

## Requisitos

| Herramienta | Versión mínima | Uso |
|---|---|---|
| Python | 3.11+ | Ejecutar el compilador |
| Java | 17+ | Regenerar el parser ANTLR4 (solo si modificas la gramática) |
| Docker | 24+ | Levantar la API y PostgreSQL generados |
| Docker Compose | 2.0+ | Orquestar los contenedores |

---

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/system-dsl.git
cd system-dsl

# 2. Crea el entorno virtual
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows

# 3. Instala las dependencias del compilador
pip install -r requirements.txt
```

### `requirements.txt` del compilador

```
antlr4-python3-runtime==4.13.1
jinja2>=3.1.0
```

---

## Uso rápido

```bash
# Genera todos los artefactos en output/
python main.py generate examples/incidencias.dsl \
  --db postgresql://admin:secret@db:5432/gestionincidencias

# Copia el fichero de variables de entorno
cp output/.env.example output/.env

# Levanta la API y la base de datos
cd output
docker compose up --build
```

Abre **http://localhost:8000/docs** para acceder a Swagger UI con todos los endpoints disponibles.

---

## Modos del compilador

El compilador expone tres comandos:

### `generate` — solo genera artefactos

```bash
python main.py generate <fichero.dsl> [opciones]
```

| Opción | Default | Descripción |
|---|---|---|
| `--output` | `output/` | Directorio de salida |
| `--db` | `postgresql://...` | URL de conexión SQLAlchemy |

### `serve` — solo levanta el servidor (desarrollo local)

```bash
python main.py serve [opciones]
```

Requiere que `generate` se haya ejecutado previamente y que PostgreSQL esté accesible.

| Opción | Default | Descripción |
|---|---|---|
| `--output` | `output/` | Directorio con los artefactos generados |
| `--host` | `127.0.0.1` | Host del servidor |
| `--port` | `8000` | Puerto del servidor |
| `--env` | `output/.env` | Ruta al fichero `.env` |
| `--reload` | `false` | Recarga automática al detectar cambios |

### `run` — genera y levanta en un paso

```bash
python main.py run <fichero.dsl> [opciones]
```

Acepta todas las opciones de `generate` y `serve` combinadas.

---

## Estructura del proyecto

```
system-dsl/
├── compiler/
│   ├── generator.py      # Orquesta los templates Jinja2
│   ├── metamodel.py      # Dataclasses del modelo intermedio
│   ├── validator.py      # Validación semántica del DSL
│   └── visitor.py        # Recorre el árbol ANTLR4 y construye el metamodelo
├── examples/
│   └── incidencias.dsl   # Ejemplo de dominio incluido
├── generated/            # Ficheros generados por ANTLR4 (no editar)
├── grammar/
│   └── SystemDSL.g4      # Gramática formal del lenguaje
├── templates/            # Templates Jinja2 por artefacto
│   ├── main.py.j2
│   ├── database.py.j2
│   ├── schema.sql.j2
│   ├── openapi.yaml.j2
│   ├── requirements.txt.j2
│   ├── .env.example.j2
│   ├── Dockerfile.j2
│   ├── docker-compose.yml.j2
│   ├── models/
│   │   ├── __init__.py.j2
│   │   ├── enums.py.j2
│   │   └── entity.py.j2
│   ├── routers/
│   │   ├── __init__.py.j2
│   │   └── entity.py.j2
│   └── tests/
│       ├── __init__.py.j2
│       └── test_api.py.j2
├── main.py               # Punto de entrada del compilador (CLI)
├── requirements.txt      # Dependencias del compilador
└── README.md
```

---

## Artefactos generados

Dado un fichero `.dsl`, el compilador produce la siguiente estructura en `output/`:

```
output/
├── main.py               # Arranque FastAPI con lifespan y routers
├── database.py           # Engine, sesión, get_db y normalize_row
├── schema.sql            # CREATE TABLE para todas las entidades
├── openapi.yaml          # Spec OpenAPI 3.0 completa
├── requirements.txt      # Dependencias de la API generada
├── .env.example          # Variables de entorno documentadas
├── Dockerfile            # Imagen de producción
├── docker-compose.yml    # API + PostgreSQL con healthcheck
├── models/
│   ├── __init__.py
│   ├── enums.py          # Enums Python de todos los enums del DSL
│   ├── usuario.py        # Modelos Pydantic: UsuarioBase, UsuarioCreate, Usuario
│   └── ...               # Un fichero por entidad
├── routers/
│   ├── __init__.py
│   ├── usuario.py        # GET, POST, PUT, DELETE /usuarios
│   └── ...               # Un router por entidad
└── tests/
    ├── __init__.py
    └── test_api.py       # Tests de integración autogenerados
```

---

## Despliegue con Docker

El `docker-compose.yml` generado incluye dos servicios:

- **api**: imagen Python 3.11 con FastAPI y uvicorn
- **db**: PostgreSQL 15 con el schema inicializado automáticamente

```bash
cd output

# Primera vez
cp .env.example .env          # ajusta las credenciales si es necesario
docker compose up --build

# Siguientes veces
docker compose up

# Limpiar volúmenes (resetea la BD)
docker compose down -v
```

---

## Regenerar el parser ANTLR4

Solo necesario si modificas `grammar/SystemDSL.g4`:

```bash
# Descarga el jar de ANTLR4 (una sola vez)
curl -o antlr-4.13.1-complete.jar \
  https://www.antlr.org/download/antlr-4.13.1-complete.jar

# Regenera el parser
java -jar antlr-4.13.1-complete.jar \
  -Dlanguage=Python3 -visitor -o generated/ grammar/SystemDSL.g4
```

---

## Tests

Los tests de integración atacan la API ya levantada. 

```bash
# Instala dependencias de test
pip install pytest httpx

# Levanta la API primero
cd output && docker compose up -d 

# Ejecuta los tests
pytest tests/test_api.py -v
```

Cada ejecución usa un sufijo de timestamp en los datos de prueba para evitar colisiones con datos existentes en la BD.

---

## `.gitignore` recomendado

```
antlr-4.13.1-complete.jar
generated/
output/
*.db
__pycache__/
.venv/
.env
```
