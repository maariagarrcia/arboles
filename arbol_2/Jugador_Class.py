class Jugador():
    def __init__(self, nombre, equipo, edad) -> None:
        self._nombre = nombre
        self._equipo = equipo
        self._edad = edad

    def __str__(self) -> str:
        return (self._nombre + " " + str(self._edad) + " " + self._equipo)

    def getNombre(self) -> str:
        return(self._nombre)

    def getEquipo(self) -> str:
        return(self._equipo)

    def getEdad(self) -> str:
        return(self._edad)
