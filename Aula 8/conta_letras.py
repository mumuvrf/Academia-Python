def conta_letras(texto):
    frequencia_letras = {}
    for letra in texto:
        if(letra in frequencia_letras):
            frequencia_letras[letra] += 1
        else:
            frequencia_letras[letra] = 1
    return frequencia_letras