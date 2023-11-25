# LSP - Liskov's Subtitution Principle

# Principio de Sustitución de Liskov.
# El principio de sustitución de Liskov se refiere a la capacidad de sustituir objetos de una clase derivada por objetos de la clase base sin interrumpir el funcionamiento correcto del programa.
# Esto significa que las clases derivadas deben ser sustituibles por sus clases base sin cambiar el comportamiento del programa.
# Este principio garantiza que las subclases hereden correctamente las propiedades y comportamientos de las superclases.

# Ejemplo:
# Supongamos que tienes una jerarquía de clases para representar diferentes tipos de aves.
# Debes asegurarte de que las subclases se comporten de manera coherente con la clase base "Ave".
class Ave:
    def volar(self):
        pass

class Pajaro(Ave):
    def volar(self):
        print("El pájaro vuela con alas")

class Pinguino(Ave):
    def volar(self):
        print("El pingüino no puede volar")

# En este ejemplo, tanto "Pajaro" como "Pinguino" son subclases de "Ave" y pueden ser sustituidos por objetos de tipo "Ave" sin cambiar el comportamiento esperado.
