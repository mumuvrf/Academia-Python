def eh_identidade(matriz):
    if (len(matriz) != len(matriz[0])): return False
    i = 0
    j = 0

    while(i < len(matriz)):
        while(j < len(matriz[i])):
            if(i != j and matriz[i][j] != 0): return False
            elif(i == j and matriz[i][j] != 1): return False
            j += 1
        j = 0

        i += 1

    return True

#print(eh_identidade([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))