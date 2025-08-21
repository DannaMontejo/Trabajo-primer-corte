class Jutsu:
    def __init__(self, nombre, tipo, poder):
        self.nombre = nombre
        self.tipo = tipo 
        self.poder = poder

    def __str__(self):
        return f"{self.nombre} [{self.tipo}] | Poder: {self.poder}"
    

#rasengan = Jutsu("Rasengan", "Ninjutsu", 20)
#kagebunshin = Jutsu("Kage Bunshin", "Taijutsu", 10)

#print(rasengan)
#print(kagebunshin)
