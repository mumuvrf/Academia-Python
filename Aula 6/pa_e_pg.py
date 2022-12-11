def verifica_progressao(sequencia):
    pg = True
    pa = True

    if(len(sequencia) <= 2): return 'AG'

    if(sequencia[0] == 0 or sequencia[1] == 0):
        if(sequencia == [0]*len(sequencia)): return 'AG'
        else: pg = False

    i = 2
    while(i < len(sequencia)):
        if(sequencia[i] == 0): pg = False
        
        if pa and ((sequencia[i]-sequencia[i-1]) != (sequencia[i-1]-sequencia[i-2])): pa = False
        if pg and ((sequencia[i]/sequencia[i-1]) != (sequencia[i-1]/sequencia[i-2])): pg = False
        i += 1

    if pg and pa: return 'AG'
    elif pg: return 'PG'
    elif pa: return 'PA'
    else: return 'NA'

#print(verifica_progressao([1, 2, 4, 8, 16, 32, 64, 65]))