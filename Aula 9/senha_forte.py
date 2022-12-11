def valida_senha(senha):
    caracteres_especiais = ['?', '!', '@', '#', '$', '%', '&', '*']
    espinpalavra = []

    i = 0
    while(i < len(senha)):
        if(i > 0 and senha[i] == senha[i-1]): return False
        if(senha[i] in caracteres_especiais and senha[i] not in espinpalavra): espinpalavra.append(senha[i])

        i+=1
    return len(senha) >= 8 and len(espinpalavra) > 1