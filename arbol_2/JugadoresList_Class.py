class JugadoresList(list):
    def __init__(self, list) -> None:
        super().__init__(list)

    def __str__(self) -> str:
        str_to_show = ""
        for idx, jugador in enumerate(self):
            if (jugador != None):
                str_to_show += "\n  · " + jugador.__str__()

        if str_to_show == "":
            str_to_show = "Jugadores [0] => Ningún jugador ..."
        else:
            str_to_show = "Jugadores [" + str(len(self)) + "]" + str_to_show

        return str_to_show

    def showQuatity(self) -> str:
        str_to_show = "Jugadores [" + str(len(self)) + "]"
        return str_to_show

    def showNames(self) -> str:
        str_to_show = "Jugadores [" + str(len(self)) + "]\n"
        for idx, jugador in enumerate(self):
            str_to_show += jugador.nombre + ", "

        if str_to_show == "":
            str_to_show = "Jugadores [0] => Ningún jugador ..."

        return str_to_show
