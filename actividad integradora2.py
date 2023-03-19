def obtener_mcm():
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            if num1 <= 0 or num2 <= 0:
                print("Ingrese solo números enteros positivos.")
            else:
                break
        except ValueError:
            print("Ingrese solo números enteros positivos.")

    # Calculamos el máximo común divisor usando el algoritmo de Euclides
    def mcd(num1, num2):
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        return num1

    # Calculamos el mínimo común múltiplo usando la fórmula
    mcm = (num1 * num2) // mcd(num1, num2)
    return mcm
