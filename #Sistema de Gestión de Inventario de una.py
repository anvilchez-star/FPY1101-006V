#Sistema de Gestión de Inventario de una Librería

inventario = []

def Registrar_libro():
    codigo = input("Ingrese codigo de libro: ")
    
    for libro in inventario:
        if libro ["codigo"] == codigo:
            print("Codigo ya existe!!")
            return
    titulo = input("Ingrese titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")

    try:
        cantidad = int (input("Ingrese cantidad: "))
        precio = float (input("Ingrese precio: "))
    except ValueError:
        print("Error: debe ingresar valores numericos.")
        return
    
    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(libro)
    print("Libro registrado correctamente.")

def Buscar_libro():
    codigo = input("Ingrese codigo a buscar: ")

    for libro in inventario:
        if libro["codigo"] == codigo:
            print("\n=== Libro Encontrado ===")
            print("Codigo: ",libro["codigo"])
            print("Titulo: ",libro["titulo"])
            print("Autor: ",libro["autor"])
            print("Cantidad: ",libro["cantidad"])
            print("Precio: ",libro["precio"])
            return
    print("Codigo no encontrado.")

def Actualizar_stock():
    codigo = input("Ingrese codigo de libro al que se desea actualizar su stock: ")

    for libro in inventario:
        if libro["codigo"] == codigo:
            try:
                Nueva_cantidad = int (input("Ingrese el nuevo stock del libro: "))
                libro ["cantidad"] = Nueva_cantidad
                print("Stock actualizado correctamente.")
            except ValueError:
                print("Error: debe ingresar un valor numerico entero.")
            return
    print("Codigo no encontrado.")

def Mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return
    
    print("==== Inventario ====")
    for libro in inventario:
        print("-----------------------")        
        print("Codigo:   ", libro["codigo"])
        print("Titulo:   ", libro["titulo"])
        print("Autor:    ", libro["autor"])
        print("Cantidad: ", libro["cantidad"])
        print("Precio:   ", libro["precio"])
    print("-----------------------")


def Libro_mas_caro():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return
    
    Mas_caro = inventario[0]
    for libro in inventario:
        if libro ["precio"] > Mas_caro["precio"]:
            Mas_caro = libro
    
    print("\n=== Libro mas caro ===")
    print("Codigo:   ", Mas_caro["codigo"])
    print("Titulo:   ", Mas_caro["titulo"])
    print("Autor:    ", Mas_caro["autor"])
    print("Cantidad: ", Mas_caro["cantidad"])
    print("Precio:   ", Mas_caro["precio"])


def Eliminar_libro():
    codigo = input ("Ingrese el codigo del libro a eliminar: ")
    for libro in inventario:
        if libro ["codigo"] == codigo:
            inventario.remove(libro)
            print("Libro eliminado correctamente.")
            return
    print("Codigo no encontrado.")

def Valor_total_inventario():
    total = 0

    for libro in inventario:
        total = total + libro["cantidad"]*libro["precio"]
    print(f"Valor total del inventario es:{total}")


while True:
    print("\n===== LIBRERÍA =====")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Actualizar stock")
    print("4. Mostrar inventario")
    print("5. Mostrar libro más caro")
    print("6. Eliminar libro")
    print("7. Mostrar el valor total del inventario")
    print("8. Salir")

    try:
        opcion = int(input("Seleccione una opcion (1-8): "))
        if opcion == 1:
            Registrar_libro()
        elif opcion == 2:
            Buscar_libro()
        elif opcion == 3:
            Actualizar_stock()
        elif opcion == 4:
            Mostrar_inventario()
        elif opcion == 5:
            Libro_mas_caro()
        elif opcion == 6:
            Eliminar_libro()
        elif opcion == 7:
            Valor_total_inventario()
        elif opcion == 8:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, ingrese un numero entre 1 y 8.")
    except:
        print("Valor ingresado es invalido por favor ingresar un numero entero entre 1 y 8.")
