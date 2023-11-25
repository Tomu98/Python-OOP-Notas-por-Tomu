# Lapices

class Lapiz:
    def __init__(self,marca,tamano,color):
        self.marca = marca
        self.tamano = tamano
        self.color = color

    def dibujar(self):
        return print(f"Dibujando con {self.color}.")

    def definicion(self):
        return print(f"Este lapiz {self.tamano} de color {self.color} es de la marca {self.marca}.")

lnegro = Lapiz("Faber","chico","negro")
lrojo = Lapiz("Faber","chico","Rojo")
lazul = Lapiz("LP","chico","azul")
lamarillo = Lapiz("Faber","grande","amarillo")
lverde = Lapiz("LP","grande","verde")
lnaranja = Lapiz("Faber","grande","naranja")



lamarillo.dibujar()
lnaranja.definicion()
