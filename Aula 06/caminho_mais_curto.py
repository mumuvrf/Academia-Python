from math import *

def caminho_mais_curto(lista_caminhos):
    menor_distancia = -1
    menor_caminho = []
    for caminho in lista_caminhos:
        distancia = 0
        for i in range(1, len(caminho)):
            distancia += sqrt((caminho[i][0]-caminho[i-1][0])**2+(caminho[i][1]-caminho[i-1][1])**2)
        if menor_distancia == -1 or menor_distancia > distancia:
            menor_distancia = distancia
            menor_caminho = caminho
    return menor_caminho

lista_caminhos = [
    [[5, 2], [3, 7], [7, 3], [10, 4]],
    [[5, 2], [300, 1000], [10, 4]],
]
print(caminho_mais_curto(lista_caminhos))