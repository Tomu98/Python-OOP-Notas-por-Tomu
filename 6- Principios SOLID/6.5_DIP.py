# DIP - Dependency Inversion Principle

# Principio de Inversión de Dependencias.
# El principio de inversión de dependencias establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino que ambos deben depender de abstracciones.
# Además, las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstracciones.
# En resumen, este principio fomenta la utilización de interfaces o clases abstractas para desacoplar componentes del sistema, lo que facilita la modificación y expansión del software.

# Ejemplo que no cumple con el DIP:
# Supongamos que tenemos una clase "Cocina" que depende directamente de una clase concreta "Ingrediente", lo que viola el DIP al acoplar la clase "Cocina" a una implementación concreta de "Ingrediente":

# Clase concreta para representar un ingrediente
class Ingrediente:

    def obtener_nombre(self):
        pass

# Clase para representar una cocina
class Cocina:

    def __init__(self, ingrediente):
        self.ingrediente = ingrediente

    def preparar_plato(self):
        nombre = self.ingrediente.obtener_nombre()
        print(f"Preparando plato con {nombre}")

# Clase concreta para un ingrediente específico
class Tomate(Ingrediente):

    def obtener_nombre(self):
        return "tomates"

# Clase concreta para otro ingrediente específico
class Cebolla(Ingrediente):

    def obtener_nombre(self):
        return "cebollas"

# En este ejemplo, la clase "Cocina" depende directamente de la clase concreta "Ingrediente", lo que hace que "Cocina" esté fuertemente acoplada a una implementación específica de "Ingrediente".
# Esto viola el DIP porque los módulos de alto nivel (en este caso, "Cocina") no deben depender de detalles de implementación (como "Tomate" o "Cebolla").


# Ejemplo que cumple con el DIP:
# Primero, definiremos una interfaz "IngredienteDIP" que servirá como abstracción para los ingredientes.
# Luego, la clase "CocinaDIP" dependerá de esta interfaz en lugar de una implementación concreta:
from abc import ABC, abstractmethod

# Interfaz abstracta para representar un ingrediente
class IngredienteDIP(ABC):

    @abstractmethod
    def obtener_nombre(self):
        pass

# Clase concreta para representar un ingrediente específico
class TomateDIP(IngredienteDIP):

    def obtener_nombre(self):
        return "tomates"

# Clase concreta para representar otro ingrediente específico
class CebollaDIP(IngredienteDIP):

    def obtener_nombre(self):
        return "cebollas"

# Clase para representar una cocina que utiliza ingredientes
class CocinaDIP:

    def __init__(self, ingrediente):
        self.ingrediente = ingrediente

    def preparar_plato(self):
        nombre = self.ingrediente.obtener_nombre()
        print(f"Preparando plato con {nombre}")

# En este diseño revisado, la clase "CocinaDIP" depende de la interfaz "IngredienteDIP", que es una abstracción.
# Las clases concretas como "TomateDIP" y "CebollaDIP" implementan esta interfaz.
# Esto cumple con el Principio de Inversión de Dependencias, ya que "CocinaDIP" depende de una abstracción en lugar de una implementación concreta de "IngredienteDIP".
# Ahora, es posible cambiar la implementación de "IngredienteDIP" sin afectar la clase "CocinaDIP".
