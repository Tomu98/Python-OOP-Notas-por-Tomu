# --- ABSTRACCION ---

# La abstracción es un principio clave que se utiliza para modelar objetos del mundo real en un programa informático de una manera simplificada y estructurada.
# La abstracción es el proceso de simplificar la complejidad de un objeto del mundo real al identificar las características esenciales y representarlas en un modelo que puede ser utilizado en un programa de software.
# En POO, la abstracción se logra mediante la creación de clases y objetos.

# Elementos de la Abstracción:
# - Clase: Una clase es una plantilla o un plano que define las propiedades y el comportamiento de un objeto.
#   Representa una abstracción general de un conjunto de objetos similares.
#   Por ejemplo, puedes tener una clase llamada "Vehiculo" que define las propiedades y comportamientos comunes de todos los vehículos.
# - Objeto: Un objeto es una instancia específica de una clase.
#   Es una representación concreta de la abstracción definida por la clase.
#   Por ejemplo, un objeto de la clase "Vehiculo" podría ser un automóvil en particular.
# - Atributos: Los atributos son las características o propiedades de un objeto que se utilizan para describirlo.
#   Por ejemplo, un objeto de la clase "Vehiculo" podría tener atributos como "marca", "modelo", "color", etc.
# - Métodos: Los métodos son funciones definidas en una clase que representan el comportamiento de un objeto.
#   Por ejemplo, un objeto de la clase "Vehiculo" podría tener métodos como "acelerar()", "frenar()", "encender()", etc.


# Ejemplo de Abstracción.
# Supongamos que deseamos modelar una abstracción para representar vehículos.
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando")

    def encender(self):
        print(f"{self.marca} {self.modelo} encendido")

coche = Vehiculo("Toyota", "Corolla", "Rojo")
moto = Vehiculo("Honda", "CBR600RR", "Negra")

coche.encender()
coche.acelerar()
coche.frenar()

moto.encender()
moto.acelerar()

# "Vehiculo" es una clase que abstrae las características comunes de los vehículos, como la marca, el modelo y el color.
# "coche" y "moto" son objetos concretos creados a partir de la clase "Vehiculo".
# Cada objeto tiene sus propias propiedades (marca, modelo, color) y puede ejecutar sus propios métodos (encender, acelerar, frenar).


# La abstracción nos permite modelar objetos del mundo real de manera más organizada y simplificada en nuestro programa.
# Cada objeto es una instancia de una clase y hereda las características y el comportamiento definidos por esa clase.
# Esto facilita el desarrollo y el mantenimiento del código, ya que podemos trabajar con conceptos de alto nivel y reutilizar clases en diferentes partes del programa.
