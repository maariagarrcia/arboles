from arbol_balanceado import *
from clase_jugador import *
from jugadores_list import *

# inicializar
a = Nodo("A",["A"])
l = Nodo("L",["L"])
d = Nodo("D",["D"])
b = Nodo("B",["B"])


# armar el arbol

arbol=ArbolBalanceado()
arbol.insertar(a.get_clave(),a)
arbol.insertar(l.get_clave(),l)
arbol.insertar(d.get_clave(),d)
arbol.insertar(b.get_clave(),b)

# probar el arbol

print(">Moostrar ARBOL (orden central")

for nodo in arbol.mostrar_todo_en_orden_central():
    print("Nodo:",nodo.get_clave(),"Altura: ",nodo.altura())











