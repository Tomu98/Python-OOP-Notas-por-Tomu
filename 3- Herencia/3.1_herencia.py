# --- HERENCIA ---

# Es un concepto fundamental que permite la creación de nuevas clases basadas en clases existentes.
# Se utiliza para modelar relaciones "es un" entre las clases, donde una nueva clase (llamada subclase o clase derivada) hereda atributos y métodos de una clase existente (llamada superclase o clase base).
# Esto es fundamental en la programación orientada a objetos para organizar y estructurar el código de manera eficiente.
# Para que una nueva clase herede de una super clase, la sintaxis que deberiamos utilizar sería "class NuevaClase(*Super Clase*)"

# Clase Base o Superclase:
# - La clase base, también llamada superclase, es la clase existente de la que se heredan los atributos y métodos.
# - Contiene características y comportamientos comunes que se comparten con una o más clases derivadas.

# Clase Derivada o Subclase:
# - La clase derivada, también llamada subclase, hereda los atributos y métodos de la clase base.
# - Puede agregar atributos y métodos adicionales o sobrescribir los existentes para personalizar su comportamiento.

# Ejemplo:
class Animal:      # Animal es la superclase común para varios tipos de animales
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):  # Perro es una subclase de Animal
    def hacer_sonido(self):
        return print("Woof")

class Gato(Animal):  # Gato es una subclase de Animal
    def hacer_sonido(self):
        return print("Meow")

gato1 = Gato("Gordo")
perro1 = Perro("Frida")
gato1.hacer_sonido()
perro1.hacer_sonido()
print(perro1.nombre)


# super()__init__
# Se utiliza para llamar al constructor de la clase base desde la subclase cuando estás trabajando con herencia.
# Cuando una subclase hereda de una clase base y quieres que la subclase también realice algunas acciones de inicialización específicas, puedes utilizar "super().__init__".
# El uso de super().__init__ es especialmente útil cuando la clase base tiene lógica de inicialización importante que la subclase debe heredar y extender.
# Ejemplo:
class ClaseBase:
    def __init__(self, parametro_base):
        self.parametro_base = parametro_base

class Subclase(ClaseBase):
    def __init__(self, parametro_base, parametro_subclase):
        super().__init__(parametro_base)   # Llama al constructor de la ClaseBase
        self.parametro_subclase = parametro_subclase

objeto_subclase = Subclase("Base", "Subclase")

print(objeto_subclase.parametro_base)      # Imprime "Base"
print(objeto_subclase.parametro_subclase)  # Imprime "Subclase"
