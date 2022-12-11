def conta_letras(palavra):
    letras_palavra = {}
    for letra in palavra:
        if letra not in letras_palavra:
            letras_palavra[letra] = 1
        else: letras_palavra[letra] += 1
    return letras_palavra

def anagrama(p1, p2):
    qnt_letras_p1 = conta_letras(p1)
    qnt_letras_p2 = conta_letras(p2)

    for letra in qnt_letras_p1.keys():
        if letra not in qnt_letras_p2.keys():
            return False
        elif qnt_letras_p1[letra] != qnt_letras_p2[letra]:
            return False
    return True

# Outra solução possível mas menos eficiente em tempo é a abaixo:

# def anagrama(p1, p2):
#     for letra in p1:
#         if letra not in p2:
#             return False
#         elif p1.count(letra) != p2.count(letra):
#             return False
#     return True

print(anagrama('alegria', 'galeria'))