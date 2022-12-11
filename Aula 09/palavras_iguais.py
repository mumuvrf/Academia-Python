def palavras_sao_iguais(palavra_composta):
    if('-' in palavra_composta):
        p1, p2 = palavra_composta.split('-')
        if(p1 == p2): return True
        else: return False
    else: return False