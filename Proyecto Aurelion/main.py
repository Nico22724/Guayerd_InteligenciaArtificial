import re

contenido = "## "

def leer_contenido():
    """Lee todo el contenido del archivo Markdown."""
    with open("Documento.md", "r", encoding="utf-8") as archivo:
        return archivo.read()


def mostrar_menu():
    contenido = leer_contenido()
    secciones = re.findall(r"^## (.+)", contenido, re.MULTILINE)
    for i, sub in enumerate(secciones, start=1):
                    print(f"{i}. {sub}")

def mostrar_subtitulos(subtitulos, bloque):
    while True:
        print("\nConsulte el registro deseado")
        for i, sub in enumerate(subtitulos, start=1):
            print(f"{i}. {sub}")
        opcion_sub = int(input("\nSeleccione una opción o 0 para volver al menú principal: "))
        if opcion_sub == 0:
            break
        option_list(opcion_sub, subtitulos, bloque)
        input("\nPresione Enter para continuar...")
            

def mostrar_seccion(nombre):
    """Muestra el contenido de una sección ## (Tema, Problema, Solución)."""
    contenido = leer_contenido()
    secciones = re.findall(r"^## (.+)", contenido, re.MULTILINE)
    match = re.search(
    fr"## {re.escape(secciones[nombre - 1])}\n([\s\S]*?)(?=\n## |\Z)", 
    contenido
    )
    
    
    bloque = match.group(1).strip()
    subtitulos = re.findall(r"^### ([^\#].*)", bloque, re.MULTILINE)
    
    if not subtitulos:
        print(bloque)
    elif subtitulos:
        mostrar_subtitulos(subtitulos, bloque)
    else:
        print(f"No se encontró la sección {nombre}.")


def option_list(num_list, subtitulos, bloque):
    # num_list ya es la opción del usuario (empieza en 1)
    titulo = subtitulos[num_list - 1]  # ajustamos al índice correcto
    # construimos regex dinámicamente
    pattern = fr"### {re.escape(titulo)}\n([\s\S]*?)(?=\n### |\Z)"
    
    match_tabla = re.search(pattern, bloque)
    if match_tabla:
        print(f"\nContenido de '{titulo}':\n")
        print(match_tabla.group(1).strip())
    else:
        print("No se encontró contenido para ese subtítulo.")


print("Bienvenido al Proyecto Aurelion")

while True:
    print("\nMenú de opciones:")
    mostrar_menu()

    opcion = int(input("Seleccione una opción (1-4) o '0' para terminar: "))
    
    if opcion == 0:
        break
  
    mostrar_seccion(opcion)
    input("\nPresione Enter para volver al menú...")