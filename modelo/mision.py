class Mision:
    def __init__(self, nombre, rango, recompensa, requisito_rango):
        self.nombre = nombre
        self.rango = rango 
        self.recompensa = recompensa
        self.requisito_rango = requisito_rango

    def detalles_mision(self):
        return f"{self.nombre} (Rango {self.rango}) - Recompensa: {self.recompensa} ryō"

    def disponible_para(self, ninja):
        """Ninja misión según su rango"""
        if ninja.rango == "Kage":
            return True  
        elif ninja.rango == "Jōnin":
            return self.requisito_rango in ["Genin", "Chūnin", "Jōnin"]
        elif ninja.rango == "Chūnin":
            return self.requisito_rango in ["Genin", "Chūnin"]
        elif ninja.rango == "Genin":
            return self.requisito_rango == "Genin"
        else:
            return False
        
    def accept(self, visitor):
        visitor.visit_mision(self)

#mision_D = Mision("Recolectar hierbas", "D", 500, "Genin")
#mision_A = Mision("Proteger al una princesa", "A", 5000, "Jounin")

#print(mision_D.detalles_mision())
#print(mision_A.detalles_mision())