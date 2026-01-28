# Menu interactivo

def mostrar_menu():
    while True: 
        print("--- Menú Principal ---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. buscar productos")
        print("4. Eliminar productos")
        print("5. Salir")


        opcion = input("Seleccione una opción: ")


        if opcion not in ["1","2","3","4","5"]:
            print("Opción inválida, intente nuevamente")
            continue

        elif opcion == "1":
            print("Opción agregar producto ")
        elif opcion == "2":
            print("Opción listar productos ")
        elif opcion =="3":
            print("Opción buscar producto ")
        elif opcion == "4":
            print("Opcion eliminar producto ")
        elif opcion == "5":
            print("Saliendo del sistema ...")
            break