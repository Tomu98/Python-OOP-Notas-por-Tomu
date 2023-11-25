# Clases

# En POO, una clase es una plantilla o un plano para crear objetos.
# Los objetos son instancias de una clase, y la clase define las propiedades (atributos) y los comportamientos (métodos) que los objetos de esa clase tendrán.
# Las clases permiten organizar y estructurar el código de manera más modular y reutilizable.


# "class"
# Para crear una clase se utiliza "class" seguido del nombre de la clase.
# Para nombrar las clases se utiliza la convención "Pascal Case".
# El contenido de la clase está indentado y puede incluir atributos y métodos.
# La sintaxis para definir una clase es la siguiente:

class MiClase:  # Aquí estamos definiendo una nueva clase llamada "MiClase".
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1  # Atributo 1
        self.atributo2 = parametro2  # Atributo 2

    def metodo1(self):   # Método 1
        # Código del método 1
        pass

    def metodo2(self):   # Método 2
        # Código del método 2
        pass


# Objetos
# En POO, un "objeto" es una instancia concreta o un ejemplar de una clase.
# Cuando creamos un objeto (instancia) estamos utilizando la "plantilla" que definimos en la clase.
# Es una instancia específica con sus propias características únicas.
# Cada objeto tiene sus propios atributos (propiedades o datos) y métodos (acciones o funciones) que puede realizar.
# Estos atributos y métodos se heredan de la clase, pero pueden tener valores específicos para cada objeto.
# Al crear un objeto lo guardamos en una varible y luego colocamos sus atributos en la clase que utilizamos.

# Atributos
# Son variables que pertenecen a una clase u objeto y representan las características o propiedades de ese objeto.
# Pueden ser variables de cualquier tipo de datos (números, cadenas, listas u otros objetos).
# Los atributos dentro de la clase son atributos estaticos, se pueden cambiar por fuera pero es más tedioso si tenemos muchos objetos.
# Se acceden utilizando la notación de punto (objeto.atributo).

# Métodos
# Son funciones que están definidas en una clase y representan el comportamiento o las acciones que un objeto de esa clase puede realizar.
# Pueden recibir argumentos, incluyendo principalmente el "self".
# Los métodos pueden acceder y modificar los atributos de un objeto y realizar diversas operaciones.
# Se invocan utilizando la notación de punto y el parentesis (objeto.metodo()).

# Ejemplo:
class AtributoPersona:       
    def __init__(self, nombre, edad):   # Parámetros
        self.nombre = nombre   # Atributo nombre
        self.edad = edad       # Atributo edad

    def saludar(self):   # Método que ejecuta un saludo
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona1 = AtributoPersona("Abel", 24)  # Instancia (objeto) creado de la clase
print(persona1.nombre)   # Accediendo al atributo nombre de persona1
persona1.saludar()       # Llamando al método saludar() en persona1


# "__init__"
# Es un método "constructor" especial en Python que se llama automáticamente cuando creas un nuevo objeto (instancia) de una clase.
# Su objetivo principal es inicializar los atributos del objeto con valores específicos cuando se crea.

# Imagina que estás construyendo una casa.
# El constructor "__init__" es como el momento en el que se coloca la primera piedra y se establece el diseño inicial de la casa.
# En este momento, puedes asignar valores iniciales a las características de la casa, como el número de habitaciones, el color de las paredes, etc.
class InitCasa:
    def __init__(self, habitaciones, color_paredes):
        self.habitaciones = habitaciones
        self.color_paredes = color_paredes

mi_casa = InitCasa(3, "azul")
print(mi_casa.habitaciones)   # Imprime 3

# Cuando creas una instancia de la clase "InitCasa", el método "__init__" se ejecuta automáticamente y establece los valores iniciales de "habitaciones" y "color_paredes".
# En este caso, "mi_casa" es un objeto (instancia) de la clase "InitCasa", y los valores iniciales de "habitaciones" y "color_paredes" se establecen en "3" y "azul", gracias al constructor "__init__".


# "Self"
# Se refiere al primer parámetro de un método de una clase, y se utiliza para hacer referencia a la instancia actual de la clase.
# Cuando defines métodos en una clase, generalmente el primer parámetro que reciben es self.
# Por ejemplo, en el método "__init__" de una clase (el constructor), "self" se refiere al objeto que se está creando.
# Permite diferenciar entre las variables locales y los atributos del objeto (que existen durante toda la vida del objeto).
# Ejemplo:
class Self:
    def __init__(self, valor):
        self.valor = valor

    def obtener_valor(self):
        return self.valor

objeto = Self(42)
print(objeto.obtener_valor())  # Imprime 42

# En este ejemplo, "self" se utiliza dentro de los métodos "__init__" y "obtener_valor" para acceder a los atributos del objeto actual (self.valor) y realizar operaciones en él.
# Cuando llamas a un método en una instancia de una clase, Python automáticamente pasa el objeto en sí como el primer argumento (self), lo que te permite acceder y modificar sus atributos.


# Ejemplo de una fabrica de celulares:
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")

celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 Pro","96MP")

print(celular1.marca)
print(celular2.marca)

celular1.llamar()
celular2.cortar()
