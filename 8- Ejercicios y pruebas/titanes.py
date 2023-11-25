"""Titanes"""

class Titan:
    """Clase de los titanes"""
    def __init__(self,nombre, altura, poder, defensa):
        self.nombre = nombre
        self.altura = altura
        self.poder = poder
        self.defensa = defensa

    def ataque(self):
        print(f"¡El titan {self.nombre} está atacando con {self.poder}!.")

    def defender(self):
        print(f"El titán {self.nombre} se defiende con {self.defensa}.")

class Ackerman:
    """Clase de los Ackermans"""
    def __init__(self,nombre, edad, poder, defensa):
        self.nombre = nombre
        self.edad = edad
        self.poder = poder
        self.defensa = defensa

    def ataque(self):
        print(f"{self.nombre} está atacando con {self.poder}.")

    def defender(self):
        print(f"{self.nombre} se defiende con {self.defensa}")
