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

# Función para ingresar los datos de una cuenta desde el teclado
    def ingresar_datos(self):
        titular = input("Ingrese el nombre del titular de la cuenta: ")
        cantidad = float(input("Ingrese la cantidad inicial de la cuenta: "))
        self.set_titular(titular)
        self.set_cantidad(cantidad)
