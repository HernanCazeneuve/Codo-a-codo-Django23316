import math


def mcd():
    # Pedir dos números al usuario
    a = input("Ingrese el primer número: ")
    b = input("Ingrese el segundo número: ")

    # Validar que sean enteros
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Los números deben ser enteros")
        return

    # Calcular el máximo común divisor usando la función math.gcd()
    resultado = math.gcd(a, b)

    # Mostrar el resultado
    print(f"El máximo común divisor entre {a} y {b} es {resultado}")


# Llamar a la función
mcd()
