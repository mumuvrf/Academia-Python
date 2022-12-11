def soma_valores(lista):
    tamanho = len(lista)
    soma = 0
    i = 0

    while(i < tamanho):
        soma += lista[i]
        i += 1

    return soma