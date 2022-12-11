def aniversariantes_de_setembro(aniversarios):
    setembrinos = {}
    for pessoa in aniversarios.keys():
        if(aniversarios[pessoa][4] == '9'):
            setembrinos[pessoa] = aniversarios[pessoa]
    return setembrinos