# OCP - Open/Closed Principle

# Principio de Abierto/Cerrado.
# El principio de abierto/cerrado establece que una entidad de software (clase, módulo o función) debe estar abierta para su extensión pero cerrada para su modificación.
# Esto significa que debes poder agregar nuevas funcionalidades a una clase sin modificar su código fuente existente.
# Para lograr esto, se suelen utilizar interfaces y herencia, permitiendo que las clases derivadas extiendan la funcionalidad de la clase base.

# Ejemplo:
# Supongamos que tienes una clase "Calculadora" que realiza operaciones matemáticas y quieres agregar una nueva operación, como la raíz cuadrada.
# En lugar de modificar la clase existente, puedes extenderla creando una nueva clase que herede de la clase base "Calculadora" y agregue la nueva funcionalidad.
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

# Extensión de la clase para agregar la operación de multiplicación
class CalculadoraAvanzada(Calculadora):
    def multiplicar(self, a, b):
        return a * b

# Extensión de la clase para agregar la operación de raíz cuadrada
class CalculadoraCientifica(Calculadora):
    def raiz_cuadrada(self, a):
        return a ** 0.5
