import re

contenido = "## "

print("Bienvenido al Proyecto Aurelion")

while True:
    print("\nMenú de opciones:")
    print("1. Tema")
    print("2. Problema")
    print("3. Solución")
    print("4. Estructura de registros de información")
    
    opcion = int(input("Seleccione una opción (1-4) o '0' para terminar: "))
    
    if opcion == 0:
        break
    elif opcion == 1:
        while True:
            with open("Documento.md", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            # Buscar sección Clientes
            match = re.search(r"## Tema\n(.*?)(?=\n##|\Z)", contenido, re.S)
            if match:
                print(match.group(1).strip())
                
            print("\Ingrese 0 para ir al menu principal:")
            sub_opcion = input()
            if sub_opcion == '0':
                break
    elif opcion == 2:
        while True:
            with open("Documento.md", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            # Buscar sección Problema
            match = re.search(r"## Problema\n(.*?)(?=\n##|\Z)", contenido, re.S)
            if match:
                print(match.group(1).strip())
                
            print("\Ingrese 0 para ir al menu principal:")
            sub_opcion = input()
            if sub_opcion == '0':
                break
    elif opcion == 3:
        while True:
            with open("Documento.md", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            # Buscar sección Solución
            match = re.search(r"## Solución\n(.*?)(?=\n##|\Z)", contenido, re.S)
            if match:
                print(match.group(1).strip())
                
            print("\Ingrese 0 para ir al menu principal:")
            sub_opcion = input()
            if sub_opcion == '0':
                break
    elif opcion == 4:
        while True:
            with open("Documento.md", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            # Extraemos la sección "Estructura de registros de información" hasta el siguiente ##
            match_seccion = re.search(
                r"## Estructura de registros de información\n([\s\S]*?)(?=\n## |\Z)", 
                contenido
            )

            if match_seccion:
                bloque = match_seccion.group(1)  # contenido solo de esta sección
                bloque = bloque.strip()  # quitar saltos de línea y espacios al inicio

                # Extraemos solo los subtítulos (###) dentro de este bloque
                subtitulos = re.findall(r"### (.+)", bloque)

                print("Consulte el registro deseado")
                print("Opciones:")

                for i, sub in enumerate(subtitulos, start=1):
                    print(f"{i}. {sub}")
                    
            opcion_sub = int(input("\nSeleccione una opción o 0 para volver al menú principal: "))
            print()
            if opcion_sub == 0:
                break
            
            if opcion_sub == 1:
                while True:
                    match_tabla = re.search(
                        r"### 📌 Clientes\n([\s\S]*?)(?=\n### |\Z)", 
                        bloque
                    )
                    if match_tabla:
                        print(match_tabla.group(1).strip())
                    
                    print("\Ingrese 0 para ir al menu principal:")
                    sub_opcion = int(input())
                    if sub_opcion == 0:
                        break
            elif opcion_sub == 2:
                while True:
                    match_tabla = re.search(
                        r"### 📌 Detalle_ventas\n([\s\S]*?)(?=\n### |\Z)", 
                        bloque
                    )
                    if match_tabla:
                        print(match_tabla.group(1).strip())
                    
                    print("\Ingrese 0 para ir atras:")
                    sub_opcion = int(input())
                    if sub_opcion == 0:
                        break
            elif opcion_sub == 3:
                while True:
                    match_tabla = re.search(
                        r"### 📌 Productos\n([\s\S]*?)(?=\n### |\Z)", 
                        bloque
                    )
                    if match_tabla:
                        print(match_tabla.group(1).strip())
                    
                    print("\Ingrese 0 para ir atras:")
                    sub_opcion = int(input())
                    if sub_opcion == 0:
                        break
            elif opcion_sub == 4:
                while True:
                    match_tabla = re.search(
                        r"### 📌 Ventas\n([\s\S]*?)(?=\n### |\Z)", 
                        bloque
                    )
                    if match_tabla:
                        print(match_tabla.group(1).strip())
                    
                    print("\Ingrese 0 para ir atras:")
                    sub_opcion = int(input())
                    if sub_opcion == 0:
                        break            