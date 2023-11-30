from monticulo_max_class import *
from colorama import Fore

def monticulo_max():
    m = MonticuloMax()

    m.insertar(2)
    m.insertar(19)
    m.insertar(36)
    m.insertar(17)
    m.insertar(25)
    m.insertar(3)
    m.insertar(7)
    m.insertar(1)
    m.insertar(92)

    print(Fore.YELLOW+ "Monticulo max :"+Fore.WHITE,m)

    m.eliminar(2) # Elimina el 19 que esta en la posicion 2
    print()
    print(Fore.YELLOW+ "Monticulo:"+Fore.WHITE,m)


    m.eliminar()
    print()
    print(Fore.YELLOW+ "Monticulo:"+Fore.WHITE,m)

def monticulo_min():
    m1=MonticuloMin()
    m1.insertar(2)
    m1.insertar(19)
    m1.insertar(36)
    m1.insertar(17)
    m1.insertar(25)
    m1.insertar(3)
    m1.insertar(7)
    m1.insertar(1)
    m1.insertar(92)


    print(Fore.YELLOW+ "Monticulo min:"+Fore.WHITE,m1)

    m1.eliminar(2) # Elimina el 19 que esta en la posicion 2
    print()
    print(Fore.YELLOW+ "Monticulo:"+Fore.WHITE,m1)


    m1.eliminar()
    print()
    print(Fore.YELLOW+ "Monticulo:"+Fore.WHITE,m1)

def monticulizar():
    #  monticulizar

    m_monticulizado=MonticuloMax([2,19,36,17,25,3,7,1,92,23])
    #m_monticulizado=MonticuloMax([1,2,2,3,1,1,2,2,3,1])

    print(Fore.YELLOW+ "Monticulo monticulizado:"+Fore.WHITE,m_monticulizado)
    # añadir el 50
    m_monticulizado.insertar(50)
    print()
    print(Fore.YELLOW+ "Monticulo monticulizado:"+Fore.WHITE,m_monticulizado)

    m_monticulizado.eliminar(2) # Elimina el 19 que esta en la posicion 2
    print()
    print(Fore.YELLOW+ "Monticulo:"+Fore.WHITE,m_monticulizado)
    m_monticulizado.eliminar()
    print()
    print(Fore.YELLOW+ "Monticulo quitando el primer elemento monticulizado:"+Fore.WHITE,m_monticulizado)

    #vamos a grafica el arbol
    #elementos=[2,19,36,17,25,3,7,1,92,23]


#monticulo_max()
#smonticulo_min()
monticulizar()