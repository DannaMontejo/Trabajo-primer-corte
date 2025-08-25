from modelo.aldea import Aldea
from modelo.ninja import Ninja
from modelo.estadisticas import Estadisticas
from modelo.jutsu import Jutsu
from modelo.mision import Mision
from factory.ninja_factory import KonohaFactory, SunaFactory, KiriFactory
from builder.ninja_builder import NinjaBuilder
from visitor.export_visitor import ExportVisitor

# --- 1. Crear Aldea ---
konoha = Aldea("Konoha")

# --- 2. Crear Ninjas usando Factory y Builder ---
# Usamos el Factory para crear un ninja de Konoha con su configuración predeterminada
konoha_factory = KonohaFactory()
naruto = konoha_factory.crear_ninja("Naruto", "Genin")

# Usamos el Builder para crear un ninja personalizado
builder = NinjaBuilder()
sasuke = builder.set_nombre("Sasuke").set_rango("Genin").set_estadisticas(ataque=12, defensa=9, chakra=15).add_jutsu("Chidori", "Ninjutsu", 25).build()

# --- 3. Agregar Ninjas a la Aldea ---
konoha.agregar_ninja(naruto)
konoha.agregar_ninja(sasuke)

# --- 4. Mostrar listado de ninjas ---
konoha.listar_ninjas()

# --- 5. Entrenar a Naruto varias veces ---
print("\n--- ENTRENAMIENTO ---")
for i in range(10):  # entrenamos 10 veces
    naruto.entrenar()
    naruto.evaluar_rango()
print(naruto)

# --- 6. Simular combate ---
print("\n--- COMBATE ---")
print(naruto.combatir(sasuke))

# --- 7. Crear misiones ---
mision_D = Mision("Recolectar hierbas", "D", 500, "Genin")
mision_A = Mision("Proteger a la princesa", "A", 5000, "Jōnin")

print("\n--- MISIONES ---")
print(mision_D.detalles_mision(), "| Disponible para Naruto:", mision_D.disponible_para(naruto))
print(mision_A.detalles_mision(), "| Disponible para Naruto:", mision_A.disponible_para(naruto))

# --- 8. Implementar el visitor ---
visitor = ExportVisitor()
naruto.accept(visitor)
sasuke.accept(visitor)
mision_A.accept(visitor)
mision_D.accept(visitor)

print("\n--- EXPORTACIÓN DE DATOS ---")
#print(visitor.export())
visitor.export("informe.json")