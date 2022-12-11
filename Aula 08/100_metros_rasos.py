import math

def calcula_tempo(aceleracao_atletas):
    tempo_atletas = {}
    for atleta in aceleracao_atletas.keys():
        tempo_atletas[atleta] = math.sqrt(2*100/aceleracao_atletas[atleta])

    return tempo_atletas

# atletas = {'samuel':1.5, 'ph':1.7, 'vinicius':1.2}
# print(calcula_tempo(atletas))