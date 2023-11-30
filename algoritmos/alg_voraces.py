from colorama import Fore
# algoritmo VORAZ para el cambio de monedas

#### CAMBIO DE MONEDAS ####
monedas = [0.001, 0.1, 0.02, 0.25, 0.5, 1, 2]


def es_solucion(solucion: list, importe:  int) -> bool:
    # calcula cuanto dinero sigue faltando por devolver
    for moneda in solucion:
        importe = round(importe - moneda[0]*moneda[1], 3)

    return importe == 0


def cambio(monedas, importe):

    solucion = []

    restante = importe

    while monedas and not es_solucion(solucion, importe):
        # cada vez que se coge una moneda se elimina de la lista
        # para que la proxima vez no se vuelva a coger
        moneda = monedas.pop()

        # algoritmo avido : coge un poco de todos los candidatos
        # voraz: coja el maximo de cada posibilidad

        # determinar cuantas monedas se pueden cooger de ese tipo
        cantidad = (restante)//moneda

        # Si no se cogen mas de una entonces de esa moneda no se puede pq debe ser mayor que el dinero que queda;
        # SI es mayor que 0 la cantidad ---> se agrega como solucion óptima a la lista: añadimos tipo de monedad y la cantidad
        # que cogemos

        # para que vamos añadir 0 monedas de 2 euros
        if cantidad > 0:
            solucion.append([moneda, cantidad])
            # restar el importe de la moneda que se ha cogido
            restante = round(restante - moneda*cantidad, 3)
    # si no se ha encontrado solucion se devuelve una lista vacia
    if not es_solucion(solucion, importe):
        solucion = None

    # si se ha encontrado solucion se devuelve la lista de monedas y su cantidad
    return solucion


print(Fore.YELLOW + "Cambio de monedas", cambio(monedas, 4.755))


##### MOCHILA #####
# va cogiendo candidatos de la lista de posibles soluciones

# dentro de solucion yo estoy metiendo  una solucion que  tiene 3 elementos
# 1) el objeto 2) el peso  2) la cantidad

def es__solucion(solucion: list, objetivo:  int) -> bool:
    cap_actual = 0
    for item in solucion:
        cap_actual = round(cap_actual + item[1], 3)

    return cap_actual == objetivo, objetivo-cap_actual


def mochila(candidatos: list, objetivo: int) -> list:
    solucion = []
    cap_Atual = 0
    c_c = candidatos.copy()
    # c_C es una copia de candidatos
    # avido: coge un poco  de todos los candidatos

    while c_c and not es__solucion(solucion, objetivo)[0]:
        item_actual = c_c.pop()

        # ver si queda espacio en la mochila
        if item_actual[1] < (objetivo-cap_Atual):
            solucion.append(item_actual)
            cap_Atual = round(cap_Atual + item_actual[1], 3)

    return es__solucion(solucion, objetivo), solucion

# funcion para ordenar con el sort() por la clave que queremos
# Debe devolver el valor por el cual se ordena
# Recibe por parametro uno de los elementosa a ordenar
# Esta funcion se le pasa al sort()


def beneficio(item):
    return item[2]


objetos = [["termo", 1.1, 20], ["mate", 0.3, 6], ["galletita", 0.5, 7], ["te", 0.09, 0.7], [
    "yerba", 0.3, 7], ["bombilla", 0.33, 6], ["azucar", 0.5, 2], ["alfajor", 0.6, 13], ["facturas", 0.8, 6]]
capacidad_maxima = 3

objetos.sort(key=beneficio)

print(Fore.YELLOW+"Objetos", objetos)
print(Fore.YELLOW+"Solcuion encontrada?",
      mochila(objetos, capacidad_maxima)[0][0])
print(Fore.YELLOW+"Error", mochila(objetos, capacidad_maxima)[0][1])

