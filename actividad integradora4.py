def contar_palabras(texto):
    # Inicializar el diccionario
    diccionario = {}
    # Convertir el texto a una lista de palabras
    palabras = texto.split()
    # Recorrer cada palabra y contar su frecuencia
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario


def palabra_mas_repetida(diccionario):
    # Encontrar la palabra con la frecuencia máxima
    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    return (palabra_max, frecuencia_max)


# Ejemplo de uso
texto = input("Ingresa un texto: ")
diccionario = contar_palabras(texto)
palabra, frecuencia = palabra_mas_repetida(diccionario)
print(
    f"La palabra más repetida es '{palabra}' con una frecuencia de {frecuencia}.")
