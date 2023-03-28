def alunos_impares(nomes):
    i = 1
    impares = []
    while i < len(nomes):
        impares.append(nomes[i])
        i+=2
    return impares