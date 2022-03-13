# valores={
#     "b":"a",
#     "c":"a",
#     "d":"a",
#     "e":"b",
#     "f":"b",
#     "h":"c",
#     "i":"d",
#     "j":"d",
#     "k":"e",
#     "m":"f",
#     "g":"h",
#     "l":"j",
#     "n":"m",
#     "o":"m"
# }
# # variable que contiene el camino recorrido hasta llegar a la letra a buscar
# camino=[]
# def buscar(inicio,valorBuscar):
#     camino.append(inicio)
#     # si encontramos el elemento, lo devolvemos
#     if inicio==valorBuscar:
#         return valorBuscar
#     # recorremos todos los elementos en busca del valor de inicio
#     for k,v in valores.items():
#         # si el valor del elemento tiene como padre al valor de inicio
#         if v==inicio:
#             # llamamos a la función recursivamente enviando el nuevo padre
#             result=buscar(k,valorBuscar)
#             # si hemos recibido algun resultado es que hemos encontrado el
#             # elemento que buscamos
#             if result:
#                 return result
#     camino.pop()
#     # si llegamos aqui, es que hemos llegado al final de una profundidad
#     return 0
# result=buscar("a","o")
# if result:
#     print(camino)
# else:
#     print("no encontrado")


import numpy as np
import time
#import pygame
import random

class array_posible_aux:
    array_posible_auxList = []

    def init(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

def pintar_camino(tablero, array_solucion):

    count = 0
    for i in array_solucion:
        count += 1
        tablero[i[0]][i[1]] = count

    return tablero


def comprobar_posicion_profundidad(tablero,ficha_posicion_p):
    array_hijos = []
    aux_count=0
    for new_position in [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]:
        if (ficha_posicion_p[0] + new_position[0]) < 0 or (ficha_posicion_p[1] + new_position[1]) < 0 or (ficha_posicion_p[0] + new_position[0]) >= (len(tablero)) or (ficha_posicion_p[1] + new_position[1]) >= (len(tablero[0])):
            continue

        if tablero[(ficha_posicion_p[0] + new_position[0])][(ficha_posicion_p[1] + new_position[1])] != 0:
            continue
        aux_count+=1
        array_hijos.insert(0,[tuple((ficha_posicion_p[0] + new_position[0],ficha_posicion_p[1] + new_position[1])),ficha_posicion_p])

    return array_hijos
    

def seleccion_profundidad(tablero,ficha_posicion,array_posible):
    
    array_posible_lista = []

    array_posible_lista = comprobar_posicion_profundidad(tablero,ficha_posicion)[0:] 
    array_solucion.append(ficha_posicion)
    tablero[array_solucion[len(array_solucion)-1][0]][array_solucion[len(array_solucion)-1][1]]=1
    
    if (np.count_nonzero(tablero)==size_tablero**2):
        lista_soluciones.append(array_solucion)
        return 1
    aux_count = 0
    for i in array_posible_lista:
        aux_count += 1    
        #print(aux_count)
        if i[1]==ficha_posicion:
            #ficha_posicion=i[0]
            resultado=seleccion_profundidad(tablero,i[0],array_posible_lista)
            if resultado!=0:
                return resultado
    
    tablero[array_solucion[len(array_solucion)-1][0]][array_solucion[len(array_solucion)-1][1]]=0
    array_solucion.pop()
    return 0

intro=0
size_tablero= 0
while intro == 0:
    print("Elija el tamaño del tablero:")
    size_tablero=input()
    if size_tablero.isnumeric():
        intro=1
        size_tablero= int(size_tablero)
    else:
        print("Valor no válido")

tablero = np.zeros((size_tablero, size_tablero))

#ficha_posicion_r=(random.randint(0,3),random.randint(0,3))
ficha_posicion_r=(0,0)
num_paso=1
tablero[ficha_posicion_r[0]][ficha_posicion_r[1]]=num_paso

lista_soluciones = []

print(tablero)

juego=0
array_posible_real=[]
array_solucion=[]
array_posible_real.insert(0,[ficha_posicion_r,(-1,-1)])
seleccion_profundidad(tablero,ficha_posicion_r,array_posible_real)


print("Juego terminado")
if len(lista_soluciones) == 0:
    print("No tiene solucion")
else:
    for i in lista_soluciones:
        pintar_camino(tablero, i)
        print(i)
        #print("Tiempo:",fin-inicio)

        print("Tablero:\n",tablero)


