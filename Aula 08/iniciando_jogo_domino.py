def inicia_jogo(n_jog, pecas):
    estado_inicial = {
        'jogadores':{},
        'monte':[],
        'mesa':[]
    }
    for i in range(0, n_jog):
        estado_inicial['jogadores'][i] = []
        for j in range(0, 7):
            estado_inicial['jogadores'][i].append(pecas[i*7+j])
    
    for k in range(n_jog*7, len(pecas)):
        estado_inicial['monte'].append(pecas[k])
    return estado_inicial

n_jog = 2
pecas = [
    [1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6],
	[1,1],[1,2],[0,0],[1,4],[1,5],[1,6],[2,2],
	[3,6],[2,4],[2,5],[2,6],[3,3],[3,4],[2,3],
	[3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]
]

print(inicia_jogo(n_jog, pecas))