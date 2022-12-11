def numero_no_indice(numeros):
    num_ig_indice = []
    
    i = 0
    while(i < len(numeros)):
        if(numeros[i] == i): num_ig_indice.append(numeros[i])
        i+=1

    return num_ig_indice