from modelo.estadisticas import Estadisticas
from modelo.jutsu import Jutsu

class Ninja:
    def __init__(self,nombre,rango,aldea=None,estadisticas=None,jutsus=None):
        self.nombre = nombre
        self.rango = rango
        self.aldea = aldea
        self.estadisticas = estadisticas if estadisticas else Estadisticas()
        self.jutsus = jutsus if jutsus else []

    def entrenar(self):
        if self.rango == "Genin":
            self.estadisticas.mejorar(1, 1, 2)
        elif self.rango == "Chūnin":
            self.estadisticas.mejorar(2, 2, 3)
        elif self.rango == "Jōnin":
            self.estadisticas.mejorar(3, 3, 4)
        elif self.rango == "Kage":
            self.estadisticas.mejorar(4, 4, 5)

    def evaluar_rango(self):
        total = self.estadisticas.total()
        if total >= 180 and self.rango != "Kage":
            self.rango = "Kage"
        elif total >= 120 and self.rango != "Jōnin":
            self.rango = "Jōnin"
        elif total >= 60 and self.rango == "Genin":
            self.rango = "Chūnin"
        elif total < 60 and self.rango == "Chūnin":
            self.rango = "Genin"


    def combatir(self, enemigo):
        poder_self = self.estadisticas.total() + sum([j.poder for j in self.jutsus])
        poder_enemigo = enemigo.estadisticas.total() + sum([j.poder for j in enemigo.jutsus])

        if poder_self > poder_enemigo:
            return f"{self.nombre} gana contra {enemigo.nombre}"
        elif poder_enemigo > poder_self:
            return f"{enemigo.nombre} gana contra {self.nombre}"
        else:
            if self.estadisticas.chakra >= enemigo.estadisticas.chakra:
                return f"{self.nombre} gana contra {enemigo.nombre} (desempate por chakra)"
            else:
                return f"{enemigo.nombre} gana contra {self.nombre} (desempate por chakra)"

    def __str__(self):
        return f"Nombre: {self.nombre}, Rango: {self.rango}, Aldea: {self.aldea}, Estadisticas ( {self.estadisticas} )"
    
    def accept(self, visitor):
        visitor.visit_ninja(self)