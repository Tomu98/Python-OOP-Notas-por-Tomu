class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")

n = input("Digame su nombre:\n")
e = input("Ahora su edad:\n")
g = input("Por ultimo, su grado:\n")

estudiante = Estudiante(n,e,g)

print(f"""
      DATOS DEL ESTUDIANTE:\n
      Nombre: {estudiante.nombre}
      Edad: {estudiante.edad}
      Grado: {estudiante.grado}\n
      """)

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
    elif estudiar.lower() == "terminar":
        break
        