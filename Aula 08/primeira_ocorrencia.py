def primeiras_ocorrencias(palavra):
    caracteres = {}
    i = 0
    while(i<len(palavra)):
        if(palavra[i] not in caracteres.keys()): caracteres[palavra[i]] = i
        i+=1

    return caracteres

# print(primeiras_ocorrencias('baila maciel'))