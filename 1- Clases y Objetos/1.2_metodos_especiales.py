# --- METODOS ESPECIALES ---

# También conocidos como "métodos mágicos" o "métodos dunder" (del inglés, "double underscore methods").
# Son métodos especiales que tienen nombres que comienzan y terminan con doble guión bajo, por ejemplo, "__init__", "__str__", "__add__", etc.
# Estos métodos permiten que las clases definan comportamientos específicos para ciertas operaciones y acciones, lo que hace que las clases sean más flexibles y puedan interactuar con los operadores y funciones incorporados de Python de una manera personalizada.
# Puedes elegir los métodos que mejor se adapten a tus necesidades al diseñar tus clases personalizadas.


# Algunos de estos métodos son:

# __init__(self, ...):
# Este es uno de los métodos dunder más comunes.
# Se utiliza para inicializar un objeto de una clase cuando se crea una instancia de esa clase.
# Recibe argumentos que se utilizan para configurar los atributos del objeto.
class InitPersona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

personaInit = InitPersona("Abel", 24)
print(personaInit.name)  # "Abel"
print(personaInit.age)   # 24


# __str__(self):
# Define la representación en cadena de texto del objeto.
# Cuando imprimimos el objeto "StrPersona" utilizando "print()", Python llama automáticamente al método "__str__" y muestra la representación en cadena definida en el método.
# Esto permite que el objeto se imprima de una manera más informativa y legible para los humanos.
class StrPersona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Nombre: {self.name}, Edad: {self.age}."

personaStr = StrPersona("Jere", 22)
print(personaStr)  # "Nombre: Jere, Edad: 22"


# __repr__(self):
# Define una representación en cadena más detallada y útil del objeto.
# Se llama cuando se utiliza "repr()" para obtener una representación oficial del objeto.
# Esta representación suele ser útil para la depuración y para crear objetos similares si es necesario.
class ReprPersona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Persona('{self.name}', {self.age})"

persona = ReprPersona("Celeste", 21)
representacion = repr(persona)
print(representacion)  # "Persona('Celeste', 21)"


# __len__(self):
# Define el comportamiento de la función "len()" para objetos de la clase.
# Debe devolver la longitud o cantidad de elementos del objeto.
class LenLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

mi_lista = LenLista([1, 2, 3, 4, 5])
longitud = len(mi_lista)
print(longitud)  # 5, ya que la lista tiene 5 elementos


# __getitem__(self, key):
# Permite que los objetos de la clase sean indexables, como las listas o diccionarios.
# Recibe una clave como argumento y devuelve el valor correspondiente.
class GetitemDic:
    def __init__(self, datos):
        self.datos = datos

    def __getitem__(self, clave):
        return self.datos[clave]

mi_diccionario = GetitemDic({"clave1": "valor1", "clave2": "valor2"})

# Acceder a elementos del diccionario utilizando el método "__getitem__" utilizando la notación de corchetes [].
valor1 = mi_diccionario["clave1"]
valor2 = mi_diccionario["clave2"]
print(valor1)  # "valor1"
print(valor2)  # "valor2"


# __setitem__(self, key, value):
# Define el comportamiento de la asignación de valores a elementos indexables del objeto.
# Se llama cuando se utiliza "obj[key] = value" para asignar un valor a un elemento.
class SetitemListaMutable:
    def __init__(self):
        self.elementos = []

    def __setitem__(self, indice, valor):
        if indice < len(self.elementos):
            self.elementos[indice] = valor
        else:
            self.elementos.append(valor)

mi_lista = SetitemListaMutable()

# Asignar valores a elementos utilizando el método "__setitem__" utilizando la notación de corchetes [].
mi_lista[0] = 1
mi_lista[1] = 2
mi_lista[2] = 3
print(mi_lista.elementos)  # [1, 2, 3]


# __delitem__(self, key):
# Define el comportamiento de la eliminación de elementos indexables del objeto.
# Se llama cuando se utiliza "del obj[key]" para eliminar un elemento.
class DelitemListaMutable:
    def __init__(self):
        self.elementos = []

    def __delitem__(self, indice):
        if indice < len(self.elementos):
            del self.elementos[indice]
        else:
            raise IndexError("Índice fuera de rango")

mi_lista = DelitemListaMutable()

# Asignar valores a elementos utilizando el método "__setitem__".
mi_lista.elementos = [1, 2, 3, 4, 5]

# Eliminar elementos utilizando el método "__delitem__" utilizando la notación de corchetes [].
del mi_lista[0]
del mi_lista[1]
print(mi_lista.elementos)  # [2, 4, 5]


# __iter__(self) y __next__(self):
# "__iter__" define un iterador para el objeto.
# Este método permite que el objeto sea iterable, lo que significa que se puede utilizar en bucles "for".
# Y "__next__" define el comportamiento de la función "next()" para obtener el siguiente elemento en un bucle "for" que itera sobre el objeto.
# El método "__next__" devuelve los valores del rango desde "inicio" hasta "fin".
class IterCount:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio <= self.fin:
            valor_actual = self.inicio
            self.inicio += 1
            return valor_actual
        else:
            raise StopIteration

contador = IterCount(1, 5)

# Iterar sobre el objeto utilizando un bucle "for".
for numero in contador:
    print(numero)   # 1, 2, 3, 4, 5

# Obtener el siguiente elemento utilizando "next()".
try:
    while True:
        numero = next(contador)
        print(numero)
except StopIteration:
    pass


# __contains__(self, item):
# Define el comportamiento de la palabra clave "in" para verificar si un elemento está presente en el objeto.
# Esto permite que los objetos de la clase sean utilizados con la palabra clave "in" de manera similar a las listas o secuencias estándar para comprobar la pertenencia de elementos.
# Se llama cuando se utiliza "item in obj".
class ListaCountains:
    def __init__(self, elementos):
        self.elementos = elementos

    def __contains__(self, elemento):
        return elemento in self.elementos

mi_lista = ListaCountains([1, 2, 3, 4, 5])

# Verificar si un elemento está presente utilizando la palabra clave 'in'.
resultado = 3 in mi_lista
print(resultado)  # True, ya que 3 está en la lista
resultado = 6 in mi_lista
print(resultado)  # False, ya que 6 no está en la lista


# __eq__(self, other):
# Define el comportamiento del operador de igualdad "==" para objetos de la clase.
# Se llama cuando se utiliza "obj1 == obj2" para comparar dos objetos.
class PersonaEq:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otro):
        if isinstance(otro, PersonaEq):
            return self.nombre == otro.nombre and self.edad == otro.edad
        return False

persona1 = PersonaEq("Tonto", 24)
persona2 = PersonaEq("Tonta", 21)
persona3 = PersonaEq("Tonto", 24)

# Comparar objetos utilizando el operador de igualdad '=='.
resultado1 = persona1 == persona2
resultado2 = persona1 == persona3
print(resultado1)  # False, nombres y edades diferentes
print(resultado2)  # True, nombres y edades iguales


# __ne__(self, other):
# Define el comportamiento del operador de desigualdad "!=" para objetos de la clase.
# Se llama cuando se utiliza "obj1 != obj2" para verificar si dos objetos son diferentes.
class PersonaNe:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __ne__(self, otro):
        if isinstance(otro, PersonaNe):
            return not (self.nombre == otro.nombre and self.edad == otro.edad)
        return True

persona1 = PersonaNe("Tonta", 21)
persona2 = PersonaNe("Tonto", 24)
persona3 = PersonaNe("Tonta", 21)

# Comparar objetos utilizando el operador de desigualdad '!='.
resultado1 = persona1 != persona2
resultado2 = persona1 != persona3
print(resultado1)   # True, nombres y edades diferentes
print(resultado2)   # False, nombres y edades iguales


# __lt__(self, other):
# Define el comportamiento del operador de menor que "<" para objetos de la clase.
# Se llama cuando se utiliza "obj1 < obj2" para comparar dos objetos.
class PersonaLt:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, otro):
        if isinstance(otro, PersonaLt):
            return self.edad < otro.edad
        return False

persona1 = PersonaLt("Cristian", 27)
persona2 = PersonaLt("Abel", 24)
persona3 = PersonaLt("Benja", 29)

# Comparar objetos utilizando el operador de menor que '<'.
resultado1 = persona1 < persona2
resultado2 = persona2 < persona3
print(resultado1)   # False, persona1 es mayor que persona2
print(resultado2)   # True, persona2 es menor que persona3


# __le__(self, other):
# Define el comportamiento del operador de menor o igual que "<=" para objetos de la clase.
# Se llama cuando se utiliza "obj1 <= obj2" para comparar dos objetos.
class PersonaLe:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __le__(self, otro):
        if isinstance(otro, PersonaLe):
            return self.edad <= otro.edad
        return False

persona1 = PersonaLe("X", 30)
persona2 = PersonaLe("Y", 25)
persona3 = PersonaLe("Z", 30)

# Comparar objetos utilizando el operador de menor o igual que '<='.
resultado1 = persona1 <= persona2
resultado2 = persona1 <= persona3
print(resultado1)   # False, persona1 es mayor que persona2
print(resultado2)   # True, persona1 es igual en edad a persona3


# __gt__(self, other):
# Define el comportamiento del operador de mayor que ">" para objetos de la clase.
# Se llama cuando se utiliza "obj1 > obj2" para comparar dos objetos.
class PersonaGt:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __gt__(self, otro):
        if isinstance(otro, PersonaGt):
            return self.edad > otro.edad
        return False

persona1 = PersonaGt("Y", 30)
persona2 = PersonaGt("X", 35)
persona3 = PersonaGt("Z", 30)

# Comparar objetos utilizando el operador de mayor que '>'.
resultado1 = persona1 > persona2
resultado2 = persona2 > persona3
print(resultado1)   # False, persona1 es menor que persona2
print(resultado2)   # True, persona2 es mayor que persona3


# __ge__(self, other):
# Define el comportamiento del operador de mayor o igual que ">=" para objetos de la clase.
# Se llama cuando se utiliza "obj1 >= obj2" para comparar dos objetos.
class PersonaGe:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __ge__(self, otro):
        if isinstance(otro, PersonaGe):
            return self.edad >= otro.edad
        return False

persona1 = PersonaGe("X", 30)
persona2 = PersonaGe("Z", 30)
persona3 = PersonaGe("Y", 25)

# Comparar objetos utilizando el operador de mayor o igual que '>='.
resultado1 = persona1 >= persona2
resultado2 = persona2 >= persona3
print(resultado1)   # True, persona1 es igual en edad a persona2
print(resultado2)   # True, persona2 es mayor o igual en edad a persona3
