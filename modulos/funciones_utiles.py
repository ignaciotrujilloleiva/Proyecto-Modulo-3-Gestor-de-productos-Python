# Lección 6: Funciones y modularización

#Funciones reutilizables para el espaciado de las funciones en el menu

#Función usada posteriormente para crear una linea para encasillar el titulo
def imprimir_linea():
    print("-" * 40)

#Función que encasilla el titulo para imprimirlo y centrarlo
def mostrar_titulo(titulo):
    imprimir_linea()
    print(titulo.upper().center(40))
    imprimir_linea()
