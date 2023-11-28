# DUCKTYPING
# "Duck Typing" es un concepto en programación que se relaciona con el polimorfismo y la flexibilidad de los lenguajes de programación dinámicos.
# Es un concepto en programación que se refiere a la forma en que se determina el tipo o la clase de un objeto en tiempo de ejecución en lugar de en tiempo de compilación.
# La idea fundamental del "Duck Typing" es que lo que importa no es la clase o el tipo específico de un objeto, sino si el objeto puede realizar ciertas operaciones o métodos.
# Se basa en el principio "Si parece un pato, nada como un pato y grazna como un pato, entonces probablemente es un pato".


# Principio de Duck Typing
# El enfoque se centra en el comportamiento de un objeto en lugar de su tipo declarado.
# Si un objeto se comporta de una manera particular (es decir, si responde a ciertos métodos o funciones), se considera válido para llevar a cabo una acción en lugar de basarse en su tipo o clase.
# Esto permite una mayor flexibilidad en la programación y fomenta la reutilización de código.

# Ejemplo
# Imaginemos que tenemos dos clases diferentes, "Pato" y "Avión", que tienen un método "hacer_sonido()".
# Queremos determinar si un objeto puede hacer un sonido y no nos importa su tipo real, solo su comportamiento.
class Pato:
    def hacer_sonido(self):
        print("Cuac cuac")

class Avion:
    def hacer_sonido(self):
        print("Zum zum")

# Función que usa Duck Typing
def hacer_un_sonido(objeto):
    objeto.hacer_sonido()

pato = Pato()
avion = Avion()

hacer_un_sonido(pato)  # Imprime "Cuac cuac"
hacer_un_sonido(avion) # Imprime "Zum zum"

# En este ejemplo, la función "hacer_un_sonido()" no se preocupa por el tipo de objeto que recibe.
# En su lugar, se enfoca en si el objeto tiene un método llamado "hacer_sonido()".
# Si lo tiene, se ejecutará sin importar si el objeto es un pato o un avión.


# Ventajas de Duck Typing
# Una de las ventajas es que permite que los objetos se utilicen en contextos diversos sin restricciones estrictas de tipo.
# También facilita la escritura de código genérico y reutilizable, ya que se basa en el comportamiento en lugar del tipo concreto.
# Y otra ventaja es que reduce la necesidad de conversiones explícitas de tipos y verifica automáticamente si un objeto es válido para una operación.

# Desventajas de Duck Typing
# Una desventaja es el P¿potencial para los errores en tiempo de ejecución, debido a que no se realiza una verificación de tipos estática, los errores relacionados con la falta de un método pueden ocurrir en tiempo de ejecución.
# Y otra es que puede ser menos obvio entender qué métodos debe tener un objeto basándose únicamente en su uso en lugar de una declaración de tipo explícita.
