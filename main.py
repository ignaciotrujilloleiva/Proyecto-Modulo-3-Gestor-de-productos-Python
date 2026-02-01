# Sistema de Gestión de Productos
# Autor: Ignacio Trujillo
# Descripción: Programa por consola para gestionar productos usando Python


#importaciones
from modulos.menu import mostrar_menu
from modulos.funciones_utiles import mostrar_titulo



#Funcion principal
def main():
    mostrar_titulo("Bienvenido al sistema de gestion de productos")
    mostrar_menu()


# Verificación de que el script se ejecuta directamente
if __name__ == "__main__":
    main()
