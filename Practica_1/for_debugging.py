# %%
import numpy
import random

# %% [markdown]
# # Definicion de funciones

# %%
different_solutions=[]
movements=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

movements_order=[]

def get_coord(number, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == number:
                return i, j


def get_move(val_pos, n, chessboard):
    if (val_pos[0] >= 0) and (val_pos[0] < n) and (val_pos[1] >= 0) and (val_pos[1] < n) and (chessboard[val_pos[0], val_pos[1]] == 0):
        return True # Se devuelve True si el movimiento se encuentra dentro del tablero y no se encuentra ocupado
    return False

# functions that returns number of posible moves for knight
def get_moves_number(val_pos, n, chessboard):
    moves = 0
    if get_move((val_pos[0] + 2, val_pos[1] + 1), n, chessboard):
        moves += 1
    if get_move((val_pos[0] + 2, val_pos[1] - 1), n, chessboard):
        moves += 1
    if get_move((val_pos[0] - 2, val_pos[1] + 1), n, chessboard):
        moves += 1
    if get_move((val_pos[0] - 2, val_pos[1] - 1), n, chessboard):
        moves += 1
    if get_move((val_pos[0] + 1, val_pos[1] + 2), n, chessboard):
        moves += 1
    if get_move((val_pos[0] + 1, val_pos[1] - 2), n, chessboard):
        moves += 1
    if get_move((val_pos[0] - 1, val_pos[1] + 2), n, chessboard):
        moves += 1
    if get_move((val_pos[0] - 1, val_pos[1] - 2), n, chessboard):
        moves += 1
    return moves

#function bubble sort
def bubble_sort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j][0]>lista[j+1][0]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista


def knights_tour(posicion,n,move_number,chessboard):
    global movements_order
    movements_order = []
    if move_number>n*n:
        different_solutions.append(chessboard.copy())
        print(f"\rnum sol = {len(different_solutions)}", end="")
        # descomentar esto si queremos mas de una solucion
        # x,y = get_coord(move_number-1, chessboard)
        # chessboard[x,y] = 0
        return True

    for i in movements:
        x,y = get_coord(move_number-1, chessboard)
        posicion=(x+i[0],y+i[1])
        if get_move(posicion,n,chessboard):
            num_valores_aux=get_moves_number(posicion,n,chessboard)
            movements_order.append((num_valores_aux,posicion))
        
    movements_order= bubble_sort(movements_order)

    for i in movements_order:
        chessboard[i[1][0],i[1][1]] = move_number
        knights_tour(i[1],n,move_number+1,chessboard)
        # comentar este break si queremos más de 1 solucion
        break
            
    x,y = get_coord(move_number-1, chessboard)
    chessboard[x,y] = 0
    return False
            


def main():
    intro=0
    move_number=1
    while intro == 0:
        print("Elija el tamaño del tablero:")
        size_tablero=input()
        # Control de errores
        if size_tablero.isnumeric():
            intro=1
            size_tablero= int(size_tablero)
        else:
            print("Valor no válido")
        print("Elija la posición inicial del caballo con la forma [x,y]:")
        posicion=input()
        # Control de errores
        posicion=posicion.split(",")
        try:
            posicion=(int(posicion[0]),int(posicion[1]))
            posicion= (posicion[0],posicion[1])
            intro=1
        except:
            print("Valor no válido")
            intro=0

    chessboard = numpy.zeros((size_tablero, size_tablero))
    chessboard[posicion[0],posicion[1]] = move_number
    move_number+=1

    knights_tour(posicion,size_tablero,move_number,chessboard)
    for i,j in enumerate(different_solutions):
        print(f"num sol = {i}")
        print(j)


if __name__ == "__main__":
	main()
