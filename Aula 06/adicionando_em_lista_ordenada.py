def adiciona_em_ordem(nome, distancia, lista_paises):
    novo_pais = [nome, distancia]
    if(lista_paises == []): return [novo_pais]
    for i in range(0, len(lista_paises)):
        if lista_paises[i] == novo_pais:
            return lista_paises
        if lista_paises[i][1] > novo_pais[1]:
            lista_paises.insert(i, novo_pais)
            return lista_paises
    lista_paises.append(novo_pais)
    return lista_paises

lista_paises = [
    ['libia', 3678],
    ['franca', 3998],
    ['siria', 5919]
]
novo_pais = ['india', 9919]

print(adiciona_em_ordem(novo_pais[0], novo_pais[1], lista_paises))