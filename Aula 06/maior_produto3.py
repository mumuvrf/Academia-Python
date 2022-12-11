def maior_produto3(lista):
    lista.sort()
    poss1 = lista[len(lista)-1]*lista[0]*lista[1]
    poss2 = lista[len(lista)-1]*lista[len(lista)-2]*lista[len(lista)-3]

    return max(poss1, poss2)

#print(maior_produto3([-10, -20, 20, 1]))