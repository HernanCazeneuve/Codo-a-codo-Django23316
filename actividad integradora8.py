class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    # Setter y Getter para el atributo titular
    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular

    # Setter y Getter para el atributo cantidad
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    # Método para mostrar los datos de la cuenta
    def mostrar(self):
        print("Titular de la cuenta:", self.titular)
        print("Saldo de la cuenta:", self.cantidad)

    # Método para ingresar una cantidad a la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    # Método para retirar una cantidad de la cuenta
    def retirar(self, cantidad):
        self.cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # Setter y Getter para el atributo bonificacion
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    # Método para validar si el titular es mayor de edad pero menor de 25 años
    def es_titular_valido(self):
        edad = int(input("Ingrese la edad del titular: "))
        return edad >= 18 and edad < 25

    # Método para mostrar los datos de la cuenta joven
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.bonificacion)

    # Método para retirar una cantidad de la cuenta joven, solo si el titular es válido
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

# Función para ingresar los datos de una cuenta desde el teclado
    def ingresar_datos(self):
        titular = input("Ingrese el nombre del titular de la cuenta: ")
        cantidad = float(input("Ingrese la cantidad inicial de la cuenta: "))
        self.set_titular(titular)
        self.set_cantidad(cantidad)
