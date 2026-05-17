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
