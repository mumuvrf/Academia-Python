def lista_caracteres(texto):
    lista_letras = []

    for letra in texto:
        if(letra not in lista_letras):
            lista_letras.append(letra)
    return lista_letras