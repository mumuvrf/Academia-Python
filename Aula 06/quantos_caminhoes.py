def quantos_caminhoes(produtos):
    peso_total = 0
    n_caminhoes = 0
    for peso in produtos:
        if(peso > peso_total):
            peso_total = 2000 - peso
            n_caminhoes += 1
        else: peso_total -= peso

    return n_caminhoes

# lista = [1000, 500, 400, 200, 50, 450, 1300, 500, 1450, 100]

# print(quantos_caminhoes(lista))