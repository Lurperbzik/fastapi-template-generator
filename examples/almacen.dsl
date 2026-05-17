system: GestionAlmacen
version: "1.0"

enums {

    enum RolEmpleado {
        values: [ADMINISTRADOR, RESPONSABLE, OPERARIO]
    }

    enum EstadoPedido {
        values: [PENDIENTE, CONFIRMADO, EN_PREPARACION, ENVIADO, ENTREGADO, CANCELADO]
    }

    enum TipoMovimiento {
        values: [ENTRADA, SALIDA, DEVOLUCION, AJUSTE]
    }

    enum CategoriaProducto {
        values: [ELECTRONICA, ALIMENTACION, TEXTIL, FERRETERIA, OFICINA, OTRO]
    }

}

entities {

    entity Empleado {
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
                type: RolEmpleado
                default: OPERARIO
            }
            field activo {
                type: Boolean
                default: true
            }
        }
    }

    entity Producto {
        fields {
            field nombre {
                type: String
                required: true
            }
            field referencia {
                type: String
                required: true
                unique: true
            }
            field descripcion {
                type: String
            }
            field categoria {
                type: CategoriaProducto
                default: OTRO
            }
            field precioUnitario {
                type: Float
                required: true
                min: 0
            }
            field stockActual {
                type: Integer
                default: 0
                min: 0
            }
            field stockMinimo {
                type: Integer
                default: 0
                min: 0
            }
        }
    }

    entity Proveedor {
        fields {
            field nombre {
                type: String
                required: true
            }
            field email {
                type: String
                unique: true
            }
            field telefono {
                type: String
            }
            field direccion {
                type: String
            }
        }
    }

    entity Pedido {
        fields {
            field numeroPedido {
                type: String
                required: true
                unique: true
            }
            field estado {
                type: EstadoPedido
                default: PENDIENTE
            }
            field fechaPedido {
                type: DateTime
                default: now()
            }
            field fechaEntregaEsperada {
                type: DateTime
            }
            field fechaEntregaReal {
                type: DateTime
            }
            field observaciones {
                type: String
                max: 500
            }
        }
    }

    entity LineaPedido {
        fields {
            field cantidad {
                type: Integer
                required: true
                min: 1
            }
            field precioUnitario {
                type: Float
                required: true
                min: 0
            }
        }
    }

    entity MovimientoStock {
        fields {
            field tipo {
                type: TipoMovimiento
                required: true
            }
            field cantidad {
                type: Integer
                required: true
                min: 1
            }
            field fecha {
                type: DateTime
                default: now()
            }
            field motivo {
                type: String
                max: 300
            }
        }
    }

}

relations {

    relation {
        from: Pedido
        to: Proveedor
        type: many-to-one
        role: proveedor
        required: true
    }

    relation {
        from: Pedido
        to: Empleado
        type: many-to-one
        role: creadoPor
        required: true
    }

    relation {
        from: Pedido
        to: Empleado
        type: many-to-one
        role: gestionadoPor
    }

    relation {
        from: LineaPedido
        to: Pedido
        type: many-to-one
        role: pedido
        required: true
    }

    relation {
        from: LineaPedido
        to: Producto
        type: many-to-one
        role: producto
        required: true
    }

    relation {
        from: MovimientoStock
        to: Producto
        type: many-to-one
        role: producto
        required: true
    }

    relation {
        from: MovimientoStock
        to: Empleado
        type: many-to-one
        role: registradoPor
        required: true
    }

    relation {
        from: MovimientoStock
        to: Pedido
        type: many-to-one
        role: pedidoOrigen
    }

}

rules {

    rule {
        entity: Pedido
        rule: "fechaEntregaReal must be null when estado != ENTREGADO"
    }

    rule {
        entity: Pedido
        rule: "gestionadoPor must not be null when estado == EN_PREPARACION or estado == ENVIADO"
    }

    rule {
        entity: Producto
        rule: "stockActual must be greater than or equal to 0"
    }

    rule {
        entity: LineaPedido
        rule: "cantidad must be greater than 0"
    }

    rule {
        entity: MovimientoStock
        rule: "pedidoOrigen must not be null when tipo == ENTRADA"
    }

}