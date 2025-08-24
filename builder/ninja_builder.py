from modelo.ninja import Ninja
from modelo.estadisticas import Estadisticas
from modelo.jutsu import Jutsu

class NinjaBuilder:
    def __init__(self):
        self.nombre = None
        self.rango = "Genin"
        self.aldea = None
        self.estadisticas = Estadisticas()
        self.jutsus = []

    def set_nombre(self, nombre):
        self.nombre = nombre
        return self

    def set_rango(self, rango):
        self.rango = rango
        return self

    def set_aldea(self, aldea):
        self.aldea = aldea
        return self

    def set_estadisticas(self, ataque, defensa, chakra):
        self.estadisticas = Estadisticas(ataque, defensa, chakra)
        return self

    def add_jutsu(self, nombre, tipo, poder):
        self.jutsus.append(Jutsu(nombre, tipo, poder))
        return self

    def build(self):
        if not self.nombre:
            raise ValueError("El ninja debe tener un nombre")
        return Ninja(
            nombre=self.nombre,
            rango=self.rango,
            aldea=self.aldea,
            estadisticas=self.estadisticas,
            jutsus=self.jutsus
        )
