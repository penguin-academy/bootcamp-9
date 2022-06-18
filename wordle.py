# Todos los créditos a Mayra 🤸🧘‍♀️

import os

os.system("clear")

# Definir cuantas letras va a tener la palabra
cantidad_de_letras_de_la_palabra_a_encontrar = 5

# Definimos nuestra palabra a encontrar
palabra_a_encontrar = "gatos"

# Crear nuestra lista que va a contener otras listas dentro
grilla = []

# Definir la cantidad de intentos
intentos = 6

# Creamos nuestra función para verfiicar las opciones del juego
def obtener_la_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    # creamos la lista que va a contener nuestro resultado
    resultado = []

    # Creamos la lista de letras en la palabra a encontrar
    letras_de_la_palabra_a_encontrar = list(palabra_a_encontrar)

    # Creamos la lista de letras de la palabra ingresada
    letras_de_la_palabra_ingresada = list(palabra_ingresada)

    # Iteramos en cada posición de ambas listas
    for posicion_de_la_letra in range(cantidad_de_letras_de_la_palabra_a_encontrar):
        # Verificamos si las letras en la misma posición son iguales
        las_letras_son_iguales = letras_de_la_palabra_a_encontrar[posicion_de_la_letra] == letras_de_la_palabra_ingresada[posicion_de_la_letra]

        # Verificamos si la letra existe en la palabra
        la_letra_existe_en_la_palabra = letras_de_la_palabra_ingresada[posicion_de_la_letra] in palabra_a_encontrar

        if las_letras_son_iguales:
            # Guardar las letras que estan en la palabra a encontrar y coinciden en la posición entre []
            letra_modificada = '[' + letras_de_la_palabra_ingresada[posicion_de_la_letra] + ']'
            resultado.append(letra_modificada)
        elif la_letra_existe_en_la_palabra:

            letra_modificada = '(' + letras_de_la_palabra_ingresada[posicion_de_la_letra] + ')'
            resultado.append(letra_modificada)
        else:
            resultado.append(letras_de_la_palabra_ingresada[posicion_de_la_letra])
        
    return resultado

# Creamos nuestra función de imprimir grilla
def imprimir_grilla(grilla):
    cantidad_de_filas = len(grilla)

    for fila in range(cantidad_de_filas):
        print(grilla[fila])

# Iniciar nuestro juego
while intentos > 0:
    print("Te quedan", intentos ,"intentos.")
    palabra_ingresada = input("Ingrese su respuesta:")
    intentos = intentos - 1 # Se crea un bucle en la variable intentos para que se ejecute mientras la resta sea mayor a 0.

    os.system("clear")

    
    letras_de_la_palabra_a_encontrar = list(palabra_a_encontrar)
    letras_de_la_palabra_ingresada = list(palabra_ingresada)

    if len(palabra_ingresada) != cantidad_de_letras_de_la_palabra_a_encontrar:
        print("La palabra ingresada no tiene la cantidad de letras correcta.")
        print(" Ingresar una palabra con", cantidad_de_letras_de_la_palabra_a_encontrar, "letras.")
    else:
        linea_verificada = obtener_la_fila_verificada(palabra_a_encontrar, palabra_ingresada)
        grilla.append(linea_verificada)

    imprimir_grilla(grilla)
    
    if palabra_ingresada != palabra_a_encontrar:
        print("Vuelva a intentarlo")
    else:
        print("Ganaste!")
        break