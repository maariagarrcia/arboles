from ArbolBinarioOrdenado_Class import *
from Jugador_Class import *
from JugadoresList_Class import *


j1 = Jugador("Ronaldo", "Juventus", 35)
j2 = Jugador("Gabi", "Barcelona", 18)
j3 = Jugador("Messi", "PSG", 33)
j4 = Jugador("Mbappe", "PSG", 22)
j5 = Jugador("Benzema", "Madrid", 32)
j6 = Jugador("Tchouameni", "Madrid", 21)
j7 = Jugador("Pedri", "Barcelona", 18)

indice_por_nombre = ArbolBinarioOrdenado()
indice_por_nombre.insertar(j1.getNombre(), j1)
indice_por_nombre.insertar(j2.getNombre(), j2)
indice_por_nombre.insertar(j3.getNombre(), j3)
indice_por_nombre.insertar(j4.getNombre(), j4)
indice_por_nombre.insertar(j5.getNombre(), j5)
indice_por_nombre.insertar(j6.getNombre(), j6)
indice_por_nombre.insertar(j7.getNombre(), j7)

print("> MOSTRAR ARBOL POR NOMBRE")
print("  · Orden central ASCENDENTE")
# indice_por_nombre.mostrarTodoEnOrdenCentral()
print("")

indice_por_edad = ArbolBinarioOrdenado()
indice_por_edad.insertar(j1.getEdad(), j1)
indice_por_edad.insertar(j2.getEdad(), j2)
indice_por_edad.insertar(j3.getEdad(), j3)
indice_por_edad.insertar(j4.getEdad(), j4)
indice_por_edad.insertar(j5.getEdad(), j5)
indice_por_edad.insertar(j6.getEdad(), j6)
indice_por_edad.insertar(j7.getEdad(), j7)

print("> MOSTRAR ARBOL POR EDAD")
print("  · Orden Central ASCENDENTE")
print(JugadoresList(indice_por_edad.todoEnOrdenCentral()))
print()

print("> BUSCAR EN LOS INDICES")
print(JugadoresList(indice_por_nombre.buscar("Iniesta")))
print(JugadoresList(indice_por_nombre.buscar("Mbappe")))
print(JugadoresList(indice_por_edad.buscar(32)))
print(JugadoresList(indice_por_edad.buscar(18)))
print()
print("\nYa he terminado!!!")

