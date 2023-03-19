# Solución iterativa:

# def get_int():
#     while True:
#         try:
#             num = int(input("Introduzca un valor entero: "))
#             print("Número aceptado:", num)
#             return num
#         except ValueError:
#             print("Valor introducido no es un entero válido, intente nuevamente.")
# get_int()

# Solucion recursiva
def get_int():
    try:
        num = int(input("Introduzca un valor entero: "))
        print("Número aceptado:", num)
        return num
    except ValueError:
        print(
            "El valor introducido no es un entero válido, intente nuevamente.")
        return get_int()


get_int()
