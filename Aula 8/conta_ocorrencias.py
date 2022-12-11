def conta_ocorrencias(lista_palavras):
    ocorrencia_palavra = {}
    for palavra in lista_palavras:
        if(palavra in ocorrencia_palavra): ocorrencia_palavra[palavra] += 1
        else: ocorrencia_palavra[palavra] = 1

    return ocorrencia_palavra