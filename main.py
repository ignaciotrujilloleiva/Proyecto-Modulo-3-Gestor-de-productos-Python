# Sistema de Gestión de Productos
# Autor: Ignacio Trujillo
# Descripción: Programa por consola para gestionar productos usando Python

# Archivo principal del sistema
# Responsabilidad:
    #Iniciar la ejecución del programa
    #Mostrar el menu principal
    #coordinar la interacción entre el usuario y los modulos 

#importaciones
from modulos.menu import mostrar_menu
from modulos.funciones_utiles import mostrar_titulo



# Funcion principal
# Bucle principal del sistema.
# Permite que el menú se muestre de forma continua
# hasta que el usuario decida salir del programa.

def main():
    mostrar_titulo("Bienvenido al sistema de gestion de productos")
    mostrar_menu()


# Verificación de que el script se ejecuta directamente
if __name__ == "__main__":
    main()
