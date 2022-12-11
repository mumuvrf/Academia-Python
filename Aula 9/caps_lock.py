def capsLock(texto):
    texto_invertido = ''
    i=0
    while(i<len(texto)):
        if(texto[i].upper() == texto[i]):
            texto_invertido += texto[i].lower()
        else:
            texto_invertido += texto[i].upper()
        i+=1
    return texto_invertido