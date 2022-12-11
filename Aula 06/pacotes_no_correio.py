def pacotes_correio(remessa):
    total_pacotes = remessa[0][0]
    tamanho_padrao = remessa[0][2]
    ultimo_id = 0

    for i in range(0, len(remessa)):
        if remessa[i][1] <= ultimo_id:
            return 'ordem errada'
        elif remessa[i][2] != tamanho_padrao:
            return 'tamanho errado'
        ultimo_id = remessa[i][1]
    
    if len(remessa) < total_pacotes:
        return 'pacote perdido'
    
    return 'tudo certo'

print(pacotes_correio([[4,1,20],[4,2,20],[4,4,20]]))