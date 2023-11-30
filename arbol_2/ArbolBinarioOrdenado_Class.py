# Binario: De cada nodo salen como máximo dos ramas
# n-ario: De cada nodo salen como máximo n ramas
# Cada nodo tiene un clave
# Pueden ser ordandos o no
# Puede tener repetidos o no
# Equilibrado = Todas las ramas tienen la misma altura o como máximo un piso de diferencia

class Nodo():
    def __init__(self, clave, datos=[], izq=None, der=None) -> None:
        self._clave = clave
        self._izq = izq
        self._der = der

        # Queremos de 'datos' sea una lista para que un nodo pueda contener los
        # datos de todos los objetos que tienen la misma clave

        # Comprobar si los datos recibidos son una lista
        if isinstance(datos, list):
            # Si son una lista los acepto directamente
            self._datos = datos 
        else:
            # Sino creo un lista con un solo elemento -> los datos
            # que me acaban de pasar
            self._datos = []
            self._datos.append(datos)

    def __str__(self) -> str:
        # Mostrar número elementos en la lista de datos
        str_a_mostrar = "NODO [" + str(len(self._datos)) + "]"

        # Mostrar cada uno de los elementos de la lista de dastos
        for dato in enumerate(self._datos):
            str_a_mostrar += "\n" + str(dato)

        if str_a_mostrar == "":
            str_a_mostrar = "Ningún dato ..."

        return str_a_mostrar

    def getClave(self):
        return self._clave

    def getDatos(self) -> list:
        return self._datos

    def getIzq(self):
        return self._izq

    def getDer(self):
        return(self._der)

    def addDatos(self, datos):
        if isinstance(datos, list):
            self._datos = self._datos + datos
        else:
            self._datos.append(datos)

    def setIzq(self, izq):
        self._izq = izq

    def setDer(self, der):
        self._der = der


class ArbolBinarioOrdenado():
    def __init__(self) -> None:
        self._raiz = None

    def insertar(self, clave, datos):
        # Crer un nuevo nodo
        nueva_hoja = Nodo(clave, datos)

        # Compruebo si el arbol esta vacio
        if self._raiz == None:
            self._raiz = nueva_hoja
            return True  # ==========================>

        nodo_actual = self._raiz
        while nodo_actual != None:
            if nueva_hoja.getClave() < nodo_actual.getClave():
                # Ver si ya he llegado al último nodo de la
                # rama izquierda
                if nodo_actual.getIzq() == None:
                    # Insertar la hoja nueva
                    nodo_actual.setIzq(nueva_hoja)
                    return True  # ====================>
                else:
                    # Bajar por la iquerda
                    nodo_actual = nodo_actual.getIzq()
            elif nueva_hoja.getClave() > nodo_actual.getClave():
                # Ver si ya he llegado al último nodo de la
                # rama derecha
                if nodo_actual.getDer() == None:
                    # Insertar la hoja nueva
                    nodo_actual.setDer(nueva_hoja)
                    return True  # ====================>
                else:
                    # Bajar por la derecha
                    nodo_actual = nodo_actual.getDer()
            else:
                # La clave del nodo ha insertar ya existe en el arbol
                # ¿Que hacemos? .... Hacemos que en datos pueda haber
                # una lista con todos los datos que tienen la misma
                # clave
                nodo_actual.addDatos(nueva_hoja.getDatos())
                return True

    def buscar(self, claveBuscar) -> list:
        # Empiezo a buscar por la raiz del arbol
        nodo_actual = self._raiz

        # Mientras no he llegado al final del arbol busco
        while (nodo_actual != None):
            # Compruebo si he encontrado la clave que busco
            if (nodo_actual.getClave() == claveBuscar):
                # He encontrado el nodo que busco
                return nodo_actual.getDatos()  # =============>

            if (claveBuscar < nodo_actual.getClave()):
                # Explorar la rama izquierda
                nodo_actual = nodo_actual.getIzq()

            elif (claveBuscar > nodo_actual.getClave()):
                # Explorar la rama derecha
                nodo_actual = nodo_actual.getDer()

        return [None]

    def buscarTodoRecursivo(self, claveBuscar) -> list:
        return self.buscarRecursivo(self._raiz, claveBuscar)

    def buscarRecursivo(self, nodo_actual: Nodo, claveBuscar) -> list:
        if (nodo_actual == None):
            return [None]

        # Compruebo si he encontrado la clave que busco
        if (nodo_actual.getClave() == claveBuscar):
            # He encontrado el nodo que busco
            return nodo_actual.getDatos()  # =============>

        if (claveBuscar < nodo_actual.getClave()):
            # Explorar la rama izquierda
            return self.buscarRecursivo(nodo_actual.getIzq(), claveBuscar)

        elif (claveBuscar > nodo_actual.getClave()):
            # Explorar la rama derecha
            return self.buscarRecursivo(nodo_actual.getDer(), claveBuscar)

    def todoEnOrdenCentral(self) -> list:
        # Muestra todo el arbol en orden central
        # es decir todo a partir del nodo raiz
        return self.enOrdenCentral(self._raiz)

    def enOrdenCentral(self, nodo: Nodo) -> list:
        # Muestra el arbol en orden central
        # a partir de un nodo concreto

        if nodo == None:
            return []

        return self.enOrdenCentral(nodo.getIzq()) + nodo.getDatos() + self.enOrdenCentral(nodo.getDer())

    def mostrarTodoEnOrdenCentralDescendente(self):
        # Muestra todo el arbol en orden central
        # es decir todo a partir del nodo raiz
        self.mostrarEnOrdenCentralDescendente(self._raiz)

    def mostrarEnOrdenCentralDescendente(self, nodo: Nodo):
        # Muestra el arbol en orden central
        # a partir de un nodo concreto

        # Mostrar rama derecha
        if nodo.getDer() != None:
            # Hay rama derecha
            self.mostrarEnOrdenCentralDescendente(nodo.getDer())
        # Mostrar nodo central del subarbol
        print(nodo.getDatos())

        # Mostrar rama izquierda
        if nodo.getIzq() != None:
            # Hay rama izquierda
            self.mostrarEnOrdenCentralDescendente(nodo.getIzq())

    def mostrarTodoEnPreorden(self):
        # Muestra todo el arbol en orden central
        # es decir todo a partir del nodo raiz
        self.mostrarEnPreorden(self._raiz)

    def mostrarEnPreorden(self, nodo: Nodo):
        # Muestra el arbol en orden central
        # a partir de un nodo concreto

        # Mostrar nodo central del subarbol
        print(nodo.getDatos())

        # Mostrar rama izquierda
        if nodo.getIzq() != None:
            # Hay rama izquierda
            self.mostrarEnPreorden(nodo.getIzq())

        # Mostrar rama izquierda
        if nodo.getDer() != None:
            # Hay rama izquierda
            self.mostrarEnPreorden(nodo.getDer())

    def mostrarTodoEnPostorden(self):
        # Muestra todo el arbol en orden central
        # es decir todo a partir del nodo raiz
        self.mostrarEnPostorden(self._raiz)

    def mostrarEnPostorden(self, nodo: Nodo):
        # Muestra el arbol en orden central
        # a partir de un nodo concreto

        # Mostrar rama izquierda
        if nodo.getIzq() != None:
            # Hay rama izquierda
            self.mostrarEnPostorden(nodo.getIzq())

        # Mostrar rama izquierda
        if nodo.getDer() != None:
            # Hay rama izquierda
            self.mostrarEnPostorden(nodo.getDer())

        # Mostrar nodo central del subarbol
        print(nodo.getDatos())

