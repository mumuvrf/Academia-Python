def zera_negativos(lista_negativos):
    i = 0
    while(i < len(lista_negativos)):
        if(lista_negativos[i] < 0): lista_negativos[i] = 0
        i+=1

    return lista_negativos