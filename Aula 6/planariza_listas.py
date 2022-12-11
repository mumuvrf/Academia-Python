def junta_listas(list_of_lists):
    lista_junta = []

    i = 0
    while(i < len(list_of_lists)):
        j = 0
        while(j < len(list_of_lists[i])):
            lista_junta.append(list_of_lists[i][j])
            j+=1
        i+=1
    
    return lista_junta