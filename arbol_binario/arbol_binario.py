from colorama  import Fore
from arbol_binario_ordenado import *
from clase_jugador  import  *
from JugadoresList_Class import *

#### INICIO  PROGRAMA PRINCIPAL ####

j1 = Jugador("Ronaldo", "Juventus", 35)

j2=  Jugador("Gavi", "Barcelona", 18)

j3=  Jugador("Messi", "PSG", 33)

j4=  Jugador("Mbappe", "PSG", 22)

j5 = Jugador("Benzema", "Real Madrid", 32)

j6 = Jugador("Tchouameni", "Real Madrid", 21)

j7=  Jugador("Pedri", "Barcelona", 18)

j8= Jugador(" Suarez", "Barcelona", 34)

j9 = Jugador("Modric", "Real Madrid", 36)

# ya se hace internamente vamos acrear un nodo
#  asi  se ordenara por  la clave nombre
#n1 = Nodo(j1._nombre, j1)
#print(n1)

indice_por_nombre= ArbolBinarioOrdenado()
# para insertar la clave y le pasamos el objeto jugador
indice_por_nombre.insertar(j1.get_nombre(),j1)
indice_por_nombre.insertar(j2.get_nombre(),j2)
indice_por_nombre.insertar(j3.get_nombre(),j3)
indice_por_nombre.insertar(j4.get_nombre(),j4)
indice_por_nombre.insertar(j5.get_nombre(),j5)
indice_por_nombre.insertar(j6.get_nombre(),j6)
indice_por_nombre.insertar(j7.get_nombre(),j7)
indice_por_nombre.insertar(j8.get_nombre(),j8)
indice_por_nombre.insertar(j9.get_nombre(),j9)

#print(Fore.YELLOW+">  MOSTRAR ARBOL POR NOMBRE  EN ORDEN CENTRAL (De  menos a mayor clave)"+Fore.WHITE)
#print(JugadoresList(indice_por_nombre.mostrar_todo_en_orden_central()))
#
#print()
#print(Fore.YELLOW+">  MOSTRAR ARBOL POR NOMBRE EN PREORDEN "+Fore.WHITE)
#indice_por_nombre.mostrar_todo_en_preorden()
#print()
#
#print(Fore.YELLOW+">  MOSTRAR ARBOL POR NOMBRE EN POSTORDEN "+Fore.WHITE)
#indice_por_nombre.mostrar_todo_en_postorden()
#
indice_por_edad = ArbolBinarioOrdenado()
## para insertar la clave y le pasamos el objeto jugador
indice_por_edad.insertar(j1.get_edad(),j1)
indice_por_edad.insertar(j2.get_edad(),j2)
indice_por_edad.insertar(j3.get_edad(),j3)
indice_por_edad.insertar(j4.get_edad(),j4)
indice_por_edad.insertar(j5.get_edad(),j5)
indice_por_edad.insertar(j6.get_edad(),j6)
indice_por_edad.insertar(j7.get_edad(),j7)
indice_por_edad.insertar(j8.get_edad(),j8)
indice_por_edad.insertar(j9.get_edad(),j9)
#

#print()
#print(Fore.YELLOW+">  MOSTRAR ARBOL POR EDAD  EN ORDEN CENTRAL (De  menos a mayor clave)"+Fore.WHITE)
#print(JugadoresList(indice_por_edad.mostrar_todo_en_orden_central()))
#
#print(Fore.YELLOW+">MOSTRAR ARBOL POR EDAD EN ORDEN CENTRAL  DESCENDENTE "+Fore.WHITE)
#print(JugadoresList(indice_por_edad.mostrar_todo_en_orden_central_descendente()))
#
#print()
#print(Fore.YELLOW+">  MOSTRAR ARBOL POR NOMBRE EN PREORDEN "+Fore.WHITE)
#print(JugadoresList(indice_por_edad.mostrar_todo_en_preorden()))
#
#print()
#print(Fore.YELLOW+">  MOSTRAR ARBOL POR NOMBRE EN POSTORDEN "+Fore.WHITE)
#print(JugadoresList(indice_por_edad.mostrar_todo_en_postorden()))
#
#print()
#
#print(Fore.YELLOW+"> BUSCAR POR NOMBRE"+Fore.WHITE)
#print(JugadoresList(indice_por_nombre.buscar("Iniesta")))
#print(JugadoresList(indice_por_nombre.buscar("Mbappe")))
## hacer los otros dos
#print()
#
#print(Fore.YELLOW+"> BUSCAR POR EDAD"+Fore.WHITE)
#print(JugadoresList(indice_por_edad.buscar(18)))
#
#print()
#print(Fore.YELLOW+"> Buscar recursivo por nombre: "+Fore.WHITE)
#print(JugadoresList(indice_por_nombre.buscar_todo_recursivo("Mbappe")))
#
#print()
##print(Fore.YELLOW+ "> Eliminar por nombre: "+Fore.WHITE)
##print(JugadoresList(indice_por_nombre.eliminar_nodo("Mbappe")))
##print(JugadoresList(indice_por_nombre.eliminar_nodo("Ronaldo")))
##
##print(JugadoresList(indice_por_nombre.buscar("Mbappe")))
##print(JugadoresList(indice_por_nombre.buscar("Ronaldo")))
#print()
print(JugadoresList(indice_por_edad.buscar(18)))
#
##print(Fore.YELLOW+ "Buscar maximo teniendo en cuenta  el actual:" +Fore.WHITE)
##nodo_messi,nodo_m_padre = indice_por_edad.buscar_NODO_todo_recursivo(33)
##nodo_tchoumeni,nodo_t_padre = indice_por_edad.buscar_NODO_todo_recursivo(21)
##print(Fore.CYAN+"NODO:",JugadoresList(nodo_messi.get_datos()),Fore.WHITE)
##print(Fore.CYAN+"NODO PADRE: ",JugadoresList(nodo_m_padre.get_datos()),Fore.WHITE)
##print()
##
##print(Fore.YELLOW+ "Buscar maximo sin tener en cuenta el actual: "+Fore.WHITE)
##nodo_max, nodo_max_padre = indice_por_edad.buscar_maximo(nodo_messi,nodo_m_padre)
##if nodo_max!= None:
##    print(nodo_max.get_clave())
##else:
##    print("No hay nodo mayor")
##
##if nodo_max_padre != None:
##    print(nodo_max_padre.get_clave())
##else:
##    print("No hay nodo mayor")
#
#
#print()
#print(Fore.YELLOW+"Eliminar nodo con dos hijos"+Fore.WHITE)
## se elimina en tods loos  casos  menos coon el  33 y la raiz
#print(indice_por_edad.eliminar_clave(33))
#print(JugadoresList(indice_por_edad.mostrar_todo_en_orden_central()))
#
#
##print(Fore.YELLOsW+"Eliminar nodo por edad"+Fore.WHITE)
##print(JugadoresList(indice_por_edad.eliminar_nodo(21)))
#print()
#print(Fore.GREEN+"YA  LO HE INSERTADO TODO"+Fore.WHITE)
#