import argparse
import os
import sys
import subprocess
import shutil

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from generated.grammar.SystemDSLLexer import SystemDSLLexer
from generated.grammar.SystemDSLParser import SystemDSLParser
from compiler.visitor import ModelBuilder
from compiler.validator import SemanticValidator, SemanticError
from compiler.generator import Generator

class StrictErrorListener(ErrorListener):

      def syntaxError(self, recognizer, offendingSymbol,
                    line, column, msg, e):

        token = offendingSymbol.text if offendingSymbol else "<EOF>"

        raise SyntaxError(
            f"\tLine {line}:{column}\n"
            f"\tToken: {token}\n"
            f"\tMessage: {msg}"
        )
      
def parse_dsl(filepath: str):
    if not os.path.exists(filepath):
        print(f"Error: file '{filepath}' not found.")
        sys.exit(1)

    input_stream = FileStream(filepath, encoding="utf-8")

    lexer = SystemDSLLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(StrictErrorListener())

    tokens = CommonTokenStream(lexer)

    parser = SystemDSLParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(StrictErrorListener())

    try:
        tree = parser.model()
        model = ModelBuilder().visit(tree)
        SemanticValidator(model).validate()
        return model

    except SyntaxError as e:
        print(f"Syntax Error:\n{e}")
        sys.exit(1)

    except SemanticError as e:
        print(f"\nSemantic Error:\n  {e}")
        sys.exit(1)

    except Exception as e:
        print(f"\nInternal Error:\n  {e}")
        sys.exit(1)

def cmd_generate(args):
    if not args.db.startswith("postgresql://"):
        print("Error: just PostgreSQL supported.")
        print("Format: postgresql://user:password@host:5432/dbname")
        sys.exit(1)
    print(f"Compiling '{args.dsl}'...")
    model = parse_dsl(args.dsl)

    # limpiar output previo
    if os.path.exists(args.output):
        print(f"Cleaning directory '{args.output}'...")
        shutil.rmtree(args.output)

    # recrear directorio vacío
    os.makedirs(args.output, exist_ok=True)
    Generator(
        model,
        output_dir=args.output,
        db_url=args.db
    ).generate_all()
    print("\System successfully generated.")
    print(f"Copy 'output/.env.example' to 'output/.env' and change values.")


def cmd_serve(args):
    output_dir = args.output
    main_py    = os.path.join(output_dir, "main.py")

    if not os.path.exists(main_py):
        print(f"Error: doesn't exists '{main_py}'.")
        print("Run first: python main.py generate <file.dsl>")
        sys.exit(1)

    # Cargar .env si se especifica
    env_file = args.env or os.path.join(output_dir, ".env")
    if os.path.exists(env_file):
        print(f"Loading variables from '{env_file}'...")
        _load_env(env_file)

    print(f"Running server on http://{args.host}:{args.port}")
    print(f"Swagger UI available on http://{args.host}:{args.port}/docs\n")

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
        description="SystemDSL compiler: generate and launch functional systems from models."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ─── generate ────────────────────────────────────────────
    gen = subparsers.add_parser(
        "generate",
        help="Compile the DSL and generate artifacts in output/"
    )
    gen.add_argument("dsl", help="Path to the .dsl file")
    gen.add_argument(
        "--output",
        default="output",
        help="Output directory (default: output/)"
    )
    gen.add_argument(
        "--db",
        default="sqlite:///./database.db",
        help="SQLAlchemy database URL"
    )
    gen.set_defaults(func=cmd_generate)

    # ─── serve ───────────────────────────────────────────────
    serve = subparsers.add_parser(
        "serve",
        help="Launch the generated system"
    )
    serve.add_argument(
        "--output",
        default="output",
        help="Directory containing generated artifacts (default: output/)"
    )
    serve.add_argument(
        "--host",
        default="127.0.0.1",
        help="Server host (default: 127.0.0.1)"
    )
    serve.add_argument(
        "--port",
        default=8000,
        type=int,
        help="Server port (default: 8000)"
    )
    serve.add_argument(
        "--env",
        default=None,
        help="Path to the .env file (default: output/.env)"
    )
    serve.add_argument(
        "--reload",
        action="store_true",
        help="Development mode with auto-reload"
    )
    serve.set_defaults(func=cmd_serve)

    # ─── run ─────────────────────────────────────────────────
    run = subparsers.add_parser(
        "run",
        help="Generate artifacts and launch the server in one step"
    )
    run.add_argument("dsl", help="Path to the .dsl file")
    run.add_argument(
        "--output",
        default="output",
        help="Output directory (default: output/)"
    )
    run.add_argument(
        "--db",
        default="sqlite:///./database.db",
        help="SQLAlchemy database URL"
    )
    run.add_argument(
        "--host",
        default="127.0.0.1",
        help="Server host (default: 127.0.0.1)"
    )
    run.add_argument(
        "--port",
        default=8000,
        type=int,
        help="Server port (default: 8000)"
    )
    run.add_argument(
        "--env",
        default=None,
        help="Path to the .env file"
    )
    run.add_argument(
        "--reload",
        action="store_true",
        help="Development mode with auto-reload"
    )
    run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()