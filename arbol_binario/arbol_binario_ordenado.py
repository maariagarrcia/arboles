class Nodo():
    # SI  NO LE PASO  NINGUN DATO QUE SEA INA LISTA
    def __init__(self, clave, datos=[], izq=None, der=None):
        self._clave = clave
        self._izq = izq
        self._der = der


        # queremos que "datos" sea una lista para que un nodo
        # pueda contener todos los datos  de todos  los objetos que 
        # tienen la misma clave
        
        # compruebo si los datos recibidos son una  lista
        if isinstance(datos, list):
            # si  son una lista  loos acepto  directamente
            self._datos = datos
        else:
            # sino creo en una lista con minimo  un  elemento -> los datos que 
            # me acaban  de pasar

            self._datos = []
            self._datos.append(datos)
 

       
    # para que nadie se salte el setter se pone el guion bajo
    def set_Datos(self, datos):
        self._datos = datos

    def set_izq(self, izq):
        self._izq = izq

    def set_der(self, der):
        self._der = der

    def get_clave(self):
        return self._clave

    def add_datos(self, datos):
        if isinstance(datos, list):
            self._datos= self._datos + datos
        else:
               self._datos.append(datos)


    def get_datos(self)-> list:
        return self._datos

    def get_izq(self):
        return self._izq

    def get_der(self):
        return self._der

    # str(self._clave)  es lo mismo que self._clave.__str__()
    #  \ ES PARA QUE  RECONOZCA EL SALTO DE LINEA
    def __str__(self) -> str:
        str_a_mostrar= "[" +str(len(self)) + "]"
        
        for  dato  in  enumerate(self._datos):
            str_a_mostrar += "\n" + dato.__str__()

        if str_a_mostrar == " ":
            str_a_mostrar = "Ningun dato..."

        return str_a_mostrar
        #  los nodos ahoora son listas por tanto hay que imprimirlos de forma diferente
        # return "Nodo: [" + str(self._clave) + "] \n" + \
        # " Datos: " + str(self._datos) + "\n" + " Izq: " +  \
        # "  "+ str(self._izq) + "\n" + " Der: " + str(self._der) + "\n"



    
# conjunto  de nodos, unos noodos que apuntan a otros
class ArbolBinarioOrdenado():
    def __init__(self):
        self._raiz = None

    # es loque se necesita una clave y  unos datos (que seria el jugador)
    # nosotros vamos   insertando una nueva hoja
    def insertar(self,clave,datos):
        # CREAR UN NUEVO NODO
        nueva_hoja = Nodo(clave,datos)
        
        # COMPROBAR SI ELARBOL ESTA VACIO
        if self._raiz == None:
            self._raiz = nueva_hoja
            return True #==================>

        nodo_actual= self._raiz
        while nodo_actual != None:
            # estariamso en la  raiz y vamos a preguntar  pq  lado me voy
            if  nueva_hoja.get_clave() < nodo_actual.get_clave():
                #  ver si ya he llegado a l ultimo nodo de la rama izquierda
                if nodo_actual.get_izq() == None:
                    #insertar la hoja   nueva
                    nodo_actual.set_izq(nueva_hoja)
                    return True #=======================>
                else:
                    # bajar por la izquierda
                    nodo_actual= nodo_actual.get_izq()
                # bajo por la  rama izquierda pero no siempre va a haber un nodo
                

            elif  nueva_hoja.get_clave() > nodo_actual.get_clave():
                #  ver si ya he llegado a l ultimo nodo de la rama derecha
                if nodo_actual.get_der() == None:
                    #insertar la hoja   nueva
                    nodo_actual.set_der(nueva_hoja)
                    return True

                else:
                    #bajo por la  rama derecha

                    nodo_actual= nodo_actual.get_der() 

            else:
                #la clave del nodo ha insertar es igual, ya existe en el arbol
                # VAMOS A HACER QUE EN DATOS PUEDA HABER UNA LISTA COON TODOS
                # # LOS DATOS QUE TIENEN LA MISMA CLAVE  
                nodo_actual.add_datos(nueva_hoja.get_datos())
                return True

    
    def mostrar_todo_en_orden_central(self):
        # Muestra todo  el arbol  en orden central
        # es  decir todo a partir del nodo raiz
        return self.mostrar_en_orden_central(self._raiz)

    def mostrar_en_orden_central(self,nodo:Nodo):
    # Muestra todo  el arbol  en orden central
    # a partir de un nodo concetro

        if nodo == None:
            return []

        return self.mostrar_en_orden_central(nodo.get_izq()) + nodo.get_datos() + self.mostrar_en_orden_central(nodo.get_der())

    def mostrar_todo_en_orden_central_descendente(self):
        # Muestra todo el arbol en orden central
        # es decir todo a partir del nodo raiz
        return self.mostrar_en_orden_central_descendente(self._raiz)

    def mostrar_en_orden_central_descendente(self, nodo: Nodo):
        
        if nodo == None:
            return []

        return self.mostrar_en_orden_central(nodo.get_der())+ nodo.get_datos() + self.mostrar_en_orden_central(nodo.get_izq()) 

    def mostrar_todo_en_preorden(self):
        return self.mostrar_en_preorden(self._raiz)
        
    def mostrar_en_preorden(self,nodo:Nodo):


        if nodo == None:
            return []

        return nodo.get_datos() + self.mostrar_en_orden_central(nodo.get_izq()) +  self.mostrar_en_orden_central(nodo.get_der())

    def mostrar_todo_en_postorden(self):
        return self.mostrar_en_postorden(self._raiz)

    def mostrar_en_postorden(self,nodo:Nodo):

        if nodo == None:
            return []

        return  self.mostrar_en_orden_central(nodo.get_izq()) +  self.mostrar_en_orden_central(nodo.get_der())+nodo.get_datos() 

    def buscar(self,clave_buscar)->list:
        #  empiezo a buscar por la raiz del arbol
        nodo_actual = self._raiz

        # mientras  no he llegado al final del arbol busco
        while (nodo_actual != None):
            # compruebo si he encontrado la  clave que busco
            if (nodo_actual.get_clave() == clave_buscar):
                return nodo_actual.get_datos() #====================>

            if (clave_buscar  <  nodo_actual.get_clave()):
                # si la clave a buscar es menor que el nodo me  voy por la izquierda
                nodo_actual = nodo_actual.get_izq()

            elif (clave_buscar  >  nodo_actual.get_clave()) :
                # si la clave a buscar es mayor que el nodo me  voy por la derecha
                nodo_actual = nodo_actual.get_der()

        return[None]  #====================>

    def buscar_todo_recursivo(self,clave_buscar)->list:
        return self.buscar_recursivo(clave_buscar,self._raiz)

    def buscar_recursivo(self,clave_buscar, nodo_actual: Nodo)->list:
        #  empiezo a buscar por la raiz del arbol
        # mientras  no he llegado al final del arbol busco
        if (nodo_actual == None):
            # condicion de fin de recursividad
            return [None]

         # compruebo si he encontrado la  clave que busco
        if (nodo_actual.get_clave() == clave_buscar):
            return nodo_actual.get_datos() #====================>

        if (clave_buscar  <  nodo_actual.get_clave()):
            # si la clave a buscar es menor que el nodo me  voy por la izquierda
            return self.buscar_recursivo(clave_buscar,nodo_actual.get_izq())
            
        elif (clave_buscar  >  nodo_actual.get_clave()) :
            # si la clave a buscar es mayor que el nodo me  voy por la derecha
            return self.buscar_recursivo(clave_buscar,nodo_actual.get_der())

    def buscar_NODO_todo_recursivo(self,clave_buscar):
        return self.buscar_nodo_recursivo(clave_buscar,self._raiz,None)

    def buscar_nodo_recursivo(self, clave_buscar, nodo_actual: Nodo, nodo_anterior=None):
        #  empiezo a buscar por la raiz del arbol
        # mientras  no he llegado al final del arbol busco
        if (nodo_actual == None):
            # condicion de fin de recursividad
            return None,None

            # compruebo si he encontrado la  clave que busco
        if (nodo_actual.get_clave() == clave_buscar):
            return nodo_actual, nodo_anterior #====================>

        if (clave_buscar  <  nodo_actual.get_clave()):
            # si la clave a buscar es menor que el nodo me  voy por la izquierda
            return self.buscar_nodo_recursivo(clave_buscar,nodo_actual.get_izq(),nodo_actual)
            
        elif (clave_buscar  >  nodo_actual.get_clave()) :
            # si la clave a buscar es mayor que el nodo me  voy por la derecha
            return self.buscar_nodo_recursivo(clave_buscar,nodo_actual.get_der(),nodo_actual)
     
    def buscar_max_sin_nodo_actual(self, nodo_actual: Nodo):
        # busca la  maxima clave  por debajo del nodo_actual
        if (nodo_actual.get_der()!=None):
            # si nodo tiene derecha seguro que ahi esta el mayor
            return self.buscar_maximo(nodo_actual.get_der())

        else:
            # si el nodo actual No tiene r ama derecha la clave mayor 
            #  por debajo tendra que estar en la rama izquierda
            return self.buscar_maximo(nodo_actual.get_izq())
   
    def  buscar_maximo(self,nodo_actual:Nodo,nodo_padre=None):
        # Busca el  nodo con clave maxima incluyendo el nodo actual
        if nodo_actual==None:
            return None,None

        # como buscamos el max nos interesa la rama  derecha si existe
        if nodo_actual.get_der() == None:
            # retorna un nodo o None
            return nodo_actual,nodo_padre
        
        else:
            return self.buscar_maximo(nodo_actual.get_der(),nodo_actual)

    def set_padre_izqder(self,nodo_padre,nodo_eliminar, nodo_siguiente):
        if nodo_padre.get_izq() == nodo_eliminar:
            nodo_padre.set_izq(nodo_siguiente)
        else:
            nodo_padre.set_der(nodo_siguiente)

    def eliminar_clave(self,clave)->bool:
        # hay 4 tipos de eliminacion
        # 1. el modo es un hoja, es decir,  no tiene hijos
        # 2. el nodo tiene un hijo derecho
        # 3. el nodo tiene un hijo izquierdo
        # 4. el nodo tiene dos hijos
        nodo, nodo_padre = self.buscar_NODO_todo_recursivo(clave)

        if nodo == None:
            return False

        if nodo.get_izq() == None and nodo.get_der() == None:
            # caso 1
            # el nodo es una hoja
            # lo elimino
            self.set_padre_izqder(nodo_padre,nodo,None)

        elif nodo.get_izq()!=None and nodo.get_der()==None:
            # caso 3
            # el nodo tiene un hijo izquierdo
            # lo elimino
            self.set_padre_izqder(nodo_padre,nodo,nodo.get_izq())
                

        elif nodo.get_izq()==None and nodo.get_der()!=None:
            # caso 2
            # el nodo tiene un hijo derecho
            # lo elimino
            self.set_padre_izqder(nodo_padre,nodo,nodo.get_der())

        else:
            # caso 4
            # el nodo tiene dos hijos
            # lo elimino
            # inicializacion
            nodo_max, nodo_max_padre= self.buscar_maximo(nodo.get_izq(),nodo)
            nodo_aux = nodo_max.get_izq()

            self.set_padre_izqder(nodo_max_padre,nodo,nodo_max)
         
            
            # PASO 2: Pooner como hijos de max los hijos de nodo a eliminar
            nodo_max.set_izq(nodo.get_izq())
            nodo_max.set_der(nodo.get_der())

            # PASO 3: Poner rama izquierda  de max en el lugar original d emax
            nodo_max_padre.set_der(nodo_aux)

        return True