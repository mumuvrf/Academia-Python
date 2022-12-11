def encontra_maximo(matriz):
    max_linhas = []
    min_linhas = []
    i = 0
    while(i < len(matriz)):
        max_linhas.append(max(matriz[i]))
        min_linhas.append(min(matriz[i]))
        i += 1

    return max(max(max_linhas), abs(min(min_linhas)))

# matriz = [
#     [-1, -2, -3], [-4, -5, -6], [-7, -8, -9]
# ]

# print(encontra_maximo(matriz))