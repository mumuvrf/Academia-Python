def inverte_dicionario(dicionario):
    dicionario_invertido = {}
    for chave in dicionario.keys():
        if dicionario[chave] in dicionario_invertido:
            dicionario_invertido[dicionario[chave]].append(chave)
        else:
            dicionario_invertido[dicionario[chave]] = [chave]
    return dicionario_invertido

dicionario = {'Ana': 19, 'Bruno': 18, 'João': 19}
print(inverte_dicionario(dicionario))