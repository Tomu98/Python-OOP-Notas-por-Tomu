# --- MRO ---

# "Method Resolution Order" o "Orden de Resolución de Métodos".
# Se utiliza para determinar el orden en el que se buscan y ejecutan los métodos de una clase en una jerarquía de herencia múltiple.
# La MRO es crucial para garantizar que los métodos se llamen en el orden correcto y que las clases derivadas hereden y sobrescriban correctamente los métodos de las clases base.

# Problema de la Ambigüedad
# Cuando una subclase hereda de múltiples superclases, puede surgir un problema de ambigüedad si ambas superclases tienen un método con el mismo nombre.
# Aquí es donde entra en juego la MRO para resolver este conflicto.

# El C3 Linearization Algorithm
# Python utiliza el algoritmo de linearización C3 para calcular la MRO.
# Este algoritmo sigue un conjunto de reglas para determinar el orden en el que se buscan los métodos en la jerarquía de clases.
# Las reglas son las siguientes:
# - Depth-First Search (DFS): El algoritmo sigue una estrategia de búsqueda en profundidad para recorrer la jerarquía de clases.
#   Esto significa que primero busca en la clase actual antes de pasar a las superclases.
# - Left-to-Right: Si una subclase hereda de varias superclases, se mantiene el orden en el que se mencionaron las superclases en la declaración de la subclase.
#   Python sigue este orden al calcular la MRO.
# - Consistencia: El algoritmo C3 garantiza que el orden de resolución sea consistente y no dependa de la forma en que se definieron las clases.

# Ejemplo para ilustrar MRO:
class A:
    def saludar(self):
        print("Hola desde A")

class B(A):
    def saludar(self):
        print("Hola desde B")

class C(A):
    def saludar(self):
        print("Hola desde C")

class D(B, C):
    pass

# En este ejemplo, tenemos cuatro clases: A, B, C y D. Las clases B y C heredan de A, y la clase D hereda de ambas B y C.
# Ahora, creemos una instancia de la clase D y llamemos al método "saludar()":

obj = D()
obj.saludar()   # Saldrá "Hola desde B"

# Aunque la clase D hereda de ambas B y C, el MRO garantiza que Python busque el método "saludar()" primero en la clase B debido a la regla de "Left-to-Right".
# Esto significa que el método "saludar()" de la clase B se ejecuta en lugar del método foo de la clase C o A.



# Método "super()" y la MRO
# El uso de "super()" en una subclase permite llamar al método de la superclase en lugar del propio método de la subclase.
# Cuando se utiliza "super()", Python se basa en la MRO para determinar cuál es la superclase y cuál es el método a ejecutar.
class Aa:
    def saludo(self):
        print("Método saludo de Aa")

class Bb(Aa):
    def saludo(self):
        super().saludo()
        print("Método saludo de Bb")

class Cc(Aa):
    def saludo(self):
        super().saludo()
        print("Método saludo de Cc")

class Dd(Bb, Cc):
    pass

d = Dd()
d.saludo()

# En este ejemplo, la clase D hereda de B y C, ambas de A.
# Cuando llamamos a "d.saludo()", Python sigue la MRO y ejecuta primero el método "saludo" de A utilizando "super()", luego ejecuta el método saludo de C (también utilizando "super()"), y finalmente ejecuta el método saludo de B.


# En algunos casos, puede ocurrir un conflicto en la MRO, especialmente cuando hay ambigüedad en la jerarquía de clases.
# Cuando esto sucede, Python generará un error de tipo "TypeError" para evitar comportamientos ambiguos.



# "mro()"
# El método mro() es un método que se puede llamar en una clase en Python para obtener la lista de la secuencia de la MRO.
# Devuelve una tupla que muestra el orden exacto en el que se buscarán los métodos en la jerarquía de clases.
# Ejemplo:
mro_result1 = D.mro()
print(mro_result1)
# Saldrá: "[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]"
# En este ejemplo, la tupla muestra el orden de resolución de métodos para la clase "D". 
# Python buscará métodos en "D", luego en "B", luego en "C", luego en "A", y finalmente en la clase base "object".

# "__mro__"
# Es un atributo especial en Python que está presente en todas las clases y es una representación más directa de la MRO de una clase.
# En lugar de llamar al método "mro()", puedes acceder al atributo "__mro__" directamente desde la clase.
mro_result2 = D.__mro__
print(mro_result2)
# Saldrá lo mismo que el anterior ejemplo:
# "(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)"

# Tanto "mro()" como "__mro__" proporcionan información sobre el orden de resolución de métodos para una clase y su jerarquía de clases.
# "mro()" es un método que devuelve una lista, mientras que "__mro__" es un atributo que almacena la misma información de manera más directa.
# Estos son útiles para comprender cómo Python resuelve los métodos en la jerarquía de clases y para solucionar problemas relacionados con la herencia y la ambigüedad en la resolución de métodos.


# Conclusiones
# La MRO (Method Resolution Order) es un concepto fundamental en Python que resuelve el problema de la ambigüedad cuando una subclase hereda de múltiples superclases.
# Python utiliza el algoritmo de linearización C3 para calcular el orden en el que se buscan los métodos en la jerarquía de clases.
# Esto asegura un comportamiento consistente y predecible en la resolución de métodos, lo que es esencial para POO en Python.
