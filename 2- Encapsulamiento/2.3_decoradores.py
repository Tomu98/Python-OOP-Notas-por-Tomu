# --- DECORADORES ---

# ¿Qué son los decoradores?.
# Un decorador es una función que toma otra función y extiende o modifica su comportamiento sin cambiar su código fuente.
# En esencia, un decorador permite "envolver" una función con otra función para agregar funcionalidad adicional.

# ¿Por qué usar decoradores?.
# Reutilización de código: Los decoradores permiten agregar funcionalidad común a múltiples funciones sin duplicar código.
# Separación de preocupaciones: Facilitan la organización del código al separar las preocupaciones específicas de una función.
# Legibilidad: Hacen que el código sea más legible al separar la funcionalidad adicional de la lógica principal de la función.
# Modularidad: Facilitan la adición y eliminación de funcionalidad sin afectar el código existente.


# Funciones anidadas.
# En Python, las funciones pueden definirse dentro de otras funciones.
# Esto es útil para crear funciones internas que no son accesibles desde fuera de la función contenedora.
def exterior():
    def interior():
        print("Función interna")
    interior()
exterior()  # Output: Función interna

# Retorno de funciones desde otras funciones.
# Las funciones pueden retornar otras funciones como resultado.
# Esto es esencial para comprender cómo funcionan los decoradores.
def crear_funcion():
    def nueva_funcion():
        return "¡Hola, soy una función!"
    return nueva_funcion

nueva = crear_funcion()
print(nueva())  # Output: ¡Hola, soy una función!


# Sintaxis de los Decoradores
# Un decorador es una función que toma una función como argumento y devuelve otra función.
# Se define utilizando la sintaxis "@nombre_del_decorador" justo encima de la función que se va a decorar.
# Definición del decorador
def decorador(funcion_a_decorar):
    def funcion_decorada():
        print("Antes de llamar a la función")
        funcion_a_decorar()  # Llamamos a la función original
        print("Después de llamar a la función")
    return funcion_decorada

# Uso del decorador
@decorador
def funcion_original():
    print("¡Hola, soy la función original!")

# Llamamos a la función decorada
funcion_original()

# En este ejemplo:
# "decorador" es el decorador que toma "funcion_a_decorar" como argumento.
# "funcion_decorada" es la función interna que envuelve a "funcion_a_decorar" y agrega funcionalidad adicional.
# "decorador" se aplica a la función "funcion_original", lo que significa que "funcion_original" se ejecutará a través de "decorador", mostrando mensajes antes y después de su ejecución.
