
#importaciones
from modulos.datos_basicos import cargar_producto
from modulos.gestion_datos import agregar_producto, listar_productos, eliminar_producto
from modulos.validaciones import validar_int

# Menu interactivo

def mostrar_menu():
    
    #Se define variable para que sea el contador y designe el ID del producto
    id_producto = 1


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
        #Esta opcion llama a la función cargar_productos que pide los datos al usuario, luego mediante agregar_producto lo agrega el dict a la list  
        elif opcion == "1":
            producto = cargar_producto(id_producto)
            agregar_producto(producto)
            print("Producto agregado correctamente")
            id_producto += 1
        
        #Esta opción llama a la función listar_productos la cual muestra la lista de los productos
        elif opcion == "2":
            listar_productos()
        
        elif opcion =="3":
            print("Opción buscar producto ")

        #Esta opción llama a la función eliminar_producto la cual mediante el id usa el metodo .remove()
        elif opcion == "4":   
            id_eliminar = validar_int("Ingrese ID del producto a eliminar: ")
            eliminar_producto(id_eliminar)

        elif opcion == "5":
            print("Saliendo del sistema ...")
            break