#Prueba n° 4 de Anthony Vilchez
print("\n                                                                    BIENVENIDO A NUESTRO SISTEMA DE GESTION DE PELICULAS!!!✌️💫           ")
nombre=input("Bienvenido, ingrese su nombre :") #profe le agregue esta parte , para que se vea mas bacano
print("Que tal! listo para organizar tus peliculas favoritas",nombre)
def mostrar_menu():
    print("\n********** MENU PRINCIPAL DEL CINE ******")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("*******************************************")

def leer_opcion():
    try:
        opcion = int(input("Seleccione una opción entre (1-6): "))
        return opcion
    except ValueError:
        return 0

def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True

def validar_duracion(duracion_str):
    try:
        duracion = int(duracion_str)
        if duracion > 0:
            return True
        return False
    except ValueError:
        return False

def validar_calificacion(califi_str):
    try:
        calificacion = float(califi_str)
        if 0.0 <= calificacion <= 10.0:
            return True
        return False
    except ValueError:
        return False

def agregar_pelicula(lista_peliculas):
    titulo = input("Ingrese el título de la película: ")
    duracion = input("Ingrese la duración (en minutos): ")
    calificacion = input("Ingrese la calificación (0.0 a 10.0): ")
    
    
    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío ni contener solo espacios")
        return
        
    if not validar_duracion(duracion):
        print("Error: la duración debe ser un número entero mayor que cero")
        return
        
    if not validar_calificacion(calificacion):
        print("Error: la calificación debe ser un número decimal entre 0.0 y 10.0")
        return
    
    nueva_pelicula = {
        "titulo": titulo.strip(),
        "duracion": int(duracion),
        "calificacion": float(calificacion),
        "disponible": False  
    }
    
    lista_peliculas.append(nueva_pelicula)
    print(f"¡Película '{titulo}' agregada exitosamente!")


def buscar_pelicula(lista_peliculas, titulo_buscar):
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]["titulo"].lower() == titulo_buscar.strip().lower():
            return i
    return -1


def eliminar_pelicula(lista_peliculas):
    titulo_eliminar = input("Ingrese el título de la película que desea eliminar: ")
    posicion = buscar_pelicula(lista_peliculas, titulo_eliminar)
    
    if posicion != -1:
        pelicula_eliminada = lista_peliculas.pop(posicion)
        print(f"La película '{pelicula_eliminada['titulo']}' ha sido eliminada correctamente")
    else:
        print(f"La película '{titulo_eliminar}' no se encuentra registrada")


def actualizar_disponibilidad(lista_peliculas):
    for pelicula in lista_peliculas:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False


def mostrar_peliculas(lista_peliculas):
    if len(lista_peliculas) == 0:
        print("\nNo hay películas registradas en el sistema actualmente")
        return

    actualizar_disponibilidad(lista_peliculas)
    
    print("\n=== LISTA DE PELICULAS ===")
    for pelicula in lista_peliculas:
        print(f"Título: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Calificación: {pelicula['calificacion']}")
        
        if pelicula["disponible"]:
            estado_texto = "DISPONIBLE"
        else:
            estado_texto = "NO RECOMENDADA"
            
        print(f"Estado: {estado_texto}")
        print("*" * 44)

def main():
    catalogo_cine = []
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_pelicula(catalogo_cine)
            
        elif opcion == 2:
            titulo_busqueda = input("Ingrese el título de la película a buscar: ")
            posicion = buscar_pelicula(catalogo_cine, titulo_busqueda)
            
            if posicion != -1:
                peli = catalogo_cine[posicion]
                print(f"\n[Película Encontrada en la posición {posicion}]")
                print(f"Título: {peli['titulo']}")
                print(f"Duración: {peli['duracion']} minutos")
                print(f"Calificación: {peli['calificacion']}")
                print(f"Estado Actual: {'DISPONIBLE' if peli['disponible'] else 'NO RECOMENDADA'}")
            else:
                print("Película no encontrada")
                
        elif opcion == 3:
            eliminar_pelicula(catalogo_cine)
            
        elif opcion == 4:
            actualizar_disponibilidad(catalogo_cine)
            print("Disponibilidad de todo el catálogo actualizada correctamente")
            
        elif opcion == 5:
            mostrar_peliculas(catalogo_cine)
            
        elif opcion == 6:
            print("\nGracias por usar el sistema, vuelva pronto")
            break
            
        else:
            print("Opción inválida, Intente ingresando un número del 1 al 6")

if __name__ == "__main__":
    main()