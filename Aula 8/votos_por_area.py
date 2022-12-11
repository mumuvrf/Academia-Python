def apura_area(secoes, candidatos_partidos):
    partidos_candidatos = {}
    for partido in candidatos_partidos.keys():
        for candidato in candidatos_partidos[partido]:
            partidos_candidatos[candidato] = partido
    partidos_candidatos['nulos'] = 'nulos'
    
    votos_area = {}
    for secao in secoes:
        if secao['area'] not in votos_area:
            votos_area[secao['area']] = {}
        for candidato in secao['candidatos'].keys():
            if candidato in partidos_candidatos.keys(): index = partidos_candidatos[candidato]
            else: index = 'brancos'
                
            if index not in votos_area[secao['area']]:
                votos_area[secao['area']][index] = secao['candidatos'][candidato]
            else:
                votos_area[secao['area']][index] += secao['candidatos'][candidato]
    return votos_area

secoes = [
    {
        'secao': 102,
        'area': 'litoral',
        'candidatos': {
            'ze da esquina': 159,
            'maria do milagre': 231,
            'nulos': 43,
            'brancos': 43
        }
    },
    {
        'secao': 103,
        'area': 'litoral',
        'candidatos': {
            'ze da esquina': 432,
            'maria do milagre': 965,
            'nulos': 63,
            'brancos': 86
        }
    },
    {
        'secao': 431,
        'area': 'capital',
        'candidatos': {
            'tiao da borracharia': 723,
            'maria do milagre': 812,
            'nulos': 3,
            'brancos': 36
        }
    }
]

partidos = {
    'fdb': ['tiao da borracharia', 'frederico ganhador', 'zelia despachante'],
    'ipdt': ['ze da esquina', 'maria do milagre'],
}

print(apura_area(secoes, partidos))