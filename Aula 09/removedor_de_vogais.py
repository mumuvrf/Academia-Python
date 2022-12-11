def remove_vogais(texto):
    sem_vogal = ''
    vogais = set(['a', 'e', 'i', 'o', 'u'])

    for letra in texto:
        if letra.lower() not in vogais:
            sem_vogal += letra

    return sem_vogal

texto = '''
Fortaleza,
Clube de gloria e tradiçao
Fortaleza,
Quantas vezes campeao
Fortaleza,
Querido idolatrado,
Estas sempre guardado
Dentro do meu coraçao.
'''
print(remove_vogais(texto))