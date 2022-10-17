from random import randrange


print("Juguemos al Ta-Te-Ti?")
name_jug = input("Ingresa tu nombre: ")
start = print("Empieza el juego, la pc realiza el primer movimiento...")


        #CREANDO EL TABLERO

def display_tablero(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def move_jug(board):
    ok = False
    while not ok:
        move = input("Ingresa tu movimiento {}: ".format(name_jug))
        ok = len(move) == 1 and move <= "9" and move >= "1"
        if not ok:
            print("Movimiento invalido. Por favor {} ingresa nuevamente tu movimiento: ".format(name_jug))
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ["X", "O"]
        if not ok:
            print("¡Celda ocupada! intenta de nuevo")
            continue
        board[row][col] = "X"

def celdas_free(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free.append((row,col))
    return free

def ganador(board,sgn):
    if sgn == "O":
        who = "me"
    elif sgn == "X":
        who = "you"
    else:
        who = None
    cross1 = cross2 = True
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



def mov_pc(board):
    free = celdas_free(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = "O"

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
board[1][1] = "O"
free = celdas_free(board)
turno_jugador = True

while len(free):
    display_tablero(board)
    if turno_jugador:
        move_jug(board)
        victoria = ganador(board,"X")
    else:
        mov_pc(board)
        victoria = ganador(board, "O")
    if victoria != None:
        break
    turno_jugador = not turno_jugador
    free = celdas_free(board)

display_tablero(board)
if victoria == "you":
    print("¡Has ganado {}!".format(name_jug))
elif victoria == "me":
    print("Perdiste {}".format(name_jug))
else:
    print("Empate")
