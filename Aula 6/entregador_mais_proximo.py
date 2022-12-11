from math import *

def entregador_mais_proximo(restaurante, entregadores):
    emp = [-1, -1]
    i = 0
    while(i<len(entregadores)):
        distancia = sqrt((entregadores[i][0]-restaurante[0])**2 + (entregadores[i][1]-restaurante[1])**2)
        if(emp[1] == -1 or distancia < emp[1]):
            emp = [i, distancia]
        i+=1

    return emp[0]

restaurante = [3, 4]
entregadores = [
    [10, 20],
    [4, 2],
    [100, 74],
    [23, 63]
]
print(entregador_mais_proximo(restaurante, entregadores))