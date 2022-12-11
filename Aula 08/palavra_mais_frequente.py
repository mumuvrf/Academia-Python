def mais_frequente(lista):
    palavras = {}
    mf = ['palavra', 0]
    for palavra in lista:
        if palavra in palavras:
            palavras[palavra] += 1
        else:
            palavras[palavra] = 1

        if palavras[palavra] > mf[1]:
            mf[0] = palavra
            mf[1] = palavras[palavra]

    return mf[0]

lista = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
print(mais_frequente(lista))