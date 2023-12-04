# CLASES ABSTRACTAS

# Una clase abstracta es una clase que no puede ser instanciada directamente, es decir, no puedes crear objetos a partir de ella.
# En su lugar, se utiliza como una plantilla para definir otras clases.
# Una clase abstracta puede contener métodos abstractos, que son métodos que deben ser implementados en las subclases.
# Estos métodos abstractos definen una interfaz que las subclases deben seguir.
# En Python, para crear una clase abstracta, puedes usar el módulo "abc".
from abc import ABC, abstractmethod

# Definimos una clase abstracta
class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Creamos una subclase que implementa FiguraGeometrica
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1415 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1415 * self.radio

# En este ejemplo, "FiguraGeometrica" es una clase abstracta que define dos métodos abstractos: "area" y "perimetro".
# La clase "Circulo" es una subclase que hereda de "FiguraGeometrica" y debe implementar ambos métodos abstractos.
# Esto garantiza que todas las subclases de "FiguraGeometrica" tengan estos métodos definidos.

# Si intentas crear una instancia de "FiguraGeometrica", obtendrás un error
# Pero puedes crear una instancia de "Circulo" y utilizar sus métodos:
circulo = Circulo(5)
print(f"Área del círculo: {circulo.area()}")
print(f"Perímetro del círculo: {circulo.perimetro()}")
