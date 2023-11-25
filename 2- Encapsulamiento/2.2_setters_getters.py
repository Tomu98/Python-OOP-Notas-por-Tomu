# --- SETTERS Y GETTERS ---

# Son una convención utilizada en la programación orientada a objetos (POO) para proporcionar acceso controlado a los atributos de una clase.
# Estos métodos se utilizan para obtener (get) y establecer (set) los valores de los atributos de un objeto de forma controlada, en lugar de acceder directamente a los atributos.
# La principal ventaja de utilizar getters y setters es que proporcionan un control más preciso sobre el acceso y la modificación de los atributos de una clase.
# Puedes agregar lógica adicional en los setters para validar los valores antes de asignarlos, lo que ayuda a mantener la integridad de los datos en tus objetos.
# Además, si en el futuro necesitas realizar cambios en la forma en que se manejan los atributos, puedes hacerlo en los getters y setters sin afectar el código que utiliza la clase.

# Getters ("get"):
# Un método "get" se utiliza para obtener el valor de un atributo de una clase.
# Generalmente tienen el formato get_nombre_del_atributo, donde "nombre_del_atributo" es el nombre del atributo que deseas obtener.
# Suelen ser métodos públicos y solo se utilizan para leer el valor de un atributo, no para modificarlo.

# Setters ("set"):
# Un método "set" se utiliza para establecer el valor de un atributo de una clase.
# Generalmente tienen el formato set_nombre_del_atributo, donde "nombre_del_atributo" es el nombre del atributo que deseas establecer.
# Suelen ser métodos públicos y se utilizan para modificar el valor de un atributo.

# Ejemplo sencillo de ambos casos juntos:
class PersonaGetSet:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

abel = PersonaGetSet("Abel", 24)

print(abel.get_nombre())    # Obtenemos el nombre
abel.set_nombre("Pepito")   # Establecemos un nombre nuevo
print(abel.get_nombre())    # Obtenemos de nuevo ese nombre nuevo


# Ejemplo de una cuenta bancaria más compleja
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular       # Atributo privado
        self.__saldo = saldo_inicial   # Atributo privado

    # Getter para obtener el titular
    def obtener_titular(self):
        return self.__titular

    # Getter para obtener el saldo
    def obtener_saldo(self):
        return self.__saldo

    # Setter para establecer el saldo
    def establecer_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("El saldo no puede ser negativo.")

    # Método para realizar un depósito
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado.")
        else:
            print("La cantidad de depósito debe ser mayor que cero.")

    # Método para realizar un retiro
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado.")
        else:
            print("Cantidad de retiro no válida o saldo insuficiente.")

# Crear una cuenta bancaria
cuenta_abel = CuentaBancaria("Abel Tomas", 1000)

# Obtener el titular y el saldo utilizando los getters
print(f"Titular: {cuenta_abel.obtener_titular()}")  # Abel Tomas
print(f"Saldo: {cuenta_abel.obtener_saldo()}")      # 1000

# Realizar un depósito
cuenta_abel.depositar(500)
print(f"Nuevo saldo: {cuenta_abel.obtener_saldo()}")  # 1500

# Intentar retirar una cantidad mayor que el saldo
cuenta_abel.retirar(2000)  # Saldo insuficiente

# Cambiar el saldo utilizando el setter
cuenta_abel.establecer_saldo(2000)
print(f"Nuevo saldo: {cuenta_abel.obtener_saldo()}")  # 2000

# En este ejemplo, la clase "CuentaBancaria" tiene dos atributos privados: "__titular" y "__saldo".
# Se han definido métodos "getter" (obtener_titular y obtener_saldo) y un método "setter" (establecer_saldo) para acceder y modificar estos atributos de manera controlada.
# También se han agregado métodos para realizar depósitos y retiros en la cuenta bancaria.
