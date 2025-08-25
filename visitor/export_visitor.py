import json
 
class ExportVisitor:
    def __init__(self):
        self.info = {"ninjas": [], "misiones": []}

    def visit_ninja(self, ninja):
        info_ninja = {
            "Nombre": ninja.nombre,
            "Rango" : ninja.rango,
            "Aldea" : ninja.aldea.nombre if ninja.aldea else None,
            "Estadisticas" : {
                "Ataque": ninja.estadisticas.ataque,
                "Defensa": ninja.estadisticas.defensa,
                "Chakra": ninja.estadisticas.chakra
            },
            "Jutsus": [{"Nombre": j.nombre, "Tipo": j.tipo, "Poder": j.poder} for j in ninja.jutsus]
        }
        self.info["ninjas"].append(info_ninja)

    def visit_mision(self, mision):
        info_mision = {
            "Nombre" : mision.nombre,
            "Rango" : mision.rango,
            "Recompensa" : mision.recompensa
            
        }
        self.info["misiones"].append(info_mision)

    #def export(self):
        #return json.dumps(self.info, indent=4)
    def export(self, ruta):
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(self.info, archivo, indent=4, ensure_ascii=False)
        print(f"Informe guardado en {ruta} ")