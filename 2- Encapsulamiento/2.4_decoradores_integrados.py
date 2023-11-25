# --- DECORADORES INTEGRADOS ---

# Python proporciona algunos decoradores integrados que te permiten controlar el acceso y la manipulación de atributos de una clase en el contexto de la POO.
# Estos decoradores son útiles para mantener la encapsulación de datos y proporcionar una interfaz controlada para acceder y modificar atributos de un objeto.

# "@property"
# Es un decorador que se coloca antes de un método en una clase para convertirlo en un método de acceso a un atributo.
# Esto significa que puedes acceder a este método como si fuera un atributo, en lugar de una función.
# El método decorado con "@property" se llama cuando intentas acceder al atributo correspondiente.
# Usar "@property" es útil cuando deseas realizar alguna lógica o validación antes de devolver el valor del atributo.

# "@setter"
# Es un decorador que se coloca antes de un método que se utilizará para asignar un valor a un atributo.
# El método decorado con "@setter" se llama cuando intentas asignar un valor al atributo correspondiente.
# Esto permite que tengas un mayor control sobre la forma en que se establecen los valores en tus atributos y, si es necesario, realizar validaciones.

# "@getter"
# Es un decorador que se coloca antes de un método que se utilizará para obtener el valor de un atributo.
# Aunque Python no requiere "@getter" como en otros lenguajes de programación, puedes usarlo para indicar de manera explícita que el método es un getter.

# "@deleter"
# Es un decorador que se coloca antes de un método que se utilizará para eliminar un atributo.
# El método decorado con "@deleter" se llama cuando intentas eliminar el atributo correspondiente.
# Esto te permite realizar operaciones personalizadas cuando se elimina un atributo, como la liberación de recursos.

# Ejemplo de ellos juntos:
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        print("Obteniendo nombre")
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        print("Cambiando nombre")
        self._nombre = nuevo_nombre

    @nombre.deleter
    def nombre(self):
        print("Eliminando nombre")
        del self._nombre

    @property
    def edad(self):
        print("Obteniendo edad")
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            print("Cambiando edad")
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

    @edad.deleter
    def edad(self):
        print("Eliminando edad")
        del self._edad

persona = Persona("Abel", 24)


print(persona.nombre)    # Acceder al nombre usando el getter
persona.nombre = "Jere"  # Cambiar el nombre usando el setter
del persona.nombre       # Eliminar el nombre usando el deleter
persona.edad = -5        # Intentar asignar una edad negativa
persona.edad = 22        # Cambiar la edad usando el setter
print(persona.edad)      # Acceder a la edad usando el getter
del persona.edad         # Eliminar la edad usando el deleter

# En este ejemplo, la clase "Persona" tiene dos atributos, "nombre" y "edad", y utiliza los decoradores "@property", "@setter", y "@deleter" para controlar el acceso y la modificación de estos atributos.
# Cada uno de estos decoradores permite realizar operaciones personalizadas cuando se accede, se modifica o se elimina un atributo, proporcionando un alto grado de encapsulación y control sobre los datos de la clase.



# Luego tenemos otros decoradores integrados por Python:

# "@staticmethod"
# Es un decorador en Python que se utiliza para definir métodos estáticos en una clase.
# Un método estático es un método que pertenece a la clase en lugar de una instancia particular de la clase.
# Esto significa que puedes llamar a un método estático directamente en la clase sin crear una instancia de la misma.
# Los métodos estáticos no tienen acceso a los atributos ni al estado interno de una instancia de clase, ya que no toman un argumento "self" como los métodos de instancia regulares.
# En su lugar, operan en función de los argumentos que se les pasan y otros valores que pueden estar disponibles en la clase.
# Para definir un método estático en una clase, se usa el decorador "@staticmethod" antes de la definición del método.
class Matematicas:
    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

resultado_suma = Matematicas.suma(5, 3)
resultado_resta = Matematicas.resta(10, 4)
print("Suma:", resultado_suma)    # Salida: Suma: 8
print("Resta:", resultado_resta)  # Salida: Resta: 6

# En este ejemplo, hemos creado una clase Matematicas con dos métodos estáticos: "suma" y "resta".
# Puedes llamar a estos métodos directamente en la clase sin crear una instancia de "Matematicas"

# Los métodos estáticos son útiles cuando tienes una funcionalidad que está relacionada con una clase pero no depende del estado de ninguna instancia particular de esa clase.
# Pueden ser convenientes para organizar el código y proporcionar utilidades relacionadas con la clase.


# "@classmethod"
# Se utiliza para definir métodos de clase en una clase.
# Los métodos de clase son aquellos que están asociados con la clase en lugar de con una instancia específica de la misma.
# Estos métodos pueden acceder y modificar atributos de la clase, pero no tienen acceso a los atributos específicos de una instancia en particular, ya que no toman un argumento "self" como los métodos de instancia regulares.
# En cambio, los métodos de clase toman un argumento especial llamado "cls", que se refiere a la propia clase.
# El uso de métodos de clase es útil cuando quieres realizar operaciones que están relacionadas con la clase en sí misma, en lugar de con instancias individuales de la clase.
# También son útiles para crear constructores alternativos o fábricas de objetos relacionados con la clase.
# Para definir un método de clase en una clase, se utiliza el decorador "@classmethod" antes de la definición del método.
class MiClaseM:
    contador = 0  # Atributo de clase

    def __init__(self, valor):
        self.valor = valor
        MiClaseM.contador += 1

    @classmethod
    def obtener_contador(cls):
        return cls.contador

objeto1 = MiClaseM(10)
objeto2 = MiClaseM(20)
contador = MiClaseM.obtener_contador()
print("Número de instancias creadas:", contador)  # Salida: Número de instancias creadas: 2

# En este ejemplo, hemos creado una clase "MiClaseM" con un método de clase llamado "obtener_contador".
# Este método puede acceder al atributo de clase "contador", que lleva el registro del número de instancias de la clase creadas.
# Hemos creado dos instancias de "MiClaseM" y luego llamado al método de clase "obtener_contador" para obtener el número total de instancias creadas.


# Tambien estan los decoradores personalizados, que serían los decoradores hechos por el usuario (TEMA POR APRENDER)}
