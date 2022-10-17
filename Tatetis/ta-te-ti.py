print("En este repositorio guardare mis avances de proyectos en python")

from random import randrange



name_jug = input("Ingresa Tu nombre: ")
saludo = input("Hola {}, tus movimientos en el tablero se marcaran con la O".format(name_jug))
run = print("Lets go!!!")

#       Creando el tablero

def display_tablero(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def mov_jug(board):
	ok = False	# suposición falsa - la necesitamos para entrar en el bucle
	while not ok:
		move = input("Ingresa tu movimiento {}: ".format(name_jug)) 
		ok = len(move) == 1 and move >= '1' and move <= '9' # validacion al input. Un solo digito, mayor a 0 y menor a 9.
		if not ok:
			print("Movimiento erróneo {}, ingrésalo nuevamente".format(name_jug)) # Ingreso invalido. ingrésalo nuevamente
			continue
		move = int(move) - 1 	# numero de la celda, del 0 al 8
		row = move // 3 	# fila de la celda
		col = move % 3		# columna de la celda
		sign = board[row][col]	# marca el cuadro elegido
		ok = sign not in ['O','X']  # Corroboracion de que esa celda esta libre
		if not ok:	# esta ocupado, ingresa una posición nuevamente
			print("¡Cuadro ocupado, ingresa nuevamente!")
			continue
	board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado


def celdas_free(board):
	free = []	# la lista esta vacía inicialmente
	for row in range(3): # itera a través de las filas
		for col in range(3): # itera a través de las columnas
			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
				free.append((row,col)) # si, agrega una nueva tupla a la lista
	return free


def ganador(board,sgn):
	if sgn == "X":	# ¿Estamos buscando X?
		who = 'me'	# Si, es la maquina
	elif sgn == "O": # ... ¿o estamos buscando O?
		who = 'you'	# Si, es el usuario
	else:
		who = None	# ¡No debemos de caer aquí!
	cross1 = cross2 = True  # para las diagonales
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc(verificacion de si esta completa la fila)
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc(verificacion de si esta completa la columna  )
			return who
		if board[rc][rc] != sgn: # revisar la primer diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # revisar la segunda diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None

#   Turno pc

def mov_pc(board):
	free = celdas_free(board) # crea una lista de los cuadros vacios o libres
	cnt = len(free) #corroboro que free no esta vacio
	if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla
		this = randrange(cnt) #Numero random en el rango cnt
		row, col = free[this] #free[indice]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primer 'X' en el centro
free = celdas_free(board)
turno_jugador = True # ¿De quien es turno ahora?


while len(free):
	display_tablero(board)
	if turno_jugador:
		mov_jug(board)
		victoria = ganador(board,'O')
	else:	
		mov_pc(board)
		victoria = ganador(board,'X')
	if victoria != None:
		break
	turno_jugador = not turno_jugador		
	free = celdas_free(board)


display_tablero(board)
if victoria == 'you':
	print("¡Has ganado {}!".format(name_jug))
elif victoria == 'me':
	print("¡Perdiste {}!".format(name_jug))
else:
	print("¡Empate!")