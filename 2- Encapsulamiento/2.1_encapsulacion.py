# --- ENCAPSULACIÓN ---


# Es la capacidad de una clase de ocultar sus detalles internos (atributos y métodos) y exponer una interfaz pública bien definida para interactuar con los objetos de esa clase.
# El encapsulamiento se logra mediante el uso de atributos y métodos de acceso.

# La encapsulación tiene varios objetivos importantes.
# - Ocultamiento de la complejidad: Permite ocultar los detalles de implementación de una clase, lo que facilita el uso de la clase sin preocuparse por cómo funciona internamente.
# - Protección de datos: Evita que los datos de un objeto se modifiquen directamente desde fuera de la clase sin un control adecuado.
# - Facilita el mantenimiento del código: Si los detalles internos de una clase cambian, los cambios solo deben realizarse en la clase, sin afectar el código que utiliza objetos de esa clase.
# - Fomenta el principio de "bajo acoplamiento": Reduce la dependencia entre las clases, ya que una clase no necesita conocer los detalles internos de otra clase para interactuar con ella.

# Atributos protegidos con un guión bajo ( _ ):
# Al utilizar un guión bajo al principio de un atributo (por ejemplo, _nombre), se indica que el atributo es considerado "protegido".
# El atributo sigue siendo accesible desde fuera de la clase, se supone que los desarrolladores no deben modificarlo directamente.

# Atributos privados con dos guiones bajos ( __ ):
# Al utilizar dos guiones bajos al principio de un atributo (por ejemplo, __edad), se indica que el atributo es "privado".
# Con eso se aplica un mecanismo de "name mangling" para hacer que el nombre del atributo sea más difícil de acceder desde fuera de la clase.
# Esto no lo hace completamente inaccesible, pero hace que sea menos probable que se acceda accidentalmente.

# Ejemplos de ambos atributos:
class Private:
    def __init__(self):
        self._atributo_protector = 42        # Atributo protegido con un guión bajo
        self.__atributo_privado = "secreto"  # Atributo privado con dos guiones bajos

    def obtener_atributo_privado(self):
        return self.__atributo_privado

    def cambiar_atributo_privado(self, nuevo_valor):
        self.__atributo_privado = nuevo_valor

objeto = Private()

# Utilizar métodos de acceso para atributo privado
print(objeto.obtener_atributo_privado())  # secreto

# Modificar el atributo privado a través del método
objeto.cambiar_atributo_privado("nuevo_valor")
print(objeto.obtener_atributo_privado())  # nuevo_valor

# La encapsulación real depende de la responsabilidad del desarrollador para no acceder ni modificar directamente los atributos protegidos o privados desde fuera de la clase.
