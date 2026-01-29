# Lección 4: Control de flujo y estructuras


#lista de productos, que tendra los productos en forma de diccionario
productos = []

#función para agregar producto a la lista
def agregar_producto(producto):
    productos.append(producto)

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