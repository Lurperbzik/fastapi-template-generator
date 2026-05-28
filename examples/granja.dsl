system: GestionGranjas
version: "1.0"

enums {

    enum TipoCultivo {
        values: [TRIGO, MAIZ, ARROZ, TOMATE, PATATA]
    }

    enum EstadoAnimal {
        values: [SANO, ENFERMO, CUARENTENA]
    }

    enum Rol {
        values: [ADMIN, TRABAJADOR, VETERINARIO]
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
                default: TRABAJADOR
            }
        }
    }

    entity Granja {
        fields {
            field nombre {
                type: String
                required: true
            }
            field ubicacion {
                type: String
                required: true
            }
        }
    }

    entity Cultivo {
        fields {
            field tipo {
                type: TipoCultivo
                required: true
            }
            field hectareas {
                type: Float
                required: true
                min: 0
            }
            field fechaSiembra {
                type: DateTime
                default: now()
            }
        }
    }

    entity Animal {
        fields {
            field especie {
                type: String
                required: true
            }
            field estado {
                type: EstadoAnimal
                default: SANO
            }
            field edad {
                type: Integer
                min: 0
            }
        }
    }

}

relations {

    relation {
        from: Cultivo
        to: Granja
        type: many-to-one
        role: granja
        required: true
    }

    relation {
        from: Animal
        to: Granja
        type: many-to-one
        role: granja
        required: true
    }

    relation {
        from: Granja
        to: Usuario
        type: many-to-one
        role: responsable
        required: true
    }

}