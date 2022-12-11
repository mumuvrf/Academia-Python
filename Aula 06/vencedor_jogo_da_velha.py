def verifica_jogo_da_velha(tabuleiro):
    venceu_diagonal_principal = True
    venceu_diagonal_secundaria = True
    for i in range(0, len(tabuleiro)):
        venceu_coluna = True
        venceu_linha = True
        if i != 0:
            if tabuleiro[i][i] != tabuleiro[i-1][i-1]:
                venceu_diagonal_principal = False
            if tabuleiro[i][-i-1] != tabuleiro[i-1][-i]:
                venceu_diagonal_secundaria = False
        for j in range(0, len(tabuleiro[0])):
            if j!=0:
                if tabuleiro[j][i] != tabuleiro[j-1][i]:
                    venceu_coluna = False

                if tabuleiro[i][j] != tabuleiro[i][j-1]:
                    venceu_linha = False
        if venceu_coluna:
            return tabuleiro[0][i]
        
        if venceu_linha:
            return tabuleiro[i][0]
    if venceu_diagonal_principal:
        return tabuleiro[0][0]
    
    if venceu_diagonal_secundaria:
        return tabuleiro[0][-1]

    return 'V'

tabuleiro = [
    ['X', 'O', 'X'],
    ['.', 'O', 'X'],
    ['O', '.', 'X']
]
print(verifica_jogo_da_velha(tabuleiro))