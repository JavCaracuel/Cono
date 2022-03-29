import numpy as np

# Se definen los movimientos posibles del caballo
knightMovements = {
	0: [1, 2],
	1: [2, 1],
	2: [2, -1],
	3: [1, -2],
	4: [-1, -2],
	5: [-2, -1],
	6: [-2, 1],
	7: [-1, 2]
}

combinations = [] # Lista de los posibles tableros

"""
Descripcion: Funcion encargada de mostrar el tablero con los caballos
Entrada: Tablero, posicion del tablero, tamano del tablero
Salida: Ninguna
"""
def print_board(board, index, size):
	print("╔" + "════╤"*(size - 1) + "════╗", end="")
	print(f"\r╔═ Tablero {index} ")
	for i in range(size):
		print("║", end="")
		for j in range(size):
			color = "\033[0m"

			if board[i, j] == 1:
				color = "\033[32m"
			elif board[i, j] == size**2:
				color = "\033[31m"				

			print(f"{color}{board[i, j]:^4}\033[0m", end="")
			
			if j != size - 1:
				print("│", end="")
		print("║")
		if i != size - 1:
			print("╟" + "────┼"*(size - 1) + "────╢")
	print("╚" + "════╧"*(size - 1) + "════╝")

"""
Descripcion: Funcion encargada de comprobar que la posicion del caballo es valida
Entrada: Tablero, tamano del tablero, posicion del caballo
Salida: True si la posicion es valida, False si no es valida
"""
def is_valid_movement(board, size, position):
	if (position[0] >= 0) and (position[0] < size) and (position[1] >= 0) and (position[1] < size) and (board[position[0], position[1]] == 0):
		return True # Se devuelve True si el movimiento se encuentra dentro del tablero y no se encuentra ocupado

	return False # Se devuelve False si la casilla se encuentra ocupada o si la posicion es invalida

"""
Descripcion: Funcion encargada de mover el caballo hacia una posicion determinada
Entrada: Tablero, tamano del tablero, posicion del caballo, numero de paso
Salida: True si se pudo mover el caballo, False si no se pudo mover
"""
def move_knight(board, size, position, step):
	# Si el caballo ya se movio en todas las posiciones posibles, se agrega la combinacion al arreglo de combinaciones
	if step > size**2:
		combinations.append(board.copy())
		print(f"\rCombinaciones obtenidas: {len(combinations)}", end="")
		board[position[0], position[1]] = 0 # Se elimina el caballo de la posicion actual

		return True # Se devuelve True para indicar que el caballo se pudo mover correctamente

	# Se obtienen todos los movimientos posibles del caballo
	for i in range(0, 8):
		next_position = [x + y for (x, y) in zip(position, knightMovements[i])] # Se obtiene la posicion siguiente del caballo
		
		# Se verifica si el movimiento es valido
		if is_valid_movement(board, size, next_position):
			board[next_position[0], next_position[1]] = step # Se coloca el caballo en la posicion siguiente

			move_knight(board, size, next_position, step + 1) # Se llama a la funcion para mover el caballo en la posicion siguiente

	board[position[0], position[1]] = 0 # Se elimina el caballo de la posicion actual

	return False # Se devuelve False para indicar que el caballo no se pudo mover

"""
Descripcion: Funcion encargda de ejecutar el programa
Entrada: Ninguna
Salida: Ninguna
"""
def main():
	# Se indica el tamano del tablero y la posicion inicial del caballo
	size = int(input("Indique el tamano del tablero: "))
	position = [int(x) for x in input("Indique la posicion del caballo [x, y]: ").split(",")]

	# Se crea el tablero y se coloca el caballo en la posicion indicada
	step = 1
	board = np.zeros((size, size), dtype=int)
	board[position[0], position[1]] = step
	step += 1

	# Se llama a la funcion encargada de mover el caballo haciendo uso de todos sus posibles movimientos
	print("\nCalculando combinaciones...")
	move_knight(board, size, position, step)

	# Se imprimen las combinaciones obtenidas
	if len(combinations) > 0:
		print("\n")
		for index, combination in enumerate(combinations):
			print_board(combination, index + 1, size)
	else:
		print("\nNo se encontraron combinaciones")

if __name__ == "__main__":
	main()