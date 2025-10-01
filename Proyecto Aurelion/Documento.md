# Proyecto Tienda Aurelion

---

## Tema
#### Control eficaz del inventario

---

## Problema
#### Stock excedente de los productos menos vendidos

El exceso de inventario en productos de baja rotación genera costos ocultos:  
almacenamiento, deterioro, obsolescencia y capital inmovilizado. Además, puede deteriorar el flujo de caja y reducir la capacidad para invertir en productos de mayor demanda.

**Consecuencias:**
- Costos de almacenamiento y manejo
- Pérdida por obsolescencia o caducidad
- Capital inmovilizado que podría usarse en artículos de alta rotación
- Riesgo de descuentos frecuentes que reducen margen

---

## Solución
#### Identificar los productos menos vendidos y maximizar el correcto abastecimiento

La solución combina análisis de datos para identificar baja rotación y políticas de abastecimiento que eviten acumulación y aseguren disponibilidad de los productos con mayor demanda.

## Estructura de registros de información

---

### 📌 Clientes
| Registro    | Tipo   | Escala    |
|-------------|--------|-----------|
| Id_cliente  | Numérico | Razón    |
| Nombre      | Texto  | Nominal   |
| Email       | Texto  | Nominal   |
| Ciudad      | Texto  | Nominal   |
| Fecha_alta  | Texto  | Intervalo |

---

### 📌 Detalle_ventas
| Registro        | Tipo   | Escala    |
|-----------------|--------|-----------|
| Id_venta        | Numérico | Razón    |
| Id_producto     | Numérico | Razón    |
| Nombre_producto | Texto  | Nominal   |
| Cantidad        | Numérico | Razón    |
| Precio_unitario | Numérico | Razón    |
| Importe         | Numérico | Razón    |

---

### 📌 Productos
| Registro        | Tipo   | Escala    |
|-----------------|--------|-----------|
| Id_producto     | Numérico | Razón    |
| Nombre_producto | Texto  | Nominal   |
| Categoria       | Texto  | Nominal   |
| Precio_unitario | Numérico | Razón    |

---

### 📌 Ventas
| Registro       | Tipo   | Escala    |
|----------------|--------|-----------|
| Id_venta       | Numérico | Razón    |
| Fecha          | Texto  | Intervalo |
| Id_cliente     | Numérico | Razón    |
| Nombre_cliente | Texto  | Nominal   |
| Email          | Texto  | Nominal   |
| Medio_pago     | Texto  | Nominal   |
