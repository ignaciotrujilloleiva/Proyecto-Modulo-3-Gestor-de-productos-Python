#Módulo encargado de la interacción con el usuario.
#Contiene el menú principal del sistema y gestiona las opciones seleccionadas por el usuario.

#importaciones
from modulos.datos_basicos import cargar_producto
from modulos.gestion_datos import agregar_producto, listar_productos, eliminar_producto, buscar_producto
from modulos.validaciones import validar_int
from modulos.funciones_utiles import mostrar_titulo

# Menu interactivo

def mostrar_menu():
    
    #Se define variable para que sea el contador y designe el ID del producto
    id_producto = 1


    while True: 
        #función del titulo
        mostrar_titulo("Menú Principal")

        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar productos")
        print("4. Eliminar productos")
        print("5. Salir")


        opcion = input("\nSeleccione una opción: ")


        if opcion not in ["1","2","3","4","5"]:
            print("\nOpción inválida, intente nuevamente")
            continue
        #Esta opcion llama a la función cargar_productos que pide los datos al usuario, luego mediante agregar_producto lo agrega el dict a la list  
        elif opcion == "1":
            producto = cargar_producto(id_producto)
            agregar_producto(producto)
            print("Producto agregado correctamente")
            id_producto += 1
        
        #Esta opción llama a la función listar_productos la cual muestra la lista de los productos
        elif opcion == "2":
            listar_productos()
        
        #Esta opción llama a la funcion buscar_producto la cual mediante el id busca el producto y lo muestra
        elif opcion =="3":
            id_buscar = validar_int("Ingrese ID del producto a buscar: ")
            buscar_producto(id_buscar)

        #Esta opción llama a la función eliminar_producto la cual mediante el id usa el metodo .remove()
        elif opcion == "4":   
            id_eliminar = validar_int("Ingrese ID del producto a eliminar: ")
            eliminar_producto(id_eliminar)

        #Esta opción llama el break permitiendo cerrar el bucle y salir del sistema
        elif opcion == "5":
            print("Saliendo del sistema ...")
            break