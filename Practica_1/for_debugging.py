# %%
from joblib import PrintTime
import numpy
import random

# %% [markdown]
# # Definicion de funciones

# %%
different_solutions=[]
movements=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

def get_coord(number, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == number:
                return i, j


def get_move(val_pos, n, chessboard):
    if (val_pos[0] >= 0) and (val_pos[0] < n) and (val_pos[1] >= 0) and (val_pos[1] < n) and (chessboard[val_pos[0], val_pos[1]] == 0):
        return True # Se devuelve True si el movimiento se encuentra dentro del tablero y no se encuentra ocupado
    return False
# %%

# %%
def knights_tour(posicion,n,move_number,chessboard):

    if move_number>n*n:
        different_solutions.append(chessboard.copy())
        print(f"\rnum sol = {len(different_solutions)}", end="")
        x,y = get_coord(move_number-1, chessboard)
        chessboard[x,y] = 0
        return True

    for i in movements:
        x,y = get_coord(move_number-1, chessboard)
        posicion=(x+i[0],y+i[1])
        if get_move(posicion, n, chessboard):
            chessboard[posicion[0],posicion[1]] = move_number
            knights_tour(posicion,n,move_number+1,chessboard)
            
    x,y = get_coord(move_number-1, chessboard)
    chessboard[x,y] = 0
    return False
            


def main():
    move_number=1
    n = int(input("Ingrese el tamaño de la matriz: "))
    chessboard = numpy.zeros((n, n))
    posicion=(0,0)
    chessboard[posicion[0],posicion[1]] = move_number
    move_number+=1
   


    knights_tour(posicion,n,move_number,chessboard)
    for i,j in enumerate(different_solutions):
        print(f"num sol = {i}")
        print(j)


if __name__ == "__main__":
	main()
