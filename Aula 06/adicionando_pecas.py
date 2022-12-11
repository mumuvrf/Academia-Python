def adiciona_na_mesa(peca, mesa):
    if mesa == []: return [peca]

    nova_mesa = mesa
    if mesa[-1][1] in peca:
        if peca[0] == mesa[-1][1]: nova_mesa.append(peca)
        else: nova_mesa.append([peca[1], peca[0]])
    elif mesa[0][0] in peca:
        nova_mesa = []
        if mesa[0][0] == peca[1]:
            nova_mesa.append(peca)
        else:
            nova_mesa.append([peca[1], peca[0]])
        nova_mesa.extend(mesa)
    return nova_mesa

peca = [1,3]
mesa = [[1,6],[6,6],[6,2]]
print(adiciona_na_mesa(peca, mesa))