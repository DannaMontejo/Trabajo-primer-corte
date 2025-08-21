from modelo.ninja import Ninja
from modelo.jutsu import Jutsu

class NinjaFactory:
    def crear_ninja(self, nombre, rango):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class KonohaFactory(NinjaFactory):
    def crear_ninja(self, nombre, rango):
        ninja = Ninja(nombre, rango, 10, 8, 12, "Konoha")
        ninja.agregar_jutsu(Jutsu("Rasengan", "Ninjutsu", 20))
        return ninja

class SunaFactory(NinjaFactory):
    def crear_ninja(self, nombre, rango):
        ninja = Ninja(nombre, rango, 9, 10, 11, "Suna")
        ninja.agregar_jutsu(Jutsu("Arenas movedizas", "Ninjutsu", 18))
        return ninja

class KiriFactory(NinjaFactory):
    def crear_ninja(self, nombre, rango):
        ninja = Ninja(nombre, rango, 8, 11, 10, "Kiri")
        ninja.agregar_jutsu(Jutsu("Agua negra", "Olas fuertes", 22))
        return ninja