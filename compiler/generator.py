from jinja2 import Environment, FileSystemLoader
from .metamodel import SystemModel
import os


def _pg_values(values: list) -> str:
    escaped = [v.replace("'", "''") for v in values]
    return ", ".join(f"'{v}'" for v in escaped)


class Generator:

    def __init__(
        self,
        model: SystemModel,
        output_dir: str = "output",
        db_url: str = "postgresql://admin:secret@db:5432/gestionincidencias"
    ):
        self.model      = model
        self.output_dir = output_dir
        self.db_url     = db_url
        self.enum_names = {e.name for e in model.enums}
        self.env        = Environment(
            loader=FileSystemLoader("templates"),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True
        )
        self.env.filters["pg_values"] = _pg_values
        os.makedirs(output_dir, exist_ok=True)

    def generate_all(self):
        # Ficheros raíz
        self._render("main.py.j2",            "main.py")
        self._render("database.py.j2",        "database.py")
        self._render("schema.sql.j2",         "schema.sql")
        self._render("openapi.yaml.j2",       "openapi.yaml")
        self._render("requirements.txt.j2",   "requirements.txt")
        self._render(".env.example.j2",       ".env.example")
        self._render("Dockerfile.j2",         "Dockerfile")
        self._render("docker-compose.yml.j2", "docker-compose.yml")

        # Subcarpeta models/
        self._render_to(
            "models/enums.py.j2",
            "models/enums.py"
        )
        self._render_to(
            "models/__init__.py.j2",
            "models/__init__.py"
        )
        for entity in self.model.entities:
            self._render_to(
                "models/entity.py.j2",
                f"models/{entity.name.lower()}.py",
                entity=entity
            )

        # Subcarpeta routers/
        self._render_to(
            "routers/__init__.py.j2",
            "routers/__init__.py"
        )
        for entity in self.model.entities:
            self._render_to(
                "routers/entity.py.j2",
                f"routers/{entity.name.lower()}.py",
                entity=entity
            )
        
        self._render_to(
            "tests/__init__.py.j2",
            "tests/__init__.py"
        )
        self._render_to(
            "tests/test_api.py.j2",
            "tests/test_api.py"
        )
        print(f"\nGenerados artefactos en '{self.output_dir}/'")

    def _render(self, template_name: str, output_name: str, **kwargs):
        self._render_to(template_name, output_name, **kwargs)

    def _render_to(self, template_name: str, output_name: str, **kwargs):
        template = self.env.get_template(template_name)
        content  = template.render(
            model=self.model,
            enum_names=self.enum_names,
            db_url=self.db_url,
            **kwargs
        )
        path = os.path.join(self.output_dir, output_name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  OK  {output_name}")