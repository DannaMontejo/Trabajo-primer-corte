class Estadisticas:
    def __init__(self, ataque=0, defensa=0, chakra=0):
        self.ataque = ataque
        self.defensa = defensa
        self.chakra = chakra

    def mejorar(self, atk=1, defn=1, ch=2):
        self.ataque += atk
        self.defensa += defn
        self.chakra += ch

    def total(self):
        return self.ataque + self.defensa + self.chakra

    def __str__(self):
        return f"Ataque: {self.ataque}, Defensa: {self.defensa}, Chakra: {self.chakra}"