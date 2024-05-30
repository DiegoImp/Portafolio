# /*
#  * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
#  * y retorne lo siguiente:
#  * - "X" si han ganado las "X"
#  * - "O" si han ganado los "O"
#  * - "Empate" si ha habido un empate
#  * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
#  *   O si han ganado los 2.
#  * Nota: La matriz puede no estar totalmente cubierta.
#  * Se podría representar con un vacío "", por ejemplo.
#  */
def Verificar(Ejemplo: list):
    try:
        for i in range(3):
            if len(Ejemplo[i]) != 3:
                raise Exception
            simbolo = Ejemplo[i]
            for j in range(3):
                if simbolo[j] not in ["X", "O", " "]:
                    raise ValueError(
                        "\033[91mSolo se aceptan simbolos \"X\" u \"O\" o vacio\033[0m")
        print("\033[92mSe verifico y todo los simbolos son correctos\033[0m")
    except ValueError as e:
        raise e
    except Exception as y:
        print("\033[91mNo tiene una longitud de 3\033[0m")


def Fila(F: list):
    count_X = 0
    count_O = 0
    for elemento in F:
        if elemento[0] == "X" and elemento[1] == "X" and elemento[2] == "X":

            count_X += 1
            continue
        elif elemento[0] == "O" and elemento[1] == "O" and elemento[2] == "O":

            count_O += 1
            continue
    return count_X, count_O


def Columna(Ejemplo: list):
    count_X = 0
    count_O = 0
    for i in range(3):
        if Ejemplo[i][0] == "X" and Ejemplo[i][1] == "X" and Ejemplo[i][2] == "X":
            count_X += 1
            continue
        elif Ejemplo[i][0] == "O" and Ejemplo[i][1] == "O" and Ejemplo[i][2] == "O":
            count_O += 1
            continue

    return count_X, count_O


def Diagonal(Ejemplo: list):
    count_X = 0
    count_O = 0

    if Ejemplo[0][0] == "X" and Ejemplo[1][1] == "X" and Ejemplo[2][2] == "X":
        count_X += 1

    elif Ejemplo[0][0] == "O" and Ejemplo[1][1] == "O" and Ejemplo[2][2] == "O":
        count_O += 1

    if Ejemplo[0][2] == "X" and Ejemplo[1][1] == "X" and Ejemplo[2][0] == "X":
        count_X += 1

    elif Ejemplo[0][2] == "O" and Ejemplo[1][1] == "O" and Ejemplo[2][0] == "O":
        count_O += 1

    return count_X, count_O


def Juez(X: int, O: int):
    if X > O:
        print("Gano X")
    elif O > X:
        print("Gano O")
    else:
        print("Empate")


TaTeTi = [
    ["X", "X", "O"],
    ["X", "X", "O"],
    ["X", "O", "X"]
]

Verificar(TaTeTi)
row_X, row_O = Fila(TaTeTi)
colum_X, colum_O = Columna(TaTeTi)
Diag_X, Diag_O = Diagonal(TaTeTi)

Total_X = row_X + colum_X + Diag_X
Total_O = row_O + colum_O + Diag_O
Juez(Total_X, Total_O)
