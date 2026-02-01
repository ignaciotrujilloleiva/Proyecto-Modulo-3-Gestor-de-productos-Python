# Lección 4: Control de flujo y estructuras
# Lección 5: Estructuras de datos

from modulos.funciones_utiles import mostrar_titulo


#lista de productos, que tendra los productos en forma de diccionario
productos = []

#Usaremos set para evitar los duplicados en los ID´s
ids_registrados = set()


#función 1° para agregar producto a la lista
def agregar_producto(producto):
    #Se agrega verificación de ID´s
    if producto["id"] in ids_registrados:
        print("Error: ID ya se encuentra en el sistema")
        return False

    #Si id no se encuentra en los ids_registrados, se agrega el producto
    productos.append(producto)
    ids_registrados.add(producto["id"])
    return True

#función 2° para listar los productos con sus atributos
def listar_productos():
    if not productos:
        print("no hay productos registrados")
        return
    
    #función del titulo
    mostrar_titulo("Lista de productos")
    
    for producto in productos:
        print(
            f"ID: {producto['id']} | "
            f"Nombre: {producto['nombre']} | "
            f"Precio: {producto['precio']} | "
            f"Stock: {producto['stock']} | "
            f"Categoría: {producto['categoria']}" 
        )

#función 4° para aplicar metodo .remove() y eliminar productos con su ID
def eliminar_producto(id_producto):
    for producto in productos:
        if producto['id'] == id_producto:
            productos.remove(producto)
            ids_registrados.remove(id_producto)
            print("producto eliminado correctamente")
            return True
    
    print("producto no encontrado")
    return False

#función 3° de busqueda en la cual se aplicara .get(), .key() y .values()
def buscar_producto(id_producto):
    for producto in productos:
        #el metodo .get() es una forma más segura y apropiada para solicitar datos al diccionario ya que de no encontrarlo arroja "none"
        if producto.get('id') == id_producto:
            print("---Producto encontrado---")

            #Si el Id se encuentra, los keys y values del producto se almacenan en variable
            claves = list(producto.keys())
            valores = list(producto.values())

            #Mediante ciclo for se recorren las claves y valores para imprimirlos, se usa capitaliza para entregarlo en formato de tabla
            for clave, valor in producto.items():
                print(f"{clave.capitalize():12}: {valor}")

            return producto
    print("Producto no encontrado")
    return None