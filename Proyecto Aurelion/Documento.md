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
