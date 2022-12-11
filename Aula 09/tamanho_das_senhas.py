def tamanho_minimo(senhas, N):
    filtro_senhas = []
    palavras = senhas.split()
    for palavra in palavras:
        if len(palavra) > N:
            filtro_senhas.append(palavra)
    return filtro_senhas