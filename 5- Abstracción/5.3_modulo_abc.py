# MÓDULO "abc"

# El módulo "abc" en Python se refiere a "Abstract Base Classes" (Clases Base Abstractas), y es una parte importante de la POO en Python.
# Las clases base abstractas son clases que no se pueden instanciar directamente, pero sirven como plantillas o interfaces para otras clases.
# El módulo "abc" proporciona herramientas para definir y trabajar con clases base abstractas en Python.
# Esto es útil para diseñar jerarquías de clases sólidas y mantener el código más legible y mantenible en proyectos con POO.

# "ABC" (Abstract Base Class)
# Una ABC es una clase que no se supone que se instancie directamente. 
# En su lugar, se utiliza como una plantilla para definir comportamientos comunes que deben tener las clases derivadas.
#  Esto fomenta la consistencia en la estructura de las clases y ayuda a garantizar que ciertos métodos estén presentes en las clases derivadas.

# "@abstractmethod"
# El módulo "abc" proporciona un decorador llamado "@abstractmethod", que se utiliza para marcar métodos en una clase como abstractos.
# Los métodos abstractos son aquellos que deben ser implementados en las clases derivadas.
# Si una clase derivada no implementa un método marcado como abstracto, Python generará un error en tiempo de ejecución.

from abc import ABC, abstractmethod

class MiClaseAbstracta(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass

# ABCMeta (Metaclase)
# La clase base abstracta se define utilizando la metaclase "ABCMeta".
# Esto se hace declarando la clase base abstracta como una subclase de "ABCMeta".

# "isinstance" y "issubclass"
# Puedes utilizar las funciones "isinstance()" y "issubclass()" para verificar si un objeto es una instancia de una clase abstracta o si una clase es una subclase de una clase abstracta.
class MiClase(MiClaseAbstracta):
    def metodo_abstracto(self):
        pass

instancia = MiClase()
print(isinstance(instancia, MiClaseAbstracta))  # True
print(issubclass(MiClase, MiClaseAbstracta))    # True

# "@abstractclassmethod"
# Se utiliza en el contexto de clases abstractas y se aplica a métodos de clase abstractos.
# Los métodos de clase abstractos son métodos que deben ser implementados en las subclases, pero en lugar de actuar sobre instancias de la clase, operan en la clase misma.

# Un método de clase abstracto es un método de una clase abstracta que debe ser implementado por todas las subclases de esa clase abstracta.
# A diferencia de los métodos de instancia, los métodos de clase no requieren una instancia de la clase para ser invocados.
# En cambio, operan en la clase misma y pueden ser invocados a través de la clase en lugar de una instancia.
# Para marcar un método de clase como abstracto en Python, se utiliza el decorador "@abstractclassmethod"
class MiCAbstracta(ABC):
    # @abstractclassmethod
    def metodo_de_clase_abstracto(self):
        pass

class MiSubclase(MiClaseAbstracta):
    @classmethod
    def metodo_de_clase_abstracto(cls):
        return "Implementación en MiSubclase"

resultado = MiSubclase.metodo_de_clase_abstracto()
print(resultado)  # Imprimirá "Implementación en MiSubclase"

# En este ejemplo, "metodo_de_clase_abstracto" es un método de clase abstracto marcado con "@abstractclassmethod" en la clase abstracta "MiCAbstracta". 
# Esto significa que cualquier subclase de "MiCAbstracta" debe proporcionar una implementación concreta de "metodo_de_clase_abstracto".
# La subclase "MiSubclase" hereda de "MiCAbstracta" y proporciona una implementación concreta para el método de clase abstracto "metodo_de_clase_abstracto".
# La subclase "MiSubclase" puede invocar "metodo_de_clase_abstracto" como si fuera un método de clase normal.
# Esto muestra cómo se puede utilizar "@abstractclassmethod" para definir una interfaz que las subclases deben seguir

# Si una subclase no proporciona una implementación para un método de clase abstracto, Python generará un error en tiempo de ejecución.
# Esto asegura que todas las subclases cumplan con los requisitos de la clase abstracta.

# En resumen, "@abstractclassmethod" se utiliza para marcar métodos de clase abstractos en una clase abstracta.
# Estos métodos deben ser implementados en todas las subclases para asegurar que las subclases sigan una interfaz común.




# IMPORTANTE: Mientras hacáa el curso, segun Pylint me indicó que "@abstractclassmethod" era obsoleto.
# Asi que pondré abajo la supuesta solución y mejora...

# "@classmethod" y "@abstractmethod" juntos.

# @classmethod: es un decorador en Python que se utiliza para definir métodos de clase.
# Los métodos de clase son aquellos que están asociados con la clase en lugar de una instancia específica de la clase.
# Estos métodos pueden acceder y modificar atributos y métodos de clase sin necesidad de crear una instancia de la clase.
# Se definen utilizando la palabra clave "@classmethod" justo encima de la definición del método.
# En detalle:
# - Un método de clase se puede llamar en la clase misma, sin necesidad de crear una instancia de la clase.
# - Un método de clase tiene un primer parámetro convencional llamado "cls", que hace referencia a la propia clase en lugar de la instancia.
# - Los métodos de clase son útiles para realizar operaciones que no dependen de una instancia específica, pero que aún están relacionadas con la clase.
# - Los métodos de clase también se pueden utilizar para crear constructores alternativos para la clase.
# Ejemplo:
class MiClaseM:
    contador = 0  # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre
        MiClaseM.contador += 1

    @classmethod
    def obtener_contador(cls):
        return cls.contador

objeto1 = MiClaseM("Objeto1")
objeto2 = MiClaseM("Objeto2")

contador = MiClaseM.obtener_contador()
print(f"El contador es: {contador}")

# En este ejemplo, "@classmethod" se utiliza para definir el método "obtener_contador", que puede ser llamado en la clase "MiClaseM" sin necesidad de crear una instancia de la misma.


# @abstractmethod: es un decorador en Python que se utiliza en una clase base para declarar un método como abstracto.
# Los métodos abstractos son métodos que deben ser implementados por las clases derivadas (subclases) de la clase base.
# Las clases que contienen métodos abstractos también se consideran abstractas y no se pueden instanciar directamente.
# En detalle:
# - Un método abstracto se declara en la clase base utilizando el decorador "@abstractmethod".
# - Las subclases deben implementar todos los métodos abstractos de la clase base.
# - Las clases que contienen al menos un método abstracto se consideran abstractas y no se pueden instanciar directamente.
# - Los métodos abstractos proporcionan una interfaz que las subclases deben seguir.
# Ejemplo:
class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Intentar crear una instancia de FiguraGeometrica generará un error
# figura = FiguraGeometrica()  # Esto generará un TypeError

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
area_circulo = circulo.calcular_area()
area_rectangulo = rectangulo.calcular_area()
print(f"Área del círculo: {area_circulo}")
print(f"Área del rectángulo: {area_rectangulo}")

# En este ejemplo, "@abstractmethod" se utiliza para declarar el método "calcular_area" en la clase base "FiguraGeometrica".
# Las subclases "Circulo" y "Rectangulo" deben implementar este método, de lo contrario, generaría un error.
# Esto asegura que todas las subclases de "FiguraGeometrica" proporcionen una implementación concreta de "calcular_area".

# Uso de "@classmethod" y "@abstractmethod" juntos
# Puedes utilizar "@classmethod" y "@abstractmethod" juntos en una clase si necesitas definir un método de clase abstracto. Aquí tienes un ejemplo:
class MiClaseAbstracta2(ABC):
    valor = 0

    @classmethod
    @abstractmethod
    def obtener_valor(cls):
        pass

class MiClaseConcreta(MiClaseAbstracta2):
    @classmethod
    def obtener_valor(cls):
        return cls.valor

# Intentar crear una instancia de MiClaseAbstracta2 generará un error
# abstract_instance = MiClaseAbstracta2()  # Esto generará un TypeError

# Crear una instancia de MiClaseConcreta
concrete_instance = MiClaseConcreta()

# Asignar un valor a la clase concreta
concrete_instance.valor = 42

# Llamar al método de clase abstracto
valor = concrete_instance.obtener_valor()
print(f"El valor es: {valor}")

# En este ejemplo, "@classmethod" y "@abstractmethod" se combinan en la definición del método "obtener_valor" en la clase abstracta "MiClaseAbstracta2".
# La subclase "MiClaseConcreta" debe implementar este método como un método de clase.
# Esto permite que las subclases concretas proporcionen una implementación específica para "obtener_valor".
