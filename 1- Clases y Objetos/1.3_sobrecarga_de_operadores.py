# --- SOBRECARGA DE OPERADORES ---

# La sobrecarga de operadores ("operator overloading" en inglés) es una característica de POO que permite a las clases definir cómo deben comportarse los operadores estándar cuando se aplican a objetos de esa clase.
# En otras palabras, te permite darle a tus objetos el comportamiento que consideres apropiado cuando se utilizan operadores comunes como +, -, *, /, ==, entre otros.
# La sobrecarga de operadores se basa en métodos especiales en Python, que se llaman "métodos mágicos" o "métodos dunder" (del inglés "double underscore").
# Cuando aplicas un operador a un objeto de una clase que ha definido estos métodos, Python invoca automáticamente el método correspondiente para realizar la operación.
# Debes utilizarla con precaución y documentar adecuadamente su uso, ya que puede hacer que el código sea menos intuitivo si se abusa de ella.

# Ejemplo 1: Sobrecarga de operadores aritméticos.
class MiNumero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, other):
        return MiNumero(self.valor + other.valor)

    def __sub__(self, other):
        return MiNumero(self.valor - other.valor)

    def __mul__(self, other):
        return MiNumero(self.valor * other.valor)

    def __truediv__(self, other):
        if other.valor != 0:
            return MiNumero(self.valor / other.valor)
        raise ValueError("División por cero no permitida")

a = MiNumero(5)
b = MiNumero(3)

resultado_suma = a + b
resultado_resta = a - b
resultado_multiplicacion = a * b
resultado_division = a / b

print(resultado_suma.valor)            # Resultado de la suma: 8
print(resultado_resta.valor)           # Resultado de la resta: 2
print(resultado_multiplicacion.valor)  # Resultado de la multiplicación: 15
print(resultado_division.valor)        # Resultado de la división: 1.6666666666666667

# En este ejemplo, hemos definido la clase "MiNumero" que sobrecarga los operadores aritméticos (+, -, *, /) para trabajar con objetos de la clase.


# Ejemplo 2: Sobrecarga de operadores de comparación.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecargamos el operador de igualdad (==).
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Sobrecargamos el operador de desigualdad (!=).
    def __ne__(self, other):
        return not self.__eq__(other)

    # Sobrecargamos el operador de menor que (<).
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    # Sobrecargamos el operador de menor o igual que (<=).
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    # Sobrecargamos el operador de mayor que (>).
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # Sobrecargamos el operador de mayor o igual que (>=).
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

punto1 = Punto(3, 4)
punto2 = Punto(3, 4)
punto3 = Punto(1, 2)

print(punto1 == punto2)  # True, porque tienen las mismas coordenadas
print(punto1 != punto3)  # True, porque tienen coordenadas diferentes
print(punto1 < punto3)   # False, porque punto1 no es menor que punto3
print(punto1 <= punto2)  # True, porque punto1 es igual a punto2
print(punto1 > punto3)   # True, porque punto1 es mayor que punto3
print(punto1 >= punto2)  # True, porque punto1 es igual a punto2

# En este ejemplo, hemos definido la clase "Punto" que representa un punto en un plano cartesiano con coordenadas "x" "e" "y".
# Hemos sobrecargado los operadores de comparación (==, !=, <, <=, >, >=) para que funcionen de acuerdo a las coordenadas de los puntos.
# Esto nos permite comparar objetos "Punto" utilizando estos operadores de manera intuitiva.


# Ejemplo 3: Sobrecarga de operadores de asignación.
class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    # Sobrecarga del operador de asignación +=.
    def __iadd__(self, monto):
        self.saldo += monto
        return self

    # Sobrecarga del operador de representación.
    def __str__(self):
        return f"Saldo actual: {self.saldo}"

cuenta = CuentaBancaria(1000)

# Realizamos una operación de depósito usando el operador +=.
cuenta += 500  # Esto es equivalente a cuenta = cuenta + 500
print(cuenta)  # Saldo actual: 1500

# En este ejemplo, hemos definido la clase "CuentaBancaria", que tiene un atributo "saldo" para rastrear el saldo de la cuenta.
# Luego, hemos sobrecargado el operador "+=" mediante el método "__iadd__".
# Cuando aplicamos "cuenta += 500", Python llama automáticamente a "cuenta.__iadd__(500)", que aumenta el saldo de la cuenta en 500 unidades y devuelve la misma instancia de la cuenta para que podamos seguir realizando más operaciones.
