import math

def calcula_tempo(aceleracao_atletas):
    tempo_atletas = {}
    for atleta in aceleracao_atletas.keys():
        tempo_atletas[atleta] = math.sqrt(2*100/aceleracao_atletas[atleta])

    return tempo_atletas


dados_corrida = {}
while(True):
    nome = input()
    if(nome == 'sair'): break
    aceleracao = float(input())

    dados_corrida[nome] = aceleracao

dados_corrida = calcula_tempo(dados_corrida)

vencedor = ['atleta', -1]
for atleta in dados_corrida.keys():
    if(dados_corrida[atleta] < vencedor[1] or vencedor[1] == -1):
        vencedor[0] = atleta
        vencedor[1] = dados_corrida[atleta]

print(f"O vencedor é {vencedor[0]} com tempo de conclusão de {vencedor[1]} s")