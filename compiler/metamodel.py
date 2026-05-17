from dataclasses import dataclass, field
from typing import Optional

@dataclass
class FieldDef:
    name: str
    type: str
    required: bool = False
    unique: bool = False
    default: Optional[str] = None
    min: Optional[float] = None
    max: Optional[float] = None

@dataclass
class EntityDef:
    name: str
    fields: list[FieldDef] = field(default_factory=list)

@dataclass
class EnumDef:
    name: str
    values: list[str] = field(default_factory=list)

@dataclass
class RelationDef:
    from_entity: str
    to_entity: str
    type: str
    role: Optional[str] = None
    required: bool = False


@dataclass
class SystemModel:
    name: str
    version: str
    enums: list[EnumDef] = field(default_factory=list)
    entities: list[EntityDef] = field(default_factory=list)
    relations: list[RelationDef] = field(default_factory=list)
