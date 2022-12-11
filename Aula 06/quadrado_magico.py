def quadrado_magico(matriz):
    soma_diagonal_principal = 0
    soma_diagonal_secundaria = 0
    soma_magica = sum(matriz[0])
    for i in range(0, len(matriz)):
        soma_diagonal_principal += matriz[i][i]
        soma_diagonal_secundaria += matriz[i][-i-1]
        soma_linha = 0
        soma_coluna = 0
        for j in range(0, len(matriz[-1])):
            soma_linha += matriz[i][j]
            soma_coluna += matriz[j][i]
        if soma_linha != soma_magica: return False
        elif soma_coluna != soma_magica: return False
    if soma_diagonal_principal != soma_magica: return False
    elif soma_diagonal_secundaria != soma_magica: return False

    return True

print(quadrado_magico([[2, 7, 6],[9, 5, 1],[4, 3, 8]]))