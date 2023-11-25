# --- SINGLETON ---

# Su objetivo principal es asegurarse de que una clase tenga una sola instancia en toda la ejecución del programa y proporcionar un punto de acceso global a esa instancia.
# Esto es útil en situaciones donde solo necesitas una única instancia de una clase para coordinar acciones en todo el sistema, como configuración, registro de eventos, administración de recursos compartidos, entre otros.

# Pasos para implementar un Singleton:
# - Privatizar el constructor: Para evitar que se creen múltiples instancias de la clase, debes hacer que el constructor sea privado (esto se logra utilizando un método privado "__init__").
# - Mantener una referencia a la instancia: Dentro de la clase Singleton, debes mantener una referencia a la única instancia creada.
# - Proporcionar un punto de acceso global: Debes proporcionar un método público que permita a otros objetos obtener la instancia única.

# Ejemplo:
class Singleton:
    _instance = None  # Almacena la instancia única

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Esta clase es un Singleton. Usa Singleton.get_instance() para obtener la instancia.")
        Singleton._instance = self
        self.data = []  # Datos de ejemplo

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def add_data(self, value):
        self.data.append(value)

# Uso del Singleton
singleton_instance1 = Singleton.get_instance()
singleton_instance1.add_data(1)

singleton_instance2 = Singleton.get_instance()
singleton_instance2.add_data(2)

print(singleton_instance1.data)  # Imprime [1, 2]
print(singleton_instance1 is singleton_instance2)  # True


# Hemos creado una clase "Singleton" con un constructor privado y un método "get_instance" que proporciona la instancia única de la clase.
# El método "add_data" agrega datos a una lista dentro de la instancia del Singleton.
# Cuando intentas crear una segunda instancia de "Singleton", obtienes la misma instancia que la primera.
# Esto se verifica con "singleton_instance1" is "singleton_instance2", que imprime "True".


# El patrón Singleton es útil cuando necesitas compartir recursos o configuración global en tu programa y deseas garantizar que solo haya una instancia de la clase que los gestione.
# Sin embargo, debes tener cuidado al usarlo, ya que puede llevar a problemas de acoplamiento y dificultades en las pruebas unitarias.
