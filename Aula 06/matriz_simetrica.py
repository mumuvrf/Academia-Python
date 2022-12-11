def eh_simetrica(matriz):
    transposta = []
    i = 0
    while(i<len(matriz[0])):
        linha_t = []
        j=0
        while(j<len(matriz)):
            linha_t.append(matriz[j][i])
            j+=1
        transposta.append(linha_t)
        i+=1
    return matriz==transposta