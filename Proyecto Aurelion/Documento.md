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

### 📌 Inventario (FactInventory)
| Registro             | Tipo     | Escala    | Definición                                                                            |
|----------------------|----------|-----------|---------------------------------------------------------------------------------------|
| InventoryKey         | Texto    | Razón     | Identificador único del registro de inventario (clave primaria)                       |
| DateKey              | Fecha    | Intervalo | Fecha asociada al registro de inventario (formato YYYY-MM-DD)                         |
| StoreKey             | Texto    | Razón     | Identificador de la tienda/ubicación (clave foránea a dimensión Tienda)               |
| ProductKey           | Texto    | Razón     | Identificador del producto (clave foránea a dimensión Producto)                       |
| CurrencyKey          | Texto    | Nominal   | Identificador de la moneda utilizada para UnitCost (clave foránea a dimensión Moneda) |
| OnHandQuantity       | Numérico | Razón     | Cantidad disponible en stock en la tienda en la fecha indicada                        |
| OnOrderQuantity      | Numérico | Razón     | Cantidad pedida pero aún no recibida                                                  |
| SafetyStockQuantity  | Numérico | Razón     | Cantidad mínima de seguridad que se debe mantener en inventario                       |
| UnitCost             | Numérico | Razón     | Costo por unidad del producto en la moneda indicada (valor monetario)                 |
| DaysInStock          | Numérico | Razón     | Días acumulados que el producto ha permanecido en inventario                          |
| MinDayInStock        | Numérico | Razón     | Mínimo de días en inventario observado (período de agregación)                        |
| MaxDayInStock        | Numérico | Razón     | Máximo de días en inventario observado (período de agregación)                        |
| Aging                | Numérico | Ordinal   | Categoría/etapa de envejecimiento del inventario (bucket de antigüedad)               |

---

### 📌 Ventas en linea (FactOnlineSales)
| Registro                | Tipo     | Escala    | Definición                                                                        |
|-------------------------|----------|-----------|-----------------------------------------------------------------------------------|
| OnlineSalesKey          | Texto    | Razón     | Identificador único de la venta online (clave primaria)                           |
| DateKey                 | Fecha    | Intervalo | Fecha de la transacción (formato YYYY-MM-DD)                                      |
| StoreKey                | Texto    | Razón     | Identificador de la tienda/fulfillment (clave foránea a dimensión Tienda)         |
| ProductKey              | Texto    | Razón     | Identificador del producto (clave foránea a dimensión Producto)                   |
| PromotionKey            | Texto    | Razón     | Identificador de la promoción aplicada (clave foránea a dimensión Promoción)      |
| CurrencyKey             | Texto    | Nominal   | Identificador de la moneda usada en los montos (clave foránea a dimensión Moneda) |
| CustomerKey             | Texto    | Razón     | Identificador del cliente (clave foránea a dimensión Cliente)                     |
| SalesOrderLineNumber    | Numérico | Razón     | Número de línea dentro de la orden de venta (secuencia por orden)                 |
| SalesQuantity           | Numérico | Razón     | Cantidad vendida en la línea                                                      |
| SalesAmount             | Numérico | Razón     | Importe de la venta para la línea (valor monetario)                               |
| ReturnQuantity          | Numérico | Razón     | Cantidad devuelta correspondiente a la línea                                      |
| ReturnAmount            | Numérico | Razón     | Importe asociado a las devoluciones de la línea (valor monetario)                 |
| DiscountQuantity        | Numérico | Razón     | Cantidad de unidades a las que se aplicó descuento en la línea                    |
| DiscountAmount          | Numérico | Razón     | Importe total de descuento aplicado en la línea (valor monetario)                 |
| TotalCost               | Numérico | Razón     | Costo total asociado a la línea (valor monetario)                                 |
| UnitCost                | Numérico | Razón     | Costo por unidad del producto (valor monetario)                                   |
| UnitPrice               | Numérico | Razón     | Precio de venta por unidad (valor monetario)                                      |
| SalesOrderNumber        | Texto    | Nominal   | Identificador de la orden de venta (cadena/alfanumérico)                          |

---

### 📌 Ventas (FactSales)
| Registro            | Tipo     | Escala   | Definición                                                        |
|---------------------|----------|----------|-------------------------------------------------------------------|
| SalesKey            | Numérico | Razón    | Identificador único de la venta                                   |
| DateKey             | Fecha    | Ordinal  | Fecha de la venta                                                 |
| channelKey          | Numérico | Razón    | Identificador del canal de venta                                  |
| StoreKey            | Numérico | Razón    | Identificador único de la tienda                                  |
| ProductKey          | Numérico | Razón    | Identificador único del producto                                  |
| PromotionKey        | Numérico | Razón    | Identificador único de la promoción                               |
| CurrencyKey         | Numérico | Razón    | Identificador de la moneda utilizada                              |
| UnitCost            | Numérico | Intervalo| Costo unitario de los productos vendidos                          |
| UnitPrice           | Numérico | Intervalo| Precio unitario de los productos vendidos                         |
| SalesQuantity       | Numérico | Razón    | Cantidad de productos vendidos                                    |
| ReturnQuantity      | Numérico | Razón    | Cantidad de productos devueltos                                   |
| ReturnAmount        | Numérico | Razón    | Monto equivalente a los productos devueltos                       |
| DiscountQuantity    | Numérico | Razón    | Cantidad de productos en descuento                                |
| DiscountAmount      | Numérico | Intervalo| Monto equivalente al descuento aplicado                           |
| TotalCost           | Numérico | Razón    | Costo total de los productos vendidos                             |
| SalesAmount         | Numérico | Razón    | Monto total recaudado por la venta                                |


---

### 📌 Canal de venta (DimChannel)
| Registro            | Tipo     | Escala  | Definición                                          |
|---------------------|----------|---------|-----------------------------------------------------|
| ChannelKey          | Numérico | Razón   | Identificador único del canal (clave primaria)      |
| ChannelLabel        | Numérico | Razón   | Etiqueta numérica del canal                         |
| ChannelName         | Texto    | Nominal | Nombre del canal                                    |
| ChannelDescription  | Texto    | Nominal | Descripción del canal                               |


---

### 📌 Productos (DimProduct)
| Registro              | Tipo     | Escala   | Definición                                          |
|-----------------------|----------|----------|-----------------------------------------------------| 
| ProductKey            | Numérico | Razón    | Identificador único de cada producto                |
| ProductLabel          | Numérico | Razón    | Etiqueta numérica asociada al producto              |
| ProductName           | Texto    | Nominal  | Nombre del producto                                 |
| Manufacturer          | Texto    | Nominal  | Nombre del fabricante del producto                  |
| BrandName             | Texto    | Nominal  | Marca asociada al producto                          |
| ClassName             | Texto    | Nominal  | Clase o categoría del producto                      |
| ColorName             | Texto    | Nominal  | Nombre del color del producto                       |
| StockTypeName         | Texto    | Nominal  | Tipo de inventario al que pertenece                 |
| UnitCost              | Numérico | Intervalo| Costo unitario del producto                         |
| UnitPrice             | Numérico | Intervalo| Precio unitario de venta del producto               |
| AvailableForSaleDate  | Fecha    | Ordinal  | Fecha en que el producto está disponible a la venta |
| Status                | Texto    | Nominal  | Estado actual del producto                          |


---

### 📌 Tiendas (DimStore)
| Registro            | Tipo     | Escala   | Definición                                      |
|---------------------|----------|----------|-------------------------------------------------|
| StoreKey            | Numérico | Razón    | Identificador único de cada almacén             |
| GeographyKey        | Numérico | Razón    | Clave de ubicación geográfica asociada          |
| StoreManager        | Numérico | Razón    | Identificador del gerente del almacén           |
| StoreType           | Texto    | Nominal  | Tipo de almacén                                 |
| StoreName           | Texto    | Nominal  | Nombre del almacén                              |
| Status              | Texto    | Nominal  | Estado operativo del almacén                    |
| OpenDate            | Fecha    | Ordinal  | Fecha de apertura del almacén                   |
| CloseDate           | Fecha    | Ordinal  | Fecha de cierre del almacén (si aplica)         |
| EntityKey           | Numérico | Razón    | Identificador único de la entidad               |
| AddressLine1        | Texto    | Nominal  | Dirección principal del almacén                 |
| CloseReason         | Texto    | Nominal  | Razón del cierre del almacén (si aplica)        |
| EmployeeCount       | Numérico | Razón    | Cantidad de empleados en el almacén             |
| SellingAreaSize     | Numérico | Razón    | Tamaño del área de ventas del almacén           |


---

### 📌 Clientes (DimCustomer)
| Registro              | Tipo     | Escala   | Definición                                              |
|-----------------------|----------|----------|---------------------------------------------------------|
| CustomerKey           | Numérico | Razón    | Identificador único del cliente                         |
| GeographyKey          | Numérico | Razón    | Clave de ubicación geográfica asociada                  |
| CustomerLabel         | Numérico | Razón    | Etiqueta numérica asociada al cliente                   |
| FirstName             | Texto    | Nominal  | Nombre del cliente                                      |
| LastName              | Texto    | Nominal  | Apellido del cliente                                    |
| BirthDate             | Fecha    | Ordinal  | Fecha de nacimiento del cliente                         |
| MaritalStatus         | Texto    | Nominal  | Estado civil del cliente                                |
| Gender                | Texto    | Nominal  | Género del cliente                                      |
| EmailAddress          | Texto    | Nominal  | Dirección de correo electrónico del cliente             |
| YearlyIncome          | Numérico | Razón    | Ingreso anual del cliente                               |
| TotalChildren         | Numérico | Intervalo| Número total de hijos del cliente                       |
| NumberChildrenAtHome  | Numérico | Intervalo| Número de hijos viviendo en casa                        |
| Education             | Texto    | Nominal  | Nivel de educación del cliente                          |
| Occupation            | Texto    | Nominal  | Ocupación del cliente                                   |
| HouseOwnerFlag        | Numérico | Nominal  | Indicador de propiedad de vivienda (1: Propietario)     |
| NumberCarsOwned       | Numérico | Intervalo| Cantidad de autos que posee el cliente                  |
| AddressLine1          | Texto    | Nominal  | Dirección principal del cliente                         |
| Phone                 | Texto    | Nominal  | Número de teléfono del cliente                          |
| DateFirstPurchase     | Fecha    | Ordinal  | Fecha de la primera compra realizada por el cliente     |
| CustomerType          | Texto    | Nominal  | Tipo de cliente (ejemplo: Persona, Corporación, etc.)   |


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
                               
## Estadísticas descriptivas básicas calculadas
## Identificación del tipo de distribución de variables
## Análisis de correlaciones entre variables principales
### 📌 Monto de ventas --> Estado civil
<h4>Conclusión final sobre el estado marital de una persona en las ventas</h4>

Con base en los 100.000 registros analizados, Se aplicó una prueba t de Welch para comparar los montos de ventas entre clientes casados (M) y solteros (S). El resultado fue estadísticamente significativo (t = 10.91, p < 0.0001), indicando que existen diferencias claras entre ambos grupos. En promedio, los clientes casados presentan montos de 
venta mayores que los solteros. Aunque la variabilidad dentro de cada grupo es alta, la diferencia en medias es consistente y robusta.

### 📌 Monto de ventas --> Ocupación
<h4>Conclusión final sobre la influencia de la ocupacion de los clientes en las ventas </h4>

Con base en los 100.000 registros analizados, el test de Kruskal-Wallis arrojó H = 0.0 y p = 1.0, lo que indica que no existen diferencias significativas en los montos de ventas entre las distintas ocupaciones (Profesional, Manual, Clerical, etc.). Por lo tanto, no se encontró evidencia de que la ocupación del cliente influya en las ventas; cualquier diferencia observada es atribuible a la variabilidad natural de los datos.

### 📌 Monto de ventas --> Edad
<h4>Conclusión Final sobre la Influencia de la Edad en las Ventas </h4>

Con base en los 100.000 registros analizados: El análisis realizado mediante la prueba no paramétrica Kruskal–Wallis reveló diferencias estadísticamente significativas en los montos de ventas entre los distintos grupos de edad.<br> El estadístico obtenido (H = 81.55) y el valor p extremadamente pequeño (p = 9.90 × 10 - 17) indican que la probabilidad de que estas diferencias se deban al azar es prácticamente nula.<br>
En consecuencia, se rechaza la hipótesis nula y se concluye que: <br>

✔️ La edad del cliente influye de manera significativa en el nivel de gasto.<br>

Esto implica que: <br>

1. Los grupos de edad no presentan el mismo comportamiento de compra. <br>

2. Existen segmentos etarios con mayor propensión de gasto y otros con menor influencia en las ventas.<br>

3. El factor edad debe considerarse dentro de estrategias de marketing, segmentación de clientes y análisis de comportamiento de compra.<br>

### 📌 Monto de ventas --> Cuanto gana al año
<h4>Conclusión Final sobre la Influencia de lo que gana el Cliente en las Ventas </h4>

Con base en los 100.000 registros analizados: El análisis realizado mediante la prueba no paramétrica Kruskal–Wallis reveló diferencias estadísticamente significativas en los montos de ventas entre los distintos grupos de ingresos anuales. <br> El estadístico obtenido (H = 374.78) y el valor p es inexistente siendo este valor tan pequeño podemos decir que (p = 0) indican que la probabilidad de que estas diferencias se deban al azar es prácticamente nula.<br>
En consecuencia, se rechaza la hipótesis nula y se concluye que: <br>

✔️ Lo que gana el cliente influye de manera significativa en el nivel de gasto.<br>

Esto implica que: <br>

1. Los grupos de ingresos presentan diferencias marcadas en sus patrones de compra, lo que indica que el gasto no solo varía, sino que varía de forma consistente según el nivel económico del cliente.

2. Los clientes con mayores ingresos tienden a realizar compras de mayor valor, lo que sugiere una relación positiva entre capacidad adquisitiva y monto gastado.

3. El ingreso del cliente emerge como un predictor clave del comportamiento de compra, útil para modelos de segmentación, análisis de clientes o predicción de ventas.

4. Existen oportunidades para diseñar estrategias de marketing diferenciadas según el nivel de ingreso, como promociones personalizadas, productos premium o descuentos dirigidos.

5. La variación por nivel de ingreso es más significativa que otras variables analizadas, lo que resalta su importancia como una de las principales variables explicativas del monto de ventas.

### 📌 Monto de ventas --> Cuantos hijos tiene
<h4>Conclusión Final sobre la Influencia de cuantos hijos tiene el Cliente en las Ventas </h4>

Con base en los 100.000 registros analizados: Analizando la correlación de Spearman entre el número total de hijos y los montos de ventas fue muy baja (rho = 0.075), indicando una relación extremadamente débil. Aunque el valor p fue significativo (p < 0.0001), la magnitud del coeficiente revela que el número de hijos no influye de manera relevante en el nivel de ventas. En consecuencia, TotalChildren no es un predictor útil del comportamiento de compra.

### 📌 Monto de ventas --> Cual es su nivel educativo
<h4>Conclusión Final sobre la Influencia del Nivel Educativo del Cliente en las Ventas</h4>

Con base en los 100.000 registros analizados, la prueba no paramétrica de Kruskal–Wallis evidenció diferencias estadísticamente significativas entre los grupos de nivel educativo en relación con los montos de venta. El estadístico obtenido (H = 344.02) y el valor p extremadamente pequeño (p ≈ 3.42×10⁻⁷³) indican que la probabilidad de que estas diferencias sean producto del azar es prácticamente nula.

En consecuencia, se rechaza la hipótesis nula y se concluye que:

✔️ El nivel educativo del cliente influye significativamente en el monto de ventas.

Esto implica que:

1. Los distintos niveles educativos muestran comportamientos de compra distintos.

2. Algunos segmentos educativos presentan una mayor propensión al gasto, mientras que otros muestran un menor nivel de ventas.

3. La variable educación debe ser considerada en estrategias de segmentación, marketing y análisis del comportamiento del cliente, dado que está asociada a diferencias reales en el consumo.

### 📌 Conclusion Final 
🧾 Conclusión Final (Crítica) sobre el análisis de Kruskal–Wallis

Si bien la prueba Kruskal–Wallis arrojó diferencias estadísticamente significativas entre las distintas variables usadas en relación con los montos de ventas, es importante subrayar que estos resultados no deben interpretarse como evidencia definitiva de que influya de manera real, directa o relevante en el comportamiento de compra.

El valor p extremadamente pequeño indica que al menos dos grupos difieren. Sin embargo, este hallazgo debe tomarse con cautela por varias razones:

1. Significancia estadística no es igual a significancia práctica

    Con 100.000 registros, incluso diferencias mínimas pueden producir valores p muy pequeños.
    Esto puede llevar a conclusiones exageradas si no se evalúa:

    la magnitud del efecto,

    las medianas,

    los rangos intercuartiles,

    y la relevancia comercial real.

    Es posible que las diferencias observadas, aunque estadísticamente detectables, sean pequeñas o irrelevantes para la toma de decisiones del negocio.

2. El Kruskal–Wallis no identifica qué grupos difieren

    La prueba solo informa que "existe al menos una diferencia", pero no especifica entre por ejemplo qué niveles educativos ocurre ni cuán grandes son esas diferencias.
    Pruebas post-hoc como Dunn o Conover son esenciales para validar si los grupos realmente presentan comportamientos distintos. Sin ellas, el hallazgo queda incompleto.

3. No implica causalidad ni una relación natural

    El resultado no significa que exista una relación directa o innata.
    Es posible que otras variables altamente correlacionadas — como ejemplo ingresos, ocupación, tipo de productos adquiridos o número de hijos— sean las verdaderas responsables del patrón observado.

    Sin controlar estos factores, el hallazgo puede ser espurio o confuso.

4. Posible efecto de distribuciones no normales o presencia de outliers

    Los montos de ventas suelen tener distribuciones sesgadas con colas largas.
    Aunque Kruskal–Wallis es robusto a la no normalidad, las diferencias significativas pueden ser impulsadas por:

    valores extremos,

    grupos altamente desbalanceados,

    o diferencias en la dispersión más que en la tendencia central.

    Esto puede generar una falsa percepción de diferencia real entre los grupos.

5. Validación cruzada necesaria

    Para fortalecer o refutar el hallazgo, es recomendable:

    aplicar pruebas post-hoc,

    calcular tamaño del efecto (η² o ε²),

    ejecutar modelos multivariables,

    o repetir el análisis en subconjuntos mediante bootstrap o sampleo aleatorio.

    Solo con estas validaciones adicionales puede confirmarse si las diferencias son consistentes, robustas y relevantes en la práctica.

✔️ Conclusión General

Aunque el análisis Kruskal–Wallis indica diferencias estadísticamente significativas entre las diferentes analisis de correlaciones, estos resultados no deben interpretarse de forma aislada ni tomarse como evidencia firme de un patrón real en el comportamiento de compra.

La significancia estadística sugiere una señal, pero no confirma una relación fuerte, práctica ni causal.
El verdadero impacto debe evaluarse mediante análisis adicionales que podrían refutar, confirmar o matizar los hallazgos actuales.

## Detección de outliers (valores extremos)
## Graficos
## Interpretación de resultados