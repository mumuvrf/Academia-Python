def classifica_trigo(defeitos):
    classificacao = []

    for medicao in defeitos:
        if(medicao > 7): classificacao.append('FT')
        elif(medicao > 3): classificacao.append('T3')
        elif(medicao > 2): classificacao.append('T2')
        else: classificacao.append('T1')

    return classificacao