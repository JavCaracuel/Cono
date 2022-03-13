valores={
    "b":"a",
    "c":"a",
    "d":"a",
    "e":"b",
    "f":"b",
    "h":"c",
    "i":"d",
    "j":"d",
    "k":"e",
    "m":"f",
    "g":"h",
    "l":"j",
    "n":"m",
    "o":"m"
}
# variable que contiene el camino recorrido hasta llegar a la letra a buscar
camino=[]
def buscar(inicio,valorBuscar):
    camino.append(inicio)
    # si encontramos el elemento, lo devolvemos
    if inicio==valorBuscar:
        return valorBuscar
    # recorremos todos los elementos en busca del valor de inicio
    for k,v in valores.items():
        # si el valor del elemento tiene como padre al valor de inicio
        if v==inicio:
            # llamamos a la función recursivamente enviando el nuevo padre
            result=buscar(k,valorBuscar)
            # si hemos recibido algun resultado es que hemos encontrado el
            # elemento que buscamos
            if result:
                return result
    camino.pop()
    # si llegamos aqui, es que hemos llegado al final de una profundidad
    return 0
result=buscar("a","o")
if result:
    print(camino)
else:
    print("no encontrado")


# import numpy as np
# import time
# import pygame
# import random


# def comprobar_posicion_profundidad(tablero,ficha_posicion,array_posible):
#     aux_count=0
#     for new_position in [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]:
#         if (ficha_posicion[0] + new_position[0]) < 0 or (ficha_posicion[1] + new_position[1]) < 0 or (ficha_posicion[0] + new_position[0]) >= (len(tablero)) or (ficha_posicion[1] + new_position[1]) >= (len(tablero[0])):
#             continue

#         if tablero[(ficha_posicion[0] + new_position[0])][(ficha_posicion[1] + new_position[1])] != 0:
#             continue
#         aux_count+=1
#         array_posible.insert(0,[tuple((ficha_posicion[0] + new_position[0],ficha_posicion[1] + new_position[1])),ficha_posicion])

#     return aux_count
    
# def seleccion_profundidad(tablero,ficha_posicion,array_posible):
    
#     comprobar_posicion_profundidad(tablero,ficha_posicion,array_posible)
#     array_solucion.append(ficha_posicion)
#     tablero[array_solucion[len(array_solucion)-1][0]][array_solucion[len(array_solucion)-1][1]]=1
#     if (np.count_nonzero(tablero)==size_tablero**2):
#         return 1
#         # ficha_posicion_aux=[array_posible[0][0],array_posible[0][1]]
#     for i in array_posible:
#         if i[1]==ficha_posicion:
#             #ficha_posicion=i[0]
#             resultado=seleccion_profundidad(tablero,i[0],array_posible)
#             if resultado!=0:
#                 return resultado

#     print("-------------",ficha_posicion,"----------------")
#     print(tablero)
#     tablero[array_solucion[len(array_solucion)-1][0]][array_solucion[len(array_solucion)-1][1]]=0
#     array_solucion.pop()
#     array_posible.pop(0)
#     return 0
#     # if(ficha_posicion==array_posible[0]):
#     #     return array_posible[0]
    
#     # tablero[array_posible[0][0]][array_posible[0][1]]=num_paso
    
#     # array_posible.pop(0)
            
#     # return ficha_posicion
    


# intro=0
# size_tablero= 0
# while intro == 0:
#     print("Elija el tamaño del tablero:")
#     size_tablero=input()
#     if size_tablero.isnumeric():
#         intro=1
#         size_tablero= int(size_tablero)
#     else:
#         print("Valor no válido")

# tablero = np.zeros((size_tablero, size_tablero))

# ficha_posicion=(0,0)
# num_paso=1
# tablero[ficha_posicion[0]][ficha_posicion[1]]=num_paso

# print(tablero)

# juego=0
# array_posible=[]
# array_solucion=[]

# seleccion_profundidad(tablero,ficha_posicion,array_posible)


# print("Juego terminado")
# print("Tiempo:",fin-inicio)

# print("Tablero:\n",tablero)


