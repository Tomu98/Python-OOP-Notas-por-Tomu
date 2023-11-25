# --- ENLACES ESTÁTICOS Y DINÁMICOS ---

# Son dos conceptos relacionados con la resolución de referencias a funciones o métodos en tiempo de compilación y en tiempo de ejecución en programación.

# Enlaces Estáticos
# Los enlaces estáticos se refieren a la resolución de referencias a funciones o métodos en tiempo de compilación.
# En otras palabras, el enlace se establece antes de que el programa se ejecute y no cambia durante la ejecución del programa.
# Esto significa que el compilador determina qué función o método se debe llamar en función de la declaración en tiempo de compilación.
# Ejemplo:
# Supongamos que tienes una clase "Calculadora" con un método "sumar" y un método "restar".
# Si en tiempo de compilación eliges llamar al método "sumar", eso se resolverá estáticamente y no cambiará durante la ejecución del programa.
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

calc = Calculadora()
resultado = calc.sumar(5, 3)  # El enlace a "sumar" se resuelve estáticamente.
# En este ejemplo, el enlace a "sumar" se establece en tiempo de compilación, ya que la decisión de qué método llamar se tomó cuando se escribió el código.
# El enlace a "sumar" no cambiará durante la ejecución del programa.

# Enlaces Dinámicos
# Los enlaces dinámicos se refieren a la resolución de referencias a funciones o métodos en tiempo de ejecución.
# En este caso, la decisión sobre qué función o método se debe llamar se toma durante la ejecución del programa, basándose en el tipo de objeto real en ese momento.
# Ejemplo:
# Supongamos que tienes una jerarquía de clases en la que varias clases implementan un método "mostrar_info".
# En tiempo de ejecución, puedes decidir qué método llamar basándote en el objeto con el que estás trabajando.
class Figura:
    def mostrar_info(self):
        return "Soy una figura"

class Circulo(Figura):
    def mostrar_info(self):
        return "Soy un circulo"

class Cuadrado(Figura):
    def mostrar_info(self):
        return "Soy un cuadrado"

# En tiempo de ejecución, decidimos qué método llamar.
figuras = [Circulo(), Cuadrado(), Figura()]

for figura in figuras:
    info = figura.mostrar_info() # El enlace a "mostrar_info" se resuelve dinámicamente.
    print(info)
# En este ejemplo, el enlace a "mostrar_info" se resuelve en tiempo de ejecución.
# El método que se llama depende del tipo real de cada objeto en el momento en que se ejecuta el búcle.


# Comparación entre Enlaces Estáticos y Enlaces Dinámicos
# Enlaces Estáticos:
# - Resuelto en tiempo de compilación.
# - Mayor eficiencia en términos de rendimiento.
# - Menos flexibilidad, ya que no se puede cambiar durante la ejecución.
# Enlaces Dinámicos:
# - Resuelto en tiempo de ejecución.
# - Mayor flexibilidad, ya que se adapta al tipo de objeto real.
# - Puede tener un ligero costo de rendimiento debido a la resolución en tiempo de ejecución.


# La elección entre enlaces estáticos y enlaces dinámicos depende de las necesidades y restricciones del programa.
# Los lenguajes de programación pueden ofrecer uno u otro, o una combinación de ambos, según su diseño y propósito.
