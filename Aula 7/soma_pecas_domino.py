def soma_pecas(pecas):
    pontos = 0
    for peca in pecas:
        for num_face in peca: pontos += num_face
    return pontos

# pecas = [
#     [1,0],[2,3],[6,6]
# ]

# print(soma_pecas(pecas))