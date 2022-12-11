import random as rd

def cria_pecas():
    pecas = []

    for i in range(0, 7):
        for j in range(0, 7):
            if(([i, j] and [j, i]) not in pecas): pecas.append([i, j])

    rd.shuffle(pecas)

    return pecas

# print(cria_pecas())