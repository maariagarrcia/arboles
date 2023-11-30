class MonticuloMax(list):
    def __init__(self, list=[]) -> None:
        # le enviaremos la  lista
        super().__init__(list)
        # monticulizar
        self._monticulizar()

    def _flotar(self, posicion=None) -> None:
        # comprobar si la posicion esta dentro
        # pq yo no puedo  hacer flotar un elemento  que  no este  en  la lista

        # Si no se  recibe la posicion  del  elementoa flotar
        # entenderemos  quee  se quiere floatar el ultimo elemento
        if posicion == None:
            posicion = len(self)-1

        if posicion < 0 or posicion > len(self):
            raise ValueError("Posicion a flotar fuera  de rango")

        posicion_padre = (posicion-1)//2
        # comparamos el elemento q  queremos flotar con su padre
        # OJO -->  el  elemento  que queremos flotar el self[posicion]
        # Como yo soy una lista yo soy self
        while posicion > 0 and self[posicion] > self[posicion_padre]:
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

        if posicion == None:
            posicion = 0

        if posicion < 0 or posicion > len(self):
            raise ValueError("Posicion a hundir fuera de rango")

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
            posicion= self._intercambio(posicion, hijo)
            # intercambiar  la posicion  con el hijo
            hundir, posicion = self.hay_que_hundir(posicion)

    def hay_que_hundir(self, posicion) -> list:

        hijo_izq = (2 * posicion) + 1
        hijo_der = hijo_izq + 1
        valor = self[posicion]
    
        if hijo_izq < len(self):
            if valor < self[hijo_izq]:
                # si es mejor significa que todavia puede bajar mas
                # el hijo izquierda es el mayor
                return True, hijo_izq

        if hijo_der < len(self):
            if valor < self[hijo_der]:
                # si es mejor significa que todavia puede bajar mas
                # el hijo derecha es el mayor
                return True, hijo_der

        return False, None

    def _monticulizar(self) -> None:
        for  posicion in range(len(self)):
            self._flotar(posicion)

    def insertar(self, item) -> None:
        # Insertar nuevo  item al final (de la lista)
        self.append(item)

        # flotar el item
        self._flotar()

    def eliminar(self, posicion=0) -> None:
        if posicion < 0 or posicion > len(self):
            raise ValueError("Posicion a hundir fuera de rango")

        # intercambiar el elemento a eliminar con el ultimo
        self._intercambio(posicion, len(self)-1)

        # hacer un hundimiento
        self._hundir(posicion)

        # eliminar el ultimo elemento
        self.pop()

class MonticuloMin(list):

    def __init__(self, list=[]) -> None:
        # le enviaremos la  lista
        super().__init__(list)
        self._monticulizar()

    def _flotar(self, posicion=None) -> None:
        # comprobar si la posicion esta dentro
        # pq  yo no puedo  hacer flotar un elemento  que  no este  en  la lista

        # Si no se  recibe la posicion  del  elementoa flotar
        # entenderemos  quee  se quiere floatar el ultimo elemento
        if posicion == None:
            posicion = len(self)-1

        if posicion < 0 or posicion > len(self):
            raise ValueError("Posicion a flotar fuera  de rango")

        # todo elemento tiene padre

        # solo sirve para monticulos maximos
        posicion_padre = (posicion-1)//2
        # comparamos el elemento q  queremos flotar con su padre
        # OJO -->  el  elemento  que queremos flotar el self[posicion]
        # Como yo soy una lista yo soy self
        while posicion > 0 and self[posicion] < self[posicion_padre]:
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

        if posicion == None:
            posicion = 0

        if posicion < 0 or posicion > len(self):
            raise ValueError("Posicion a hundir fuera de rango")

        # mientras  no este  en el fondo y el peeso del elemento
        # a hundir es menor continuar hundiendo
        # si mi hijo esta fuera del array estamos en el fondo
        #  si es  mayor qes que he llegado al fondo menor que no
        # es la primer posicion de lo qnue tenemos nque hundir
        hundir, hijo = self.hay_que_hundir(posicion)
        while hundir:
              # ver si  el  valor es menor que el hijo izquierda o  derecha
              #  intercambia los valores
                posicion= self._intercambio(posicion, hijo)
                # intercambiar  la posicion  con el hijo
                hundir, posicion = self.hay_que_hundir(posicion)

    def hay_que_hundir(self, posicion) -> list:
            
            hijo_izq = (2 * posicion) + 1
            hijo_der = hijo_izq + 1
            valor = self[posicion]
    
            if hijo_izq < len(self):
                if valor > self[hijo_izq]:
                    # si es mejor significa que todavia puede bajar mas
                    # el hijo izquierda es el menor
                    return True, hijo_izq
    
            if hijo_der < len(self):
                if valor > self[hijo_der]:
                    # si es mejor significa que todavia puede bajar mas
                    # el hijo derecha es el menor
                    return True, hijo_der
    
            return False, None

    def _monticulizar(self) -> None:
        for  posicion in range(len(self)):
            self._flotar(posicion)

    def insertar(self, item) -> None:
        # Insertar nuevo  item al final (de la lista)
        self.append(item)

        # flotar el item
        self._flotar()

    def eliminar(self, posicion=0) -> None:
        if posicion < 0 or posicion > len(self):
            raise ValueError("Posicion a hundir fuera de rango")

        # intercambiar el elemento a eliminar con el ultimo
        self._intercambio(posicion, len(self)-1)

        # hacer un hundimiento
        self._hundir(posicion)

        # eliminar el ultimo elemento
        self.pop()

    