"""
Programa interactivo para calcular la edad y determinar mayoría de edad.

Este programa:
- Solicita al usuario su nombre y su año de nacimiento.
- Calcula la edad en base al año actual.
- Muestra el tipo de dato de la variable edad.
- Determina si el usuario es mayor de edad.
- Muestra un saludo personalizado indicando el nombre, la edad y si es mayor o menor de edad.
"""

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

# Año actual (puede reemplazarse por datetime para hacerlo automático)
año_actual = 2025

# Calcular edad
edad = año_actual - año_nacimiento

# Mostrar el tipo de dato
print("El tipo de dato de la edad es:", type(edad))

# Determinar si es mayor de edad (True o False)
is_older = edad >= 18   

# Mostrar saludo personalizado
print(f"Hola {nombre}, tienes {edad} años.")

# Mostrar si es mayor de edad
if is_older:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
