# --- HERENCIA MÚLTIPLE ---

# La herencia múltiple es un concepto en POO que permite que una clase derivada herede atributos y métodos de más de una clase base.
# Esto se logra al enumerar todas las clases base separadas por comas en la definición de la clase derivada.
# Ejemplo:
class Ave:
    def __init__(self, nombre):
        self.nombre = nombre

    def volar(self):
        print(f"{self.nombre} puede volar")

class Mamifero:
    def __init__(self, nombre):
        self.nombre = nombre

    def amamantar(self):
        print(f"{self.nombre} puede amamantar")

class Pinguino(Ave, Mamifero):
    def __init__(self, nombre):
        # Llamamos a los constructores de las clases base explícitamente
        Ave.__init__(self, nombre)
        Mamifero.__init__(self, nombre)

    def nadar(self):
        print(f"{self.nombre} puede nadar")

pinguino = Pinguino("Pingu")
pinguino.volar()      # Llama al método de la clase base Ave
pinguino.amamantar()  # Llama al método de la clase base Mamifero
pinguino.nadar()      # Llama al método de la clase Pinguino


# clase.__init__()
# Cuando tienes más de una clase base y deseas llamar explícitamente a los constructores de las clases base en lugar de usar super().__init__(), puedes hacerlo utilizando la sintaxis ClaseBase.__init__(self, ...).
# Es útil cuando deseas controlar específicamente cuál constructor de clase base llamar en una situación de herencia múltiple.
# Cuando usas ClaseBase.__init__(self, ...), debes pasar explícitamente self como el primer argumento, para que la instancia de la subclase se pase correctamente al constructor de la clase base.
# Esto es necesario para que la clase base pueda inicializar los atributos de la instancia correctamente.
class ClaseA:
    def __init__(self, parametro_a):
        self.parametro_a = parametro_a

class ClaseB:
    def __init__(self, parametro_b):
        self.parametro_b = parametro_b

class ClaseC(ClaseA, ClaseB):
    def __init__(self, parametro_a, parametro_b, parametro_c):
        ClaseA.__init__(self, parametro_a)  # Llama al constructor de ClaseA
        ClaseB.__init__(self, parametro_b)  # Llama al constructor de ClaseB
        self.parametro_c = parametro_c

objeto_c = ClaseC("A", "B", "C")

print(objeto_c.parametro_a)  # Imprime "A"
print(objeto_c.parametro_b)  # Imprime "B"
print(objeto_c.parametro_c)  # Imprime "C"
