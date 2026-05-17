import argparse
import os
import sys
import subprocess

from antlr4 import FileStream, CommonTokenStream
from generated.SystemDSLLexer import SystemDSLLexer
from generated.SystemDSLParser import SystemDSLParser
from compiler.visitor import ModelBuilder
from compiler.validator import SemanticValidator, SemanticError
from compiler.generator import Generator


def parse_dsl(filepath: str):
    if not os.path.exists(filepath):
        print(f"Error: fichero '{filepath}' no encontrado.")
        sys.exit(1)

    input_stream = FileStream(filepath, encoding="utf-8")
    lexer        = SystemDSLLexer(input_stream)
    tokens       = CommonTokenStream(lexer)
    parser       = SystemDSLParser(tokens)
    tree         = parser.model()

    model = ModelBuilder().visit(tree)

    try:
        SemanticValidator(model).validate()
    except SemanticError as e:
        print(e)
        sys.exit(1)

    return model


def cmd_generate(args):
    if not args.db.startswith("postgresql://"):
        print("Error: solo se soporta PostgreSQL.")
        print("Formato: postgresql://user:password@host:5432/dbname")
        sys.exit(1)
    print(f"Compilando '{args.dsl}'...")
    model = parse_dsl(args.dsl)
    Generator(
        model,
        output_dir=args.output,
        db_url=args.db
    ).generate_all()
    print("\nSistema generado correctamente.")
    print(f"Copia 'output/.env.example' a 'output/.env' y ajusta las variables.")


def cmd_serve(args):
    output_dir = args.output
    main_py    = os.path.join(output_dir, "main.py")

    if not os.path.exists(main_py):
        print(f"Error: no existe '{main_py}'.")
        print("Ejecuta primero: python main.py generate <fichero.dsl>")
        sys.exit(1)

    # Cargar .env si se especifica
    env_file = args.env or os.path.join(output_dir, ".env")
    if os.path.exists(env_file):
        print(f"Cargando variables desde '{env_file}'...")
        _load_env(env_file)

    print(f"Arrancando servidor en http://{args.host}:{args.port}")
    print(f"Swagger UI disponible en http://{args.host}:{args.port}/docs\n")

    cmd = [
        sys.executable, "-m", "uvicorn",
        "main:app",
        "--host", args.host,
        "--port", str(args.port),
        "--app-dir", output_dir,
    ]
    if args.reload:
        cmd.append("--reload")

    subprocess.run(cmd)


def cmd_run(args):
    cmd_generate(args)
    print()
    cmd_serve(args)


def _load_env(filepath: str):
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())


def main():
    parser = argparse.ArgumentParser(
        prog="systemdsl",
        description="Compilador SystemDSL: genera y levanta sistemas funcionales desde modelos."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ─── generate ────────────────────────────────────────────
    gen = subparsers.add_parser(
        "generate",
        help="Compila el DSL y genera los artefactos en output/"
    )
    gen.add_argument("dsl",    help="Ruta al fichero .dsl")
    gen.add_argument("--output", default="output",
                     help="Directorio de salida (default: output/)")
    gen.add_argument("--db",   default="sqlite:///./database.db",
                     help="URL de base de datos SQLAlchemy")
    gen.set_defaults(func=cmd_generate)

    # ─── serve ───────────────────────────────────────────────
    serve = subparsers.add_parser(
        "serve",
        help="Levanta el sistema generado"
    )
    serve.add_argument("--output", default="output",
                       help="Directorio donde están los artefactos (default: output/)")
    serve.add_argument("--host",   default="127.0.0.1",
                       help="Host del servidor (default: 127.0.0.1)")
    serve.add_argument("--port",   default=8000, type=int,
                       help="Puerto del servidor (default: 8000)")
    serve.add_argument("--env",    default=None,
                       help="Ruta al fichero .env (default: output/.env)")
    serve.add_argument("--reload", action="store_true",
                       help="Modo desarrollo con recarga automática")
    serve.set_defaults(func=cmd_serve)

    # ─── run ─────────────────────────────────────────────────
    run = subparsers.add_parser(
        "run",
        help="Genera los artefactos y levanta el servidor en un paso"
    )
    run.add_argument("dsl",    help="Ruta al fichero .dsl")
    run.add_argument("--output", default="output",
                     help="Directorio de salida (default: output/)")
    run.add_argument("--db",   default="sqlite:///./database.db",
                     help="URL de base de datos SQLAlchemy")
    run.add_argument("--host", default="127.0.0.1",
                     help="Host del servidor (default: 127.0.0.1)")
    run.add_argument("--port", default=8000, type=int,
                     help="Puerto del servidor (default: 8000)")
    run.add_argument("--env",  default=None,
                     help="Ruta al fichero .env")
    run.add_argument("--reload", action="store_true",
                     help="Modo desarrollo con recarga automática")
    run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()