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

## Diagramacion de la base de datos y relaciones

![Diagrama de la base de datos](./ContosoDB.png)