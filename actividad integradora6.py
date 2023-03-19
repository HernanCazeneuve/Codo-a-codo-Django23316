class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Getters para el atributo 'nombre'
    def get_nombre(self):
        return self.nombre

    # Setter para el atributo 'nombre'
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            print('Error: El nombre debe ser una cadena de texto.')

    # Getters para el atributo 'edad'
    def get_edad(self):
        return self.edad

    # Setter para el atributo 'edad'
    def set_edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self.edad = edad
        else:
            print('Error: La edad debe ser un número entero positivo.')

    # Getters para el atributo 'dni'
    def get_dni(self):
        return self.dni

    # Setter para el atributo 'dni'
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.dni = dni
        else:
            print('Error: El DNI debe ser una cadena de texto de 9 caracteres.')

    def mostrar(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}')

    def es_mayor_de_edad(self):
        return self.edad >= 18


def ingresar_datos_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = input("Ingrese la edad de la persona: ")
    dni = input("Ingrese el DNI de la persona: ")
    persona = Persona()
    persona.set_nombre(nombre)
    persona.set_edad(int(edad))
    persona.set_dni(dni)
    return persona


persona1 = ingresar_datos_persona()
persona1.mostrar()
print(f"¿Es mayor de edad?: {persona1.es_mayor_de_edad()}")
