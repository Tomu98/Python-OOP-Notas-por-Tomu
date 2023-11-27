# SOBREESCRITURA DE MÉTODOS
# También conocido como "Overriding".
# Permite a una clase hija (o subclase) proporcionar una implementación específica de un método que ya está definido en su clase padre (o superclase).
# Esto permite personalizar el comportamiento de un método heredado en la clase hija sin modificar la definición original en la superclase.

# En la subclase, la sobreescritura de métodos se realiza definiendo un método con el mismo nombre que el de la superclase.
# Cuando se llama al método en un objeto de la subclase, Python ejecutará la versión del método definida en la subclase en lugar de la versión de la superclase.

# Ejemplo:
class Animal:
    def hablar(self):
        print("Este animal hace algún sonido.")

class Perro(Animal):
    def hablar(self):
        print("El perro ladra.")

animal_generico = Animal()
mi_perro = Perro()

animal_generico.hablar()  # Imprime "Este animal hace algún sonido."
mi_perro.hablar()         # Imprime "El perro ladra."

# Como puedes ver, cuando llamamos al método hablar() en un objeto de la clase Perro, Python ejecuta la versión de la subclase (Perro), que imprime "El perro ladra".
# Esto demuestra la sobreescritura exitosa del método.

# Ventajas de la sobreescritura de métodos es que permite personalizar el comportamiento de los métodos heredados en las subclases.
# Tambien facilita la implementación de la herencia, ya que las subclases pueden adaptar el comportamiento de los métodos a sus necesidades específicas sin modificar la superclase.
# Y ayuda a mantener un código más limpio y organizado, ya que evita la duplicación innecesaria de código.



# Ejemplo en vehiculos:
class Vehiculo:
    def encender_motor(self):
        print("El vehículo ha encendido el motor.")

class Coche(Vehiculo):
    def encender_motor(self):
        print("El coche ha encendido el motor y está listo para conducir.")

class Motocicleta(Vehiculo):
    def encender_motor(self):
        print("La motocicleta ha encendido el motor y está lista para arrancar.")

mi_coche = Coche()
mi_motocicleta = Motocicleta()

mi_coche.encender_motor()        # Imprime "El coche ha encendido el motor y está listo para conducir."
mi_motocicleta.encender_motor()  # Imprime "La motocicleta ha encendido el motor y está lista para arrancar."

# En este ejemplo, tenemos una superclase "Vehiculo" con un método "encender_motor()", y luego creamos dos subclases, "Coche" y "Motocicleta", que heredan de la superclase.
# Ambas subclases sobreponen el método "encender_motor()" para proporcionar su propia implementación personalizada.
# Cuando llamamos a encender_motor() en objetos de Coche y Motocicleta, Python ejecuta la versión del método definida en la subclase correspondiente, lo que nos permite ver diferentes mensajes de salida según el tipo de vehículo.
