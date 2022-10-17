print("Empieza el jueggo")

from random import randrange

nameJug = input("Ingresa tu Nombre: ")
saludo = print("Hola {}, tus movimientos en el tablero se marcaran con la O".format(nameJug))
run = print("Lets go!!!")


def display_tablero(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def movJug(board):
    ok = False
    while not ok:
        move = input("ingresa un movimiento {}: ".format(nameJug))
        ok = len(move) == 1 and move >= "1" and move <= "9"
        if not ok:
            print("Movimiento invalido, ingresa otro movimiento {}".format(nameJug))
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col] #pararse en la celda indicada y corroborar que no este ocupada
        ok = sign not in ["O","X"] #ok es verdadero si la celda no esta ocupada por nada
        if not ok:	# esta ocupado, ingresa una posición nuevamente
                print("¡Cuadro ocupado, ingresa nuevamente!")
                continue
        board[row][col] = "O" #marcar movimiento
    


def celdasFree(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O","X"]:
                free.append((row,col))
    return free


def ganador(board, sgn):
    if sgn == "X":
        who = 'me'	
    elif sgn == "O":
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True #verificacion de diagonales
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None

# Turno Pc

def movPc(board):
    free = celdasFree(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'



board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primer 'X' en el centro
free = celdasFree(board)
turno_jugador = True # ¿De quien es turno ahora?

while len(free):
    display_tablero(board)
    if turno_jugador:
        movJug(board)
        victoria = ganador(board, "O")
    else:
        movPc(board)
        victoria = ganador(board, "X")
    if victoria != None:
        break
    turno_jugador = not turno_jugador
    free = celdasFree(board)

display_tablero(board)
if victoria == "you":
    print("Ganaste {}".format(nameJug))
elif victoria == "me":
    print("Perdiste {}".format(nameJug))
else:
    print("Empate")
    