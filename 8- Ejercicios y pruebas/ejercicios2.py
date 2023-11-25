# Ejercicio 2 - Herencias

# Ejercicio con herencia y uso de super:
# Crea un sistema para una escuela. En este sistema, vamos a tener dos clases principales: "Persona" y "Estudiante".
# La clase "Persona" tendrá los atributos de -nombre y -edad y un método que imprima el nombre y la edad de la persona.
# La clase "Estudiante" heredará de la clase "Persona" y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante.
# Deberás utilizar "super" en el método de inicialización (init) para reutilizar el código de la clase padre (Persona).
# Luego crea una instancia de la clase "Estudiante" e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.
# Ejercicio:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"El nombre es {self.nombre} y su edad es {self.edad}.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"El grado del estudiante {self.nombre} es: {self.grado}.")

abel = Estudiante("Abel","24","10mo")
abel.mostrar_datos()
abel.mostrar_grado()



# Ejercicio de herencia múltiple y MRO:
# Imagina que estás modelando animales en un zoológico. Crea tres clases: "Animal", "Mamifero" y "Ave".
# La clase "Animal" debe tener un método llamado "comer". La clase "Mamifero" debe tener un método "amamantar" y la clase "Ave" un método llamado "volar".
# Ahora crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", además de "comer".
# Finalmente, juega con el orden de herencia de la clase "Murcielago" y observa cómo cambia el MRO y el comportamiento de los métodos al usar super().
# Ejercicio:
class Animal:
    def comer(self):
        print("El animal está comiendo.")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando.")

class Ave(Animal):
    def volar(self):
        print("El animal está volando.")

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())
