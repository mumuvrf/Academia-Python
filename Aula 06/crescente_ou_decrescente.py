def classifica_lista(lista):
    if(len(lista) < 2): return 'nenhum'
    crescente = True
    decrescente = True

    i = 1
    while(i < len(lista)):
        if(lista[i] < lista[i-1]): crescente = False
        if(lista[i] > lista[i-1]): decrescente = False
        i+=1

    if crescente: return 'crescente'
    elif decrescente: return 'decrescente'
    else: return 'nenhum'

#print(classifica_lista([1, 2, 3, 5, 9, 12, 51]))