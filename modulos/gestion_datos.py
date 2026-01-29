# Lección 4: Control de flujo y estructuras
# Lección 5: Estructuras de datos



#lista de productos, que tendra los productos en forma de diccionario
productos = []

#Usaremos set para evitar los duplicados en los ID´s
ids_registrados = set()


#función para agregar producto a la lista
def agregar_producto(producto):
    #Se agrega verificación de ID´s
    if producto["id"] in ids_registrados:
        print("Error: ID ya se encuentra en el sistema")
        return False

    #Si id no se encuentra en los ids_registrados, se agrega el producto
    productos.append(producto)
    ids_registrados.add(producto["id"])
    return True

#función para listar los productos con sus atributos
def listar_productos():
    if not productos:
        print("no hay productos registrados")
        return
    
    print("---Lista de productos---")
    for producto in productos:
        print(
            f"ID: {producto['id']} | "
            f"Nombre: {producto['nombre']} |"
            f"Precio: {producto['precio']} |"
            f"Stock: {producto['stock']} |"
            f"Categoría: {producto['categoria']}" 
        )

#función para aplicar metodo .remove() y eliminar productos con su ID
def eliminar_producto(id_producto):
    for producto in productos:
        if producto['id'] == id_producto:
            productos.remove(producto)
            ids_registrados.remove(id_producto)
            print("producto eliminado correctamente")
            return True
    
    print("producto no encontrado")
    return False
