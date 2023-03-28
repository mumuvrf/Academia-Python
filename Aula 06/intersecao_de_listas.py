def intersecao_de_lista(lista1, lista2):
    i = 0
    intersecao = []
    while i < len(lista1):
        k = 0
        while k < len(lista2):
            if lista1[i] == lista2[k]:
                intersecao.append(lista1[i])
            k+=1
        i+=1
    return intersecao