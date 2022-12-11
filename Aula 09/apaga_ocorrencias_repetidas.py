def apaga_repetidos(texto):
    sem_repetidos = ''
    ja_apareceram = set([])
    
    for letra in texto:
        if letra in ja_apareceram:
            sem_repetidos += '*'
        else:
            sem_repetidos += letra
            ja_apareceram.add(letra)
    return sem_repetidos

print(apaga_repetidos('abacaxi'))