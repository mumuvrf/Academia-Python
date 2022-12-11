def interseccao_valores(d1, d2):
    valores_comuns = []
    for chave in d1:
        if d1[chave] in d2.values():
            valores_comuns.append(d1[chave])

    return valores_comuns