def posicoes_possiveis(mesa, pecas):
    posicoes = []

    if(len(mesa) > 0):
        pontas = [mesa[0][0], mesa[-1][1]]
        index = 0

        for peca in pecas:
            for numero in peca:
                if((numero in pontas) and (index not in posicoes)): posicoes.append(index)
            
            index += 1
    else:
        for i in range(0, len(pecas)): posicoes.append(i)

    return posicoes

# mesa = [
#     [0,2],[2,1],[1,6],[6,5],[5,3]
# ]
# pecas = [
#     [1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6]
# ]

# print(posicoes_possiveis(mesa, pecas))