# ISP - Interface Segregation Principle

# Principio de Segregación de Interfaces.
# El principio de segregación de interfaces establece que los clientes no deben depender de interfaces que no utilizan.
# En otras palabras, una clase no debe verse obligada a implementar métodos que no necesita.
# Esto promueve la creación de interfaces pequeñas y específicas que contienen solo los métodos necesarios para un conjunto particular de funcionalidades.

# Abajo un ejemplo cuando este principio no se cumple:
from abc import ABC, abstractmethod

# Interfaz única para todos los empleados
class Empleado(ABC):

    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def reportar_horas_trabajo(self):
        pass

    @abstractmethod
    def entregar_paquetes(self):
        pass

# Clase para los empleados de oficina
class EmpleadoOficina(Empleado):

    def calcular_salario(self):
        # Cálculo del salario para empleados de oficina
        pass

    def reportar_horas_trabajo(self):
        # Los empleados de oficina deben reportar sus horas de trabajo
        pass

    def entregar_paquetes(self):
        # ERROR: Los empleados de oficina no entregan paquetes
        pass

# Clase para los trabajadores de fábrica
class TrabajadorFabrica(Empleado):

    def calcular_salario(self):
        # Cálculo del salario para trabajadores de fábrica
        pass

    def reportar_horas_trabajo(self):
        # Los trabajadores de fábrica también deben reportar sus horas de trabajo
        pass

    def entregar_paquetes(self):
        # ERROR: Los trabajadores de fábrica no entregan paquetes
        pass

# Clase para los repartidores
class Repartidor(Empleado):

    def calcular_salario(self):
        # Cálculo del salario para repartidores
        pass

    def reportar_horas_trabajo(self):
        # Los repartidores deben reportar sus horas de trabajo
        pass

    def entregar_paquetes(self):
        # Función específica para los repartidores
        pass

# En este ejemplo, no hemos el principio ISP porque la interfaz "Empleado" contiene un método "entregar_paquetes", que es relevante solo para los repartidores.
# Las clases "EmpleadoOficina" y "TrabajadorFabrica" se ven obligadas a implementar un método que no es relevante para su función.



# Ejemplo que cumple con el ISP:
# Interfaz para empleados de oficina
class EmpleadoOficinaISP(ABC):

    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def reportar_horas_trabajo(self):
        pass

# Interfaz para trabajadores de fábrica
class TrabajadorFabricaISP(ABC):

    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def reportar_horas_trabajo(self):
        pass

# Interfaz para repartidores
class RepartidorISP(ABC):

    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def reportar_horas_trabajo(self):
        pass

    @abstractmethod
    def entregar_paquetes(self):
        pass

# Clases concretas que implementan las interfaces específicas
class EmpleadoOficinaConcretoISP(EmpleadoOficina):

    def calcular_salario(self):
        # Cálculo del salario para empleados de oficina
        pass

    def reportar_horas_trabajo(self):
        # Los empleados de oficina deben reportar sus horas de trabajo
        pass

class TrabajadorFabricaConcretoISP(TrabajadorFabrica):

    def calcular_salario(self):
        # Cálculo del salario para trabajadores de fábrica
        pass

    def reportar_horas_trabajo(self):
        # Los trabajadores de fábrica también deben reportar sus horas de trabajo
        pass

class RepartidorConcretoISP(Repartidor):

    def calcular_salario(self):
        # Cálculo del salario para repartidores
        pass

    def reportar_horas_trabajo(self):
        # Los repartidores deben reportar sus horas de trabajo
        pass

    def entregar_paquetes(self):
        # Función específica para los repartidores
        pass

# En este nuevo diseño, hemos creado interfaces específicas para cada tipo de empleado, y cada clase concreta implementa solo las interfaces relevantes para su función.
# Esto cumple con el Principio de Segregación de Interfaces y evita que las clases tengan que implementar métodos que no son aplicables a su contexto.
