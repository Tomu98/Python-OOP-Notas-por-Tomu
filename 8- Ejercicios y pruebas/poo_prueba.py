# Se declara la clase vehiculo
class Vehiculo():

    pais_origen = "Alemania"

    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    def arrancar(self):
        print("El vehículo ha arrancado.")

    def detener(self):
        print("El vehículo está detenido.")
        
    def mostrar_info(self):
        print(f"Vehículo de color {self.color}. Con una longitud de {self.longitud_metros} metros. Tiene {self.ruedas} ruedas.\nEl país de origen es {self.pais_origen}.")


vehiculo_1 = Vehiculo("rojo", 4, 4)
vehiculo_2 = Vehiculo("negro", 8.25, 8)

vehiculo_1.mostrar_info()