# Sistema de Gestión de Productos
# Autor: Ignacio Trujillo
# Descripción: Programa por consola para gestionar productos usando Python


#importaciones
from modulos.menu import mostrar_menu
from modulos.datos_basicos import cargar_producto



#Funcion principal
def main():
    print("Bienvenido al sistema de gestion de productos")
    mostrar_menu()


# Verificación de que el script se ejecuta directamente
if __name__ == "__main__":
    main()
