# divide y venceras con dos numeros grandes
# inclusoel ordenador no sb hcaerlo

# algoritmo de karatsuba
# pero si que poodemos hacerlo con operaci9ones mas peuqeñas
# va coonviertiendo en suma de descoomposiciones de dos
# y asi  cada vez que se divida en una parte dificil
# multiplicar sus digitos y esa sera su complexidad * sus digitos
# 1, z vale 3 , y vale 4  y xz vale 12 y xz se ira diviendp  otra vez hasta q llegue a mas pequeñas
# 1 por 3 de complejidad 20

# descomponer en complexidades mas p equeñas y sino se vuelve a dividir

def multiplicacion_enteroos(num1, num2):
    max_num_digitos = max(len(str(num1)), len(str(num2)))

    if max_num_digitos == 1:
        return num1*num2  # ==========>

    # dividir en dos partes iguales
    # ejemplo si num1 vale 632.345
    # mitad_difitos 6//2 = 3
    mitad_digitos = max_num_digitos//2

    # Ejemplo si num1 vale 632.345, entonces
    # mitat_alta_num1 = 632 <--- 632.345 // 10^3
    # mitad_baja_num1 = 345 <--- 632.345 entre 10^3 da como solucion el resto
    parte_alta_num1 = num1 // 10**mitad_digitos  # w
    parte_baja_num1 = num1 % 10**mitad_digitos  # x

    parte_alta_num2 = num2 // 10**mitad_digitos  # y
    parte_baja_num2 = num2 % 10**mitad_digitos  # z

    r = multiplicacion_enteroos(
        parte_alta_num1 + parte_baja_num1, parte_alta_num2+parte_baja_num2)
    wy = multiplicacion_enteroos(parte_alta_num1, parte_alta_num2)
    xz = multiplicacion_enteroos(parte_baja_num1, parte_baja_num2)

    solucion = wy*10**(2*mitad_digitos) + (r-wy-xz)*(10**mitad_digitos) + xz
    return solucion


print(multiplicacion_enteroos(1257, 34908))


def multiplicacion_no_optimos_enteroos(num1, num2):
    max_num_digitos = max(len(str(num1)), len(str(num2)))

    if max_num_digitos == 1:
        return num1*num2  # ==========>

    # dividir en dos partes iguales
    # ejemplo si num1 vale 632.345
    # mitad_difitos 6//2 = 3
    mitad_digitos = max_num_digitos//2

    # Ejemplo si num1 vale 632.345, entonces
    # mitat_alta_num1 = 632 <--- 632.345 // 10^3
    # mitad_baja_num1 = 345 <--- 632.345 entre 10^3 da como solucion el resto
    parte_alta_num1 = num1 // 10**mitad_digitos  # w
    parte_baja_num1 = num1 % 10**mitad_digitos  # x

    parte_alta_num2 = num2 // 10**mitad_digitos  # y
    parte_baja_num2 = num2 % 10**mitad_digitos  # z

    wz = multiplicacion_enteroos(parte_alta_num1, parte_baja_num2)
    xy = multiplicacion_enteroos(parte_baja_num1, parte_alta_num2)

    wy = multiplicacion_enteroos(parte_alta_num1, parte_alta_num2)
    xz = multiplicacion_enteroos(parte_baja_num1, parte_baja_num2)

    solucion = wy*10**(2*mitad_digitos) + 10**mitad_digitos*(wz+xy) + xz
    return solucion


print(multiplicacion_no_optimos_enteroos(1257, 34908))


def potencia_eficiente(base, exponente) -> int:
    newExponente = exponente//2

    if newExponente == 1:
        return base**exponente # ==============>

    resultado = potencia_eficiente(
        base, newExponente)**2 * (base ** (exponente % 2))

    return resultado


print(potencia_eficiente(2, 32))

