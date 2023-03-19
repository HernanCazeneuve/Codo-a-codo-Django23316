def contar_palabras(texto):
    # Convertir el texto en una lista de palabras
    palabras = texto.split()

    # Crear un diccionario vacío para almacenar las frecuencias
    frecuencias = {}

    # Iterar sobre cada palabra en la lista
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementar su frecuencia
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        # Si no está en el diccionario, agregarla con una frecuencia de 1
        else:
            frecuencias[palabra] = 1

    # Devolver el diccionario de frecuencias
    return frecuencias


# Ejemplo de uso
texto = input("Ingresa un texto: ")
resultado = contar_palabras(texto)
print(resultado)
