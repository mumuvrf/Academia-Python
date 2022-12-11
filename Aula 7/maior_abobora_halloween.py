def maior_abobora(especie, fazendeiros):
    existe_abobora = False
    maior_peso = 0
    ind_maior_peso = 0
    index = 0
    for fazendeiro in fazendeiros:
        for abobora in fazendeiro:
            if ((especie in abobora) and (maior_peso < abobora[0])):
                existe_abobora = True
                maior_peso = abobora[0]
                ind_maior_peso = index
        index+=1

    if existe_abobora: return ind_maior_peso
    else: return -1

# fazendeiros = [
#     [[2.3, 'kabotia']], [[6.2, 'kabotia'], [5.5, 'moranga'], [2.5, 'japonesa'],
#     [1.4, 'moranga']], [[4.2, 'moranga'], [9.2, 'moranga'], [14.2, 'moranga']],
#     [[5.6, 'kabotia'], [16.2, 'kabotia']], 
#     [[5.5, 'japonesa'], [12.2, 'japonesa'], [12.3, 'japonesa']],
#     [[1.2, 'moranga'], [9.2, 'japonesa'], [8.5, 'japonesa']],
# ]

# print(maior_abobora('japonesa', fazendeiros))