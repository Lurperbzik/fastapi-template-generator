from .metamodel import SystemModel

class SemanticError(Exception):
    pass

class SemanticValidator:

    def __init__(self, model: SystemModel):
        self.model       = model
        self.errors      = []
        self.enum_names  = {e.name for e in model.enums}
        self.entity_names = {e.name for e in model.entities}

        self.PRIMITIVE_TYPES = {
            "String", "Integer", "Float", "Boolean", "DateTime"
        }
        self.VALID_TYPES = self.PRIMITIVE_TYPES | self.enum_names

        self.NUMERIC_TYPES = {"Integer", "Float"}
        self.STRING_TYPES  = {"String"}

    # ─── Punto de entrada ─────────────────────────────────────

    def validate(self):
        self._validate_enums()
        self._validate_entities()
        self._validate_relations()

        if self.errors:
            msg = "\n".join(f"  - {e}" for e in self.errors)
            raise SemanticError(f"\nSemantic Error:\n{msg}")

    # ─── Enums ────────────────────────────────────────────────

    def _validate_enums(self):
        seen = set()
        for enum in self.model.enums:
            if enum.name in seen:
                self._error(f"Duplicated Enum: '{enum.name}'")
            seen.add(enum.name)

            if not enum.values:
                self._error(f"Enum '{enum.name}' has not defined values")

            seen_vals = set()
            for val in enum.values:
                if val in seen_vals:
                    self._error(
                        f"Duplicated value '{val}' on enum '{enum.name}'"
                    )
                seen_vals.add(val)

    # ─── Entidades ────────────────────────────────────────────

    def _validate_entities(self):
        seen = set()
        for entity in self.model.entities:
            if entity.name in seen:
                self._error(f"Duplicated entity: '{entity.name}'")
            seen.add(entity.name)

            if not entity.fields:
                self._error(
                    f"Entity '{entity.name}' has not defined fields"
                )

            self._validate_fields(entity)

    def _validate_fields(self, entity):
        seen = set()
        for f in entity.fields:
            if f.name in seen:
                self._error(
                    f"Duplicated field '{f.name}' on entity '{entity.name}'"
                )
            seen.add(f.name)

            # type obligatorio
            if not f.type:
                self._error(
                    f"Field '{f.name}' on '{entity.name}' has no type"
                )
                continue

            # type debe existir
            if f.type not in self.VALID_TYPES:
                self._error(
                    f"Unknown type '{f.type}' on "
                    f"'{entity.name}.{f.name}'"
                )

            # min/max solo en String, Integer y Float
            if f.min is not None and f.type not in (
                self.STRING_TYPES | self.NUMERIC_TYPES
            ):
                self._error(
                    f"'min' no aplicable to type '{f.type}' "
                    f"on '{entity.name}.{f.name}'"
                )
            if f.max is not None and f.type not in (
                self.STRING_TYPES | self.NUMERIC_TYPES
            ):
                self._error(
                    f"'max' no aplicable to type '{f.type}' "
                    f"on '{entity.name}.{f.name}'"
                )

            # min <= max si ambos presentes
            if f.min is not None and f.max is not None:
                if f.min > f.max:
                    self._error(
                        f"'min' ({f.min}) > 'max' ({f.max}) "
                        f"on '{entity.name}.{f.name}'"
                    )

            # default coherente con el tipo
            if f.default is not None:
                self._validate_default(entity.name, f)

    def _validate_default(self, entity_name, f):
        val = f.default

        # now() solo para DateTime
        if val == "now()":
            if f.type != "DateTime":
                self._error(
                    f"'now()' just valid for DateTime, "
                    f"no for '{f.type}' on '{entity_name}.{f.name}'"
                )
            return

        # Si el tipo es un enum, el default debe ser un valor del enum
        if f.type in self.enum_names:
            enum_def = next(
                e for e in self.model.enums if e.name == f.type
            )
            if val not in enum_def.values:
                self._error(
                    f"Default '{val}' is not valid on enum "
                    f"'{f.type}' on '{entity_name}.{f.name}'. "
                    f"Valid values: {enum_def.values}"
                )
            return

        # Tipos primitivos
        if f.type == "Boolean" and val not in ("true", "false"):
            self._error(
                f"Default '{val}' is not a valid Boolean "
                f"on '{entity_name}.{f.name}'"
            )
        elif f.type == "Integer":
            try:
                int(val)
            except ValueError:
                self._error(
                    f"Default '{val}' is not a valid Integer "
                    f"on '{entity_name}.{f.name}'"
                )
        elif f.type == "Float":
            try:
                float(val)
            except ValueError:
                self._error(
                    f"Default '{val}' is not a valid float "
                    f"on '{entity_name}.{f.name}'"
                )

    # ─── Relaciones ───────────────────────────────────────────

    def _validate_relations(self):
        for r in self.model.relations:
            if r.from_entity not in self.entity_names:
                self._error(
                    f"Relation with 'from' unknown: '{r.from_entity}'"
                )
            if r.to_entity not in self.entity_names:
                self._error(
                    f"Relation with 'to' unknown: '{r.to_entity}'"
                )

        # Detectar relaciones ambiguas: mismo from+to sin role
        seen = {}
        for r in self.model.relations:
            key = (r.from_entity, r.to_entity)
            if key in seen:
                if not r.role or not seen[key].role:
                    self._error(
                        f"Multiple relations between '{r.from_entity}' and "
                        f"'{r.to_entity}' required 'role' in both"
                    )
            seen[key] = r

    # ─── Utilidad ─────────────────────────────────────────────

    def _error(self, msg: str):
        self.errors.append(msg)
