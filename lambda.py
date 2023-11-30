# Funcion encargada de obtener la entrada del usuario.
def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation # Devuelve los valores ingresados
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

# Funcion encargada de ejecutar las operaciones matematicas.
def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input

    # Diccionario encargado de asociar cada operación con una función lambda
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: No es posible dividir por cero.",
    }

    # Verifica si la operación ingresada por el usuario está en el diccionario
    if operation in operations:
        result = operations[operation](num1, num2)   # Calcula el resultado utilizando la función lambda correspondiente
    else:
        result = "Operacion invalida"

    print("Resultado:", result)



def main():
    while True:
        user_input = get_user_input()         # Obtiene la entrada del usuario

        # Estructura de control encargada de verificar si el usuario desea salir del programa
        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")
        ejecutar_operacion(user_input, None)   # Llama a la función para ejecutar la operación selecionada

main()

