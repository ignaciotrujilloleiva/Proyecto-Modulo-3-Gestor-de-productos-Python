# Lección 2: Tipos de datos y sentencias básicas

#importaciónes desde validaciones
from modulos.validaciones import (validar_int,validar_string,validar_float)
#Diccionario con productos


#Tupla para las categorias
categorias = ("cat1","cat2","cat3","cat4")


#Declaración de variables para recibir y almacenar datos
def cargar_producto(id_producto):
    #solicita al usuario el ingreso de datos del producto
    nombre = validar_string("Ingrese nombre del producto: ")
    precio = validar_float("Ingrese precio del producto: ")
    stock = validar_int("Ingrese stock del producto: ")

    print("Categorias disponibles: ")
    #imprime las categorias disponibles
    for item, categoria in enumerate(categorias, start=1):
        print(f"{item}. {categoria}")

    #Validación de elección de categoria
    while True:
        opcion = validar_int("Seleccione categoría (número): ")
        if opcion >=1 and opcion <= len(categorias):
            categoria = categorias[opcion - 1]
            break
        else:
            print("Categoría inválida")
    

    #Diccionario del producto
    producto = {
        "id": id_producto,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "categoria": categoria,
        
    }

    return producto
