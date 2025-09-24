# Estructura
### Registros de información

#### Clientes
- **Id_cliente** — type: numeric (PK)
- Nombre — type: text
- Email — type: text
- Ciudad — type: text
- Fecha_alta — type: text
- Relación: FK en *Ventas.Id_cliente*

#### Detalle_ventas
- **Id_venta** — type: numeric (PK)
- Id_producto — type: numeric (FK → Productos.Id_producto)
- Nombre_producto — type: text
- Cantidad — type: numeric
- Precio_unitario — type: numeric
- Importe — type: numeric
- Relación: FK en *Ventas.Id_venta*

#### Productos
- **Id_producto** — type: numeric (PK)
- Nombre_producto — type: text
- Categoria — type: text
- Precio_unitario — type: numeric

#### Ventas
- **Id_venta** — type: numeric (PK)
- Fecha — type: text
- Id_cliente — type: numeric (FK → Clientes.Id_cliente)
- Nombre_cliente — type: text
- Email — type: text
- Medio_pago — type: text
