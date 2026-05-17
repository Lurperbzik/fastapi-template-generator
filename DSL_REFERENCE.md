# SystemDSL — Referencia del lenguaje

SystemDSL es un lenguaje específico de dominio (DSL) para describir sistemas de información. A partir de un fichero `.dsl` el compilador genera automáticamente la base de datos, la API REST y la documentación del sistema.

---

## Estructura de un fichero `.dsl`

Un fichero `.dsl` tiene siempre esta estructura y en este orden:

```
system: <nombre>
version: "<versión>"

enums { ... }

entities { ... }

relations { ... }

rules { ... }
```

Todas las secciones son obligatorias aunque pueden estar vacías (`enums {}`, `relations {}`, `rules {}`).

---

## Cabecera

Define el nombre y la versión del sistema. Ambos campos son obligatorios.

```
system: GestionIncidencias
version: "1.0"
```

| Campo | Tipo | Descripción |
|---|---|---|
| `system` | Identificador | Nombre del sistema. Se usa como nombre de la BD y título de la API. |
| `version` | String entre comillas | Versión del sistema. Aparece en la spec OpenAPI. |

---

## Sección `enums`

Define los tipos enumerados que pueden usarse como tipo de campo en las entidades.

```
enums {

    enum Estado {
        values: [ABIERTO, EN_PROGRESO, RESUELTO, CERRADO]
    }

    enum Prioridad {
        values: [BAJA, MEDIA, ALTA, CRITICA]
    }

}
```

### Sintaxis

```
enum <Nombre> {
    values: [VALOR1, VALOR2, ...]
}
```

### Reglas

- El nombre del enum debe empezar por mayúscula.
- Debe tener al menos un valor.
- Los valores no pueden repetirse dentro del mismo enum.
- Los nombres de enum no pueden repetirse en el fichero.
- Los valores se generan como `str` Enum en Python y como constraint `CHECK` en PostgreSQL.

---

## Sección `entities`

Define las entidades del dominio. Cada entidad se convierte en una tabla SQL y en un conjunto de modelos Pydantic con su router CRUD.

```
entities {

    entity Usuario {
        fields {
            field nombre {
                type: String
                required: true
            }
            field email {
                type: String
                required: true
                unique: true
            }
            field rol {
                type: Rol
                default: USUARIO
            }
        }
    }

}
```

### Sintaxis de entidad

```
entity <Nombre> {
    fields {
        field <nombre_campo> {
            <propiedades>
        }
        ...
    }
}
```

### Propiedades de un campo

| Propiedad | Valores | Obligatoria | Descripción |
|---|---|---|---|
| `type` | Ver tipos | Sí | Tipo del campo |
| `required` | `true` / `false` | No | Si es obligatorio. Default: `false` |
| `unique` | `true` / `false` | No | Si debe ser único en la tabla. Default: `false` |
| `default` | Depende del tipo | No | Valor por defecto |
| `min` | Número | No | Valor mínimo (numéricos) o longitud mínima (String) |
| `max` | Número | No | Valor máximo (numéricos) o longitud máxima (String) |

### Tipos de campo

| Tipo DSL | Tipo Python | Tipo PostgreSQL | Notas |
|---|---|---|---|
| `String` | `str` | `TEXT` | Admite `min`, `max` |
| `Integer` | `int` | `INTEGER` | Admite `min`, `max` |
| `Float` | `float` | `FLOAT` | Admite `min`, `max` |
| `Boolean` | `bool` | `BOOLEAN` | Default: `true` o `false` |
| `DateTime` | `datetime` | `TIMESTAMP` | Default especial: `now()` |
| `<NombreEnum>` | `str` (Enum) | `TEXT` + `CHECK` | Referencia a un enum declarado |

### Valores de `default`

| Tipo | Ejemplo de default | Notas |
|---|---|---|
| `String` | `default: "activo"` | Entre comillas |
| `Integer` | `default: 0` | Valor numérico |
| `Float` | `default: 0.0` | Valor decimal |
| `Boolean` | `default: false` | `true` o `false` |
| `DateTime` | `default: now()` | Inserta la fecha/hora actual |
| Enum | `default: ABIERTO` | Debe ser un valor válido del enum |

### Reglas de validación semántica

- `type` es obligatorio en todos los campos.
- El tipo referenciado debe existir como primitivo o como enum declarado.
- `min` y `max` solo son aplicables a `String`, `Integer` y `Float`.
- Si `min` y `max` están ambos presentes, `min` debe ser menor o igual que `max`.
- `default: now()` solo es válido para campos de tipo `DateTime`.
- El valor de `default` en un campo de tipo enum debe ser uno de los valores declarados en ese enum.
- No pueden existir dos campos con el mismo nombre en la misma entidad.
- No pueden existir dos entidades con el mismo nombre.

---

## Sección `relations`

Define las relaciones entre entidades. Cada relación con tipo `many-to-one` u `one-to-one` genera una columna de clave foránea en la tabla de la entidad origen.

```
relations {

    relation {
        from: Ticket
        to: Usuario
        type: many-to-one
        role: creadoPor
        required: true
    }

    relation {
        from: Ticket
        to: Usuario
        type: many-to-one
        role: asignadoA
    }

}
```

### Propiedades de una relación

| Propiedad | Valores | Obligatoria | Descripción |
|---|---|---|---|
| `from` | Nombre de entidad | Sí | Entidad origen (la que tiene la FK) |
| `to` | Nombre de entidad | Sí | Entidad destino |
| `type` | Ver cardinalidades | Sí | Cardinalidad de la relación |
| `role` | Identificador | Recomendado | Nombre semántico de la relación. Se usa como nombre de la columna FK |
| `required` | `true` / `false` | No | Si la FK puede ser nula. Default: `false` |

### Cardinalidades soportadas

| Tipo | Columna generada | Notas |
|---|---|---|
| `many-to-one` | FK en tabla `from` | La más común. Varios registros apuntan a uno. |
| `one-to-one` | FK en tabla `from` | Un registro apunta a exactamente uno. |
| `one-to-many` | Sin columna FK | La FK reside en la otra entidad. Define la relación inversa. |
| `many-to-many` | Sin columna FK | No genera tabla intermedia en v1.0. |

### Reglas del `role`

El `role` es obligatorio cuando existen dos o más relaciones entre el mismo par de entidades. Sin `role`, el compilador no puede distinguir los nombres de las columnas FK y lanzará un error semántico.

```
# CORRECTO: dos relaciones entre Ticket y Usuario con roles distintos
relation {
    from: Ticket
    to: Usuario
    type: many-to-one
    role: creadoPor
}

relation {
    from: Ticket
    to: Usuario
    type: many-to-one
    role: asignadoA
}
```

```
# INCORRECTO: dos relaciones sin role
relation {
    from: Ticket
    to: Usuario
    type: many-to-one
}

relation {
    from: Ticket
    to: Usuario
    type: many-to-one
}
```

### Nombre de la columna FK generada

La columna FK se nombra `<role>_id` en minúsculas. Ejemplos:

| `role` | Columna generada |
|---|---|
| `creadoPor` | `creadopor_id` |
| `asignadoA` | `asignadoa_id` |
| `autor` | `autor_id` |
| `ticket` | `ticket_id` |

---

## Sección `rules`

Define reglas de negocio asociadas a entidades. En v1.0 se almacenan como metadatos del modelo y se incluyen como comentarios en el código generado.

```
rules {

    rule {
        entity: Ticket
        rule: "fechaCierre must be null when estado != RESUELTO and estado != CERRADO"
    }

    rule {
        entity: Ticket
        rule: "asignadoA must not be null when estado == EN_PROGRESO"
    }

}
```

### Propiedades de una regla

| Propiedad | Tipo | Obligatoria | Descripción |
|---|---|---|---|
| `entity` | Nombre de entidad | Sí | Entidad a la que aplica la regla |
| `rule` | String entre comillas | Sí | Descripción de la regla en lenguaje natural estructurado |

### Reglas de validación semántica

- La entidad referenciada debe existir en la sección `entities`.
- El texto de la regla no puede estar vacío.

---

## Ejemplo completo

```
system: GestionIncidencias
version: "1.0"

enums {

    enum Estado {
        values: [ABIERTO, EN_PROGRESO, RESUELTO, CERRADO]
    }

    enum Prioridad {
        values: [BAJA, MEDIA, ALTA, CRITICA]
    }

    enum Rol {
        values: [ADMIN, AGENTE, USUARIO]
    }

}

entities {

    entity Usuario {
        fields {
            field nombre {
                type: String
                required: true
            }
            field email {
                type: String
                required: true
                unique: true
            }
            field rol {
                type: Rol
                default: USUARIO
            }
        }
    }

    entity Ticket {
        fields {
            field titulo {
                type: String
                required: true
                max: 200
            }
            field descripcion {
                type: String
            }
            field estado {
                type: Estado
                default: ABIERTO
            }
            field prioridad {
                type: Prioridad
                default: MEDIA
            }
            field fechaCreacion {
                type: DateTime
                default: now()
            }
            field fechaCierre {
                type: DateTime
            }
        }
    }

    entity Comentario {
        fields {
            field texto {
                type: String
                required: true
                max: 1000
            }
            field fechaCreacion {
                type: DateTime
                default: now()
            }
        }
    }

}

relations {

    relation {
        from: Ticket
        to: Usuario
        type: many-to-one
        role: creadoPor
        required: true
    }

    relation {
        from: Ticket
        to: Usuario
        type: many-to-one
        role: asignadoA
    }

    relation {
        from: Comentario
        to: Ticket
        type: many-to-one
        role: ticket
        required: true
    }

    relation {
        from: Comentario
        to: Usuario
        type: many-to-one
        role: autor
        required: true
    }

}

rules {

    rule {
        entity: Ticket
        rule: "fechaCierre must be null when estado != RESUELTO and estado != CERRADO"
    }

    rule {
        entity: Ticket
        rule: "asignadoA must not be null when estado == EN_PROGRESO"
    }

}
```

---

## Errores semánticos comunes

| Error | Causa | Solución |
|---|---|---|
| `Tipo desconocido 'X'` | El tipo no es primitivo ni enum declarado | Declara el enum o corrige el nombre del tipo |
| `Default 'X' no es un valor válido del enum 'Y'` | El valor no existe en ese enum | Usa un valor de la lista `values` del enum |
| `'max' no aplicable al tipo 'DateTime'` | `min`/`max` en un tipo no numérico ni String | Elimina la constraint o cambia el tipo |
| `Relaciones múltiples entre 'A' y 'B' requieren 'role'` | Dos relaciones entre el mismo par sin `role` | Añade `role` en ambas relaciones |
| `Relación con 'from' desconocido: 'X'` | La entidad no está declarada | Declara la entidad o corrige el nombre |
| `Enum duplicado: 'X'` | Dos enums con el mismo nombre | Renombra uno de ellos |
| `Campo duplicado 'X' en entidad 'Y'` | Dos campos con el mismo nombre | Renombra uno de los campos |
