def apurando_votos(candidatos, votos):
    contagem = [0]*len(candidatos)
    invalido = 0
    for voto in votos:
        if voto in candidatos:
            contagem[candidatos.index(voto)] += 1
        else:
            invalido += 1
    if max(contagem) > invalido:
        return candidatos[contagem.index(max(contagem))]
    else: return 'CANCELADA'

candidatos = ['Maria', 'Joana', 'Marcos', 'Paulo', 'Joaquim']
votos = [
    'Maria', 'Joaquim', 'Joaquim', 'Joana', 'Marcos',
    'Silvio', 'Marcos', 'Joana', 'Joana', 'Maria',
    'Maria', 'Joana', 'Marcos', 'Joaquim', 'Joana',
    'Joana', 'Lucas'
]
print(apurando_votos(candidatos, votos))