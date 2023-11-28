# POLIMORFISMO
# El término "polimorfismo" se deriva de las palabras griegas "poly" (muchos) y "morph" (forma).
# Se refiere a la capacidad de diferentes clases o tipos de objetos para responder a la misma interfaz o mensaje de una manera específica para cada clase.
# En otras palabras, se trata de la capacidad de objetos de diferentes tipos para realizar acciones similares, pero cada uno de ellos lo hace de manera única según su propia implementación.

# Ejemplo Simple de Polimorfismo:
class Perro:
    def hacer_sonido(self):
        print("Guau!")

class Gato:
    def hacer_sonido(self):
        print("Miau!")

chuchi = Perro()
gordo = Gato()

def haz_sonar(animal):
    animal.hacer_sonido()

haz_sonar(chuchi)  # Salida: Guau!
haz_sonar(gordo)   # Salida: Miau!

# Supongamos que tenemos dos clases: Perro y Gato. Ambas clases tienen un método llamado hacer_sonido() que imprime el sonido característico de cada animal.
# Aunque "chuchi" y "gordo" son de tipos diferentes, ambos tienen un método llamado "hacer_sonido()".


# Polimorfismo en Python
# El polimorfismo en Python se puede lograr de varias maneras diferentes:
# Polimorfismo de interfaz: se refiere a tener clases con métodos que tienen el mismo nombre pero diferentes implementaciones, como en el ejemplo de Perro y Gato.
# Polimorfismo de herencia: las clases derivadas (subclases) pueden reemplazar o extender métodos de las clases base (superclases). Esto se llama sobrescritura de métodos.
# Polimorfismo de operadores: Python permite sobrecargar operadores como +, -, *, etc., para que funcionen de manera diferente según el tipo de objetos involucrados.
# Polimorfismo paramétrico: Esto se logra mediante el uso de genéricos o clases paramétricas (como List[T] en el módulo typing), donde los tipos de datos se parametrizan y pueden adaptarse a diferentes tipos de datos.

# Beneficios del Polimorfismo.
# El polimorfismo proporciona varios beneficios en la programación orientada a objetos:
# Reutilización de código: permite que se pueda reutilizar código al tratar diferentes objetos de manera uniforme.
# Flexibilidad: facilita la extensión y modificación del código sin afectar otras partes del programa.
# Mantenibilidad: hace que el código sea más legible y fácil de mantener, ya que las acciones comunes se agrupan bajo una interfaz común.



# TIPO REAL Y TIPO DECLARADO

# Tipo Declarado (Declared Type):
# El "tipo declarado" se refiere al tipo de dato que se asigna a una variable o se declara para un objeto en el código fuente del programa.
# Es la información que proporcionas explícitamente al definir una variable o crear un objeto.
# El tipo declarado se establece en tiempo de compilación y se utiliza para verificar la corrección del código y para determinar qué operaciones y métodos son válidos para ese objeto en ese contexto.

# Ejemplos:
# Tipo declarado: int (entero)
numero = 42

# Tipo declarado: str (cadena de caracteres)
nombre = "Thorfinn"

# En estos ejemplos, el tipo declarado se establece explícitamente al asignar valores a las variables "numero" y "nombre".
# Esto ayuda al compilador o al intérprete a realizar comprobaciones estáticas y a garantizar que las operaciones posteriores se realicen de acuerdo con los tipos declarados.


# Tipo Real (Actual Type o Runtime Type):
# El "tipo real" (a veces llamado "tipo de tiempo de ejecución" o "actual type") se refiere al tipo de dato con el que realmente opera un objeto o variable en tiempo de ejecución, en contraste con el tipo declarado que se establece en tiempo de compilación.
# El tipo real se determina por la instancia o el valor que se asigna a una variable u objeto en un momento dado durante la ejecución del programa.

# Ejemplos:
def imprimir_tipo(objeto):
    print(f"Tipo declarado: {type(objeto).__name__}, Tipo real: {type(objeto).__name__}")

# Tipo declarado: int, Tipo real: int
numero = 42
imprimir_tipo(numero)

# Tipo declarado: str, Tipo real: str
nombre = "Alice"
imprimir_tipo(nombre)

# En este ejemplo, la función "imprimir_tipo()" muestra tanto el tipo declarado como el tipo real del objeto que se le pasa como argumento.
# Aunque las variables "numero" y "nombre" se declararon con tipos específicos, sus tipos reales coinciden con sus tipos declarados.
