# Proyecto Tienda Aurelion

---
## Tema, Problema, Solucion
### Tema
#### Control eficaz del inventario

---

### Problema
#### Stock excedente de los productos menos vendidos

El exceso de inventario en productos de baja rotación genera costos ocultos:  
almacenamiento, deterioro, obsolescencia y capital inmovilizado. Además, puede deteriorar el flujo de caja y reducir la capacidad para invertir en productos de mayor demanda.

**Consecuencias:**
- Costos de almacenamiento y manejo
- Pérdida por obsolescencia o caducidad
- Capital inmovilizado que podría usarse en artículos de alta rotación
- Riesgo de descuentos frecuentes que reducen margen

---

### Solución
#### Identificar los productos menos vendidos y maximizar el correcto abastecimiento

La solución combina análisis de datos para identificar baja rotación y políticas de abastecimiento que eviten acumulación y aseguren disponibilidad de los productos con mayor demanda.

## Estructura de registros de información

---

### 📌 Clientes
| Registro    | Tipo     | Escala      | Definición |
|-------------|----------|-------------|------------|
| Id_cliente  | Numérico | Razón       | Identificador único del cliente |
| Nombre      | Texto    | Nominal     | Nombre completo del cliente |
| Email       | Texto    | Nominal     | Correo electrónico del cliente |
| Ciudad      | Texto    | Nominal     | Ciudad de residencia del cliente |
| Fecha_alta  | Texto    | Intervalo   | Fecha de registro del cliente |

---

### 📌 Detalle_ventas
| Registro        | Tipo     | Escala    | Definición |
|-----------------|----------|-----------|------------|
| Id_venta        | Numérico | Razón     | Identificador único de la venta |
| Id_producto     | Numérico | Razón     | Identificador único del producto vendido |
| Nombre_producto | Texto    | Nominal   | Nombre del producto vendido |
| Cantidad        | Numérico | Razón     | Número de unidades vendidas |
| Precio_unitario | Numérico | Razón     | Precio por unidad del producto |
| Importe         | Numérico | Razón     | Importe total de la línea de venta |

---

### 📌 Productos
| Registro        | Tipo     | Escala   | Definición |
|-----------------|----------|----------|------------|
| Id_producto     | Numérico | Razón    | Identificador único del producto |
| Nombre_producto | Texto    | Nominal  | Nombre del producto |
| Categoria       | Texto    | Nominal  | Categoría a la que pertenece el producto |
| Precio_unitario | Numérico | Razón    | Precio por unidad del producto |

---

### 📌 Ventas
| Registro       | Tipo     | Escala    | Definición |
|----------------|--------- |-----------|------------|
| Id_venta       | Numérico | Razón     | Identificador único de la venta |
| Fecha          | Texto    | Intervalo | Fecha en que se realizó la venta |
| Id_cliente     | Numérico | Razón     | Identificador único del cliente |
| Nombre_cliente | Texto    | Nominal   | Nombre completo del cliente |
| Email          | Texto    | Nominal   | Correo electrónico del cliente |
| Medio_pago     | Texto    | Nominal   | Forma de pago utilizada |

---

## Información, pasos, y pseudocódigo

---

### Información
El programa está desarrollado en Python y permite navegar por un archivo Markdown, mostrando secciones y subsecciones.

---

### Pasos

1. Leer el archivo Documento.md.

2. Extraer los títulos principales (##).

3. Mostrar menú principal con esas secciones.

4. Permitir navegar dentro de cada sección.

5. Validar entradas del usuario (solo valores numéricos dentro del rango válido).

6. Mostrar el contenido o los subtítulos según corresponda.

### Pseudocódigo
Inicio
  Mostrar menú principal con secciones (##)
  Mientras usuario no elija salir:
      Leer opción
      Si la sección tiene subtítulos (###):
          Mostrar lista de subtítulos
          Leer sub-opción
          Mostrar contenido correspondiente
      Sino:
          Mostrar contenido directo
Fin
## Diagrama

 ┌─────────────────────────┐
 │   Inicio del programa   │
 └───────────┬─────────────┘
             │
             ▼
 ┌─────────────────────────┐
 │  Mostrar mensaje        │
 │ "Bienvenido al Proyecto │
 │         Aurelion"       │
 └───────────┬─────────────┘
             │
             ▼
 ┌─────────────────────────┐
 │  Bucle Menú Principal   │◄─────────────┐
 └───────────┬─────────────┘              │
             │                            │
             ▼                            │
 ┌─────────────────────────┐              │
 │  Mostrar opciones del   │              │
 │    menú (leer ## )      │              │
 └───────────┬─────────────┘              │
             │                            │
             ▼                            │
 ┌─────────────────────────┐              │
 │ Ingresar opción (input) │              │
 └───────────┬─────────────┘              │
             │                            │
             ▼                            │
 ┌─────────────────────────┐              │
 │ Validar con             │              │
 │ value_correct()         │              │
 │ (¿numérico?)            │              │
 └───────────┬─────────────┘              │
        Sí   │    No                      │
             ▼                            │
     ┌───────────────┐       ┌─────────────────────────┐
     │ Guardar valor │       │ Error: "Debe ser número"│
     │ como 'opcion' │       │ volver a pedir          │
     └───────┬───────┘       └─────────────────────────┘
             │
             ▼
 ┌─────────────────────────┐
 │ ¿opcion == 0 ?          │
 └───────┬───────┬─────────┘
         │Sí      │No
         ▼        ▼
 ┌──────────────┐  ┌─────────────────────────┐
 │   Fin        │  │ mostrar_seccion(opcion) │
 │ (Salir loop) │  └───────────┬─────────────┘
 └──────────────┘              │
                               ▼
                 ┌─────────────────────────┐
                 │ Buscar sección ##       │
                 │ con regex en documento  │
                 └───────────┬─────────────┘
                             │
                             ▼
                 ┌─────────────────────────┐
                 │ ¿Tiene subtítulos ### ? │
                 └───────┬───────┬─────────┘
                         │Sí      │No
                         ▼        ▼
            ┌─────────────────┐   ┌─────────────────┐
            │ mostrar_subtit. │   │ Mostrar bloque  │
            │ (menú interno)  │   │ completo        │
            └───────┬─────────┘   └─────────────────┘
                    │
                    ▼
          ┌─────────────────────────┐
          │  Bucle Subtítulos       │◄───────────────┐
          └───────────┬─────────────┘                │
                      │                              │
                      ▼                              │
          ┌─────────────────────────┐                │
          │ Mostrar lista de ###    │                │
          │ y pedir opción          │                │
          └───────────┬─────────────┘                │
                      │                              │
                      ▼                              │
          ┌─────────────────────────┐                │
          │ Validar con index_corr. │                │
          │ (numérico y rango)      │                │
          └───────────┬─────────────┘                │
                      │                              │
                      ▼                              │
          ┌─────────────────────────┐                │
          │ ¿opcion_sub == 0 ?      │                │
          └───────┬───────┬─────────┘                │
                  │Sí      │No                        │
                  ▼        ▼                          │
          ┌──────────────┐  ┌───────────────────────┐ │
          │ Volver al    │  │ Llamar option_list()  │ │
          │ menú principal│ │ mostrar contenido ### │ │
          └──────────────┘  └───────────────────────┘ │
                                                      │
                                                      ▼
                                      ┌─────────────────────────┐
                                      │  Pausa (Enter)          │
                                      └───────────┬─────────────┘
                                                  │
                                                  ▼
                               (Regresa al menú principal)
