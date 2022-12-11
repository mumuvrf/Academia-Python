def mais_medalhas(medalha, quadro_medalhas):
    filtro = {}
    maior_numero = 0
    for pais in quadro_medalhas.keys():
        if quadro_medalhas[pais][medalha] > maior_numero:
            maior_numero = quadro_medalhas[pais][medalha]

    for pais in quadro_medalhas.keys():
        if quadro_medalhas[pais][medalha] == maior_numero:
            filtro[pais] = quadro_medalhas[pais]
    return filtro

def pais_campeao(quadro_medalhas):
    maiores_medalhistas = mais_medalhas('ouro', quadro_medalhas)
    if len(maiores_medalhistas.keys()) > 1:
        maiores_medalhistas = mais_medalhas('prata', maiores_medalhistas)
        if len(maiores_medalhistas.keys()) > 1:
            maiores_medalhistas = mais_medalhas('bronze', maiores_medalhistas)
    
    return list(maiores_medalhistas.keys())[0]

quadro_medalhas = {
        'China': {
        'ouro': 20,
        'prata': 35,
        'bronze': 40 
    },
    'Canadá': {
        'ouro': 5,
        'prata': 15,
        'bronze': 20
    },
    'Estados Unidos': {
        'ouro': 25,
        'prata': 30,
        'bronze': 40
    },
    'Brasil': {
        'ouro': 10,
        'prata': 10,
        'bronze': 8
    }
}
print(pais_campeao(quadro_medalhas))