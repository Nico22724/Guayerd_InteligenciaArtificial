"""
Programa de lista de compras interactiva.

Este programa permite al usuario ingresar una cantidad fija de artículos con su precio.
- Solicita al usuario el nombre y precio de cada artículo.
- Guarda los artículos en un diccionario con el formato {nombre: precio}.
- Calcula el precio total de la compra sumando todos los valores.
- Determina cuál es el artículo con el precio más alto.
- Muestra la lista completa de artículos con sus precios, el total y el artículo más caro.
"""

# Número de artículos que se van a ingresar
num_items = 3
shopping_list = {}

# Ingreso de artículos y precios
for i in range(num_items):
    item = input(f"Ingrese el nombre del artículo {i + 1}: ")
    price = float(input(f"Ingrese el precio del artículo {i + 1}: "))
    shopping_list[item] = price
    
# Calcular precio total
price_total = sum(shopping_list.values())

# Determinar el artículo con mayor precio
item_max_price = max(shopping_list, key=shopping_list.get)

# Mostrar artículos y precios
for item, price in shopping_list.items():
    print(f"Artículo: {item}, Precio: {price}")

# Mostrar resultados finales
print(f"El precio total de la compra es: {price_total}")
print(f"El artículo con el precio más alto es: {item_max_price} con un precio de {shopping_list[item_max_price]}")
