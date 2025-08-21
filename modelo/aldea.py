class Aldea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ninjas = []

    def agregar_ninja(self, ninja):
        self.ninjas.append(ninja)
        print(f"El ninja {ninja.nombre} pertenece a la aldea {self.nombre}")

    def listar_ninjas(self):
        print(f"Ninjas de la aldea {self.nombre}")
        if not self.ninjas:
            print("No hay ninjas en esta aldea")
        for ninja in self.ninjas:
            print(f"Nombre: {ninja.nombre}")