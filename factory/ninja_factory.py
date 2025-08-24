from modelo.ninja import Ninja
from modelo.jutsu import Jutsu
from modelo.estadisticas import Estadisticas

class NinjaFactory:
    def crear_ninja(self, nombre, rango):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class KonohaFactory(NinjaFactory):
    def crear_ninja(self, nombre, rango):
        estadisticas = Estadisticas(ataque=10, defensa=8, chakra=12)
        jutsu = [Jutsu("Rasengan", "Ninjutsu", 20)]
        ninja = Ninja(nombre, rango,"Konoha", estadisticas,jutsu)
        return ninja

class SunaFactory(NinjaFactory):
    def crear_ninja(self, nombre, rango):
        estadisticas = Estadisticas(ataque=9, defensa=10, chakra=11)
        jutsu = [Jutsu("Arenas movedizas", "Ninjutsu", 18)]
        ninja = Ninja(nombre, rango,"Suna",estadisticas,jutsu)
        return ninja

class KiriFactory(NinjaFactory):
    def crear_ninja(self, nombre, rango):
        jutsu = [Jutsu("Agua negra", "Ninjutsu", 22)]
        estadisticas = Estadisticas(ataque=8, defensa=11, chakra=10)
        ninja = Ninja(nombre, rango, "Kiri",estadisticas,jutsu)
        return ninja