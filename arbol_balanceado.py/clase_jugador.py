class Jugador():
    def __init__(self, nombre, equipo, edad) -> None:
        self._nombre = nombre
        self._equipo = equipo
        self._edad = edad

    def __str__(self) -> str:
        return (self._nombre + " " + str(self._edad) + " " + self._equipo)

    def get_nombre(self) -> str:
        return(self._nombre)

    def get_equipo(self) -> str:
        return(self._equipo)

    def get_edad(self) -> str:
        return(self._edad)