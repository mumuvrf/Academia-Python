def estritamente_crescente(lista):
    est_cresc = [ ]

    if(lista == [ ]): return lista
    ult_cresc = lista[0]
    est_cresc.append(lista[0])
    i = 1
    while(i < len(lista)):
        if(lista[i] > ult_cresc):
            ult_cresc = lista[i]
            est_cresc.append(lista[i])
        i += 1

    return est_cresc

#print(estritamente_crescente([1, 3, 2, 3, 4, 6, 5]))