# ENCAPSULACIÓN
# Es la capacidad de una clase de ocultar sus detalles internos (atributos y métodos) y exponer una interfaz pública bien definida para interactuar con los objetos de esa clase.
# El encapsulamiento se logra mediante el uso de atributos y métodos de acceso.

# La encapsulación tiene varios objetivos importantes:
# Una de ellas es ocultar los detalles de implementación de una clase, facilitando el uso de la clase sin preocuparse por cómo funciona internamente.
# Otro objetivo es evitar que los datos de un objeto se modifiquen directamente desde fuera de la clase sin un control adecuado.
# También facilita el mantenimiento del código, si los detalles internos de una clase cambian, los cambios solo deben realizarse en la clase, sin afectar el código que utiliza objetos de esa clase.
# Y por ultimo fomenta el principio de "bajo acoplamiento", que reduce la dependencia entre las clases, ya que una clase no necesita conocer los detalles internos de otra clase para interactuar con ella.



# Atributos protegidos con un guión bajo ( _atributo )
# Al utilizar un guión bajo al principio de un atributo (por ejemplo, _nombre), se indica que el atributo es considerado "protegido".
# En su lugar, se debe utilizar un método de acceso para obtener o modificar el valor del atributo.
# Esto es más una convención que una regla, ya que Python no impide que se acceda o modifique el atributo directamente, por lo que sigue siendo posible hacerlo.
# Sin embargo, si se utiliza un método de acceso, se puede agregar lógica adicional para controlar el acceso al atributo.

# Atributos privados con dos guiones bajos ( __atributo )
# Al utilizar dos guiones bajos al principio de un atributo (por ejemplo, __edad), se indica que el atributo es "privado".
# Con eso se aplica un mecanismo de "name mangling" para hacer que el nombre del atributo sea más difícil de acceder desde fuera de la clase.
# Esto no lo hace completamente inaccesible, pero hace que sea menos probable que se acceda accidentalmente.
# Al igual que con los atributos protegidos, se debe utilizar un método de acceso para obtener o modificar el valor del atributo.

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
# Sin embargo, si se hace, el uso de métodos de acceso facilita la tarea de modificar la clase en el futuro, ya que se puede agregar lógica adicional en los métodos de acceso para controlar el acceso a los atributos.
# Por ejemplo, se puede agregar una condición para verificar que el nuevo valor de un atributo sea válido antes de asignarlo.
# Si se accede directamente al atributo, no se puede agregar esta lógica adicional.
# Por lo tanto, es una buena práctica utilizar métodos de acceso para todos los atributos protegidos y privados, incluso si no se agrega lógica adicional en el momento.
# De esta manera, si se necesita agregar lógica adicional en el futuro, se puede hacer sin tener que modificar el código que utiliza la clase.
