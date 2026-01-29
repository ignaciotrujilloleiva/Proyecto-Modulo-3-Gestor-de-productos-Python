# Lección 6: Funciones y modularización

#Funciones reutilizables para el espaciado de las funciones en el menu

#Función usada posteriormente para crear una linea para encasillar el titulo
def imprimir_linea():
    print("-" * 40)

#Funcion que encasilla el titulo para imprimirlo
def mostrar_titulo(titulo):
    imprimir_linea()
    print(titulo.upper())
    imprimir_linea()
