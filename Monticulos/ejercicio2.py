# El general Hux es la persona encargada de administrar todas las operaciones de la base Starki- ller, para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que se realizan, contemplando lo siguiente:

# vamos a crear un monticulo de maximos de 8 elementoos del general Hux

from monticulo_max_class import *
from colorama import Fore


class MonticuloMax(list):
    def __init__(self, list=[]) -> None:
        # le enviaremos la  lista
        super().__init__(list)
        # monticulizar
        self._monticulizar()

    def __str__(self) -> str:
        s= ""
        for item in self:
            s+= str(item[0])+ " "+ str(item[1])+ "\n"
        return s

    def _flotar(self, posicion=None) -> None:
        
        if posicion == None:
            posicion = len(self)-1

        # comprobar si la posicion esta dentro
        # pq yo no puedo  hacer flotar un elemento  que  no este  en  la lista

        # Si no se  recibe la posicion  del  elementoa flotar
        # entenderemos  quee  se quiere floatar el ultimo elemento

        posicion_padre = (posicion-1)//2
        # comparamos el elemento q  queremos flotar con su padre
        # OJO -->  el  elemento  que queremos flotar el self[posicion]
        # Como yo soy una lista yo soy self
        while (posicion > 0) and (self[posicion][0] > self[posicion_padre][0]):
            # el elemento pesa mas  que su padre
            # hay que intercambiarlo  con su padre
            self._intercambio(posicion, posicion_padre)
            posicion = posicion_padre
            posicion_padre = (posicion-1)//2

        # flota cada vez una sola poosicion
        # vamos a  haver  subir el elemento  añadido  hasta
        # la que  corresponda su pesoo

    def _intercambio(self, pos1, pos2=None) -> None:
        if pos2 == None:
            pos2 = len(self)-1

        aux = self[pos1]
        self[pos1] = self[pos2]
        self[pos2] = aux

        return pos2

    def _hundir(self, posicion=None) -> None:
        # Si no recibe la posicion del elemento a hundir
        # entenderemos que se quiere hundir el primer elemento

        # mientras  no este  en el fondo y el peeso del elemento
        # a hundir es menor continuar hundiendo
        # si mi hijo esta fuera del array estamos en el fondo
        #  si es  mayor es que he llegado al fondo
        # menor que no es la primer posicion de lo qnue tenemos nque hundir
        hundir, hijo = self.hay_que_hundir(posicion)
        # si hundir es true entrara en el bucle
        while hundir:
            # ver si  el  valor es menor que el hijo izquierda o  derecha
            # intercambia los valores
            posicion = self._intercambio(posicion, hijo)
            # intercambiar  la posicion  con el hijo
            hundir, hijo = self.hay_que_hundir(posicion)

    def hay_que_hundir(self, posicion) -> list:

        pos_hijo_izq = (2 * posicion) + 1
        pos_hijo_der = pos_hijo_izq + 1
        valor = self[posicion][0]

        if pos_hijo_izq < len(self):
            if valor < self[pos_hijo_izq][0]:
                # si es mejor significa que todavia puede bajar mas
                # el hijo izquierda es el mayor
                return [True, pos_hijo_izq]

        if pos_hijo_der < len(self):
            if valor < self[pos_hijo_der][0]:
                # si es mejor significa que todavia puede bajar mas
                # el hijo derecha es el mayor
                return [True, pos_hijo_der]

        return [False, None]

    def _monticulizar(self) -> None:
        for posicion in range(len(self)):
            self._flotar(posicion)

    def insertar(self, clave,item) -> None:
        # Insertar nuevo  item al final (de la lista)
        self.append((clave,item))

        # flotar el item
        self._flotar()

    def eliminar(self, posicion=0) -> None:
        if posicion < 0 or posicion > len(self):
            raise ValueError("Posicion a hundir fuera de rango")

        # intercambiar el elemento a eliminar con el ultimo
        self._intercambio(posicion)

        # hacer un hundimiento
        self._hundir(posicion)

        # eliminar el ultimo elemento
        return self.pop()

#m1 = MonticuloMax([3,1,2,1,2,3,2,1,2,1])
# print(m1)
#


# inicializamos el monticulo con 8 operaciones  que contegan: encargado, descripcion,  hora, cantidad de strormtroopers
# las ooperaciones se ordenan por: pedidos de lider supermo nivel 3, capitan phasma 2, resto 1

# si se lo paso asi no va a funcionar
#m = MonticuloMax([(3,"ordenar a los stormtroopers", 8, 100),(2,"controlar nave", 21, 70),(1,"destruir nave X", 12, 8),1,("ordenar armas", 2, 9),(3,"limpiar  base Starkiller", 15, 24),(1,"aterrizar en planeta ", 11),(2,"buscar armas  ", 22, 11),(2,"vigilar intrusos", 5, 25),(2,"preparar ataque", 7, 2),(1,"buscar comida", 17, 10)])

m = MonticuloMax()
#m.insertar([3, "ordenar a los stormtroopers", 8, 100])
#m.insertar([1, "ordenar armas", 2, 9])
#m.insertar([2, "vigilar intrusos", 5, 25])
#m.insertar([1, "aterrizar en planeta ", 11])
#m.insertar([2, "buscar armas  ", 22, 11])
#m.insertar([3, "limpiar  base Starkiller", 15, 24])
#m.insertar([2, "preparar ataque", 7, 2])
#m.insertar([1, "buscar comida", 17, 10])
#m.insertar([2, "controlar nave", 21, 70])
#m.insertar([1, "destruir nave X", 12, 8])
#print(Fore.YELLOW + "Monticulo monticulizado:"+Fore.WHITE, m)


class Paciente():
    def __init__(self, nombre:str, edad:int, dolencia:str, telefono:str) -> None:
        self._nombre = nombre
        self._edad = edad
        self._dolencia = dolencia
        self._telefono = telefono
        self._prioridad = self._calcular_prioridad()

    def _calcular_prioridad(self) -> int:
        if self._dolencia == "consulta":
            return 1
        elif self._dolencia == "emergencias":
            return 2
        elif self._dolencia == "urgencias":
            return 3

    def get_prioridad(self) -> int:
        return self._prioridad



    def __str__(self) -> str:
        return ("Paciente: "+self._nombre+\
        " Edad: "+str(self._edad)+\
         "Dolencia: "+self._dolencia)


p1=Paciente("Maria", 19, "urgencias", "641234567")
p2=Paciente("Manuel", 34, "consulta", "641233567")
p3=Paciente("Ana", 45, " urgencias", "641234567")
p4=Paciente("Juan", 23, "consulta", "641234567")
p5=Paciente("Luis", 56, "consulta", "641234567")
p6=Paciente("Antonio", 12, "emergencias", "641234567")
p7=Paciente("Jose", 67, "emergencias", "641234567")
p8=Paciente("Mariana", 59, "consulta", "641234567")
p9=Paciente("Manuela", 3, "consulta", "641234567")
p10=Paciente("Anabel", 4, "urgencias", "641234567")



m.insertar(p1.get_prioridad(),p1)
m.insertar(p2.get_prioridad(),p2)
m.insertar(p3.get_prioridad(),p3)
m.insertar(p4.get_prioridad(),p4)
m.insertar(p5.get_prioridad(),p5)
m.insertar(p6.get_prioridad(),p6)
m.insertar(p7.get_prioridad(),p7)
m.insertar(p8.get_prioridad(),p8)
m.insertar(p9.get_prioridad(),p9)
m.insertar(p10.get_prioridad(),p10)

print(m)

# cambiar pedir turno  de p7

#clave,paciente= m.eliminar()
#print(clave,str(paciente))


for i in range(0,10):
    print(m.eliminar()[1])
    print(m)