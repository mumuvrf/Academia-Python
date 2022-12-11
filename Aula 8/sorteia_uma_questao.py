from random import randint

def sorteia_questao(questoes, nivel):
    n_quest = randint(0, len(questoes[nivel])-1)
    return questoes[nivel][n_quest]