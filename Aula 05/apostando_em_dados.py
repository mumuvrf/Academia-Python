import random

def apostando_em_dados(num_sorte, aposta, rodadas):
    i = 0
    while(i < rodadas):
        rolagem = random.randint(1, 6)
        if(num_sorte == rolagem): aposta = (4/3)*aposta
        else: aposta = (5/6)*aposta
        i += 1

    return aposta