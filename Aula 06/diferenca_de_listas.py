def subtracao_de_listas(lista1, lista2):
    dif_listas = []
    i = 0
    while(i < len(lista1)):
        if(lista1[i] not in lista2): dif_listas.append(lista1[i])
        i+=1

    return dif_listas