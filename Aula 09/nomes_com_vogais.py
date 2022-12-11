def nomes_com_vogais(lista_nomes):
    vogal_inicia = 0
    consoante_inicia = 0
    vogais = ['A', 'E', 'I', 'O', 'U']

    for nome in lista_nomes:
        if nome[0].upper() in vogais:
            vogal_inicia += 1
        else:
            consoante_inicia += 1

    return [vogal_inicia, consoante_inicia]