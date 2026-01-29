#Lección 3: Sentencias condicionales


#función para validación del string, valida que el texto del usuario no este vacío
def validar_string(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("El texto no puede estar vacío")
        else:
            return texto
        
#función para validación del int, isdigit mendiante un bool verifica que lo escrito por el usuario sean numeros
def validar_int(mensaje):
    while True:
        numero = input(mensaje)

        if numero.isdigit():
            return int(numero)
        else:
            print("Debe ingresar un número entero válido")

#función para validación del float, try se usa para intentar devolver un float, en caso de error pasa al except
def validar_float(mensaje):
    while True:
        decimal= input(mensaje)

        try:
            return float(decimal)
        except ValueError:
            print("Debe ingresar un número decimal válido")