def interseccao_chaves(d1, d2):
    chaves_comuns = []
    for chave in d1.keys():
        if chave in d2: chaves_comuns.append(chave)
    return chaves_comuns