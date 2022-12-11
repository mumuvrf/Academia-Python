def promocao_viagens(ranking_destinos):
    destinos_promo = {}
    for destino in ranking_destinos.keys():
        preco_pacote = ranking_destinos[destino][1]
        pos_ranking = ranking_destinos[destino][0]
        destinos_promo[destino] = preco_pacote*((100-pos_ranking*10)/100)

    return destinos_promo

ranking_destinos = {
    "Miami":[1,1000],
    "Ilhas Sandwich do Sul":[4,5000],
    "Barcelona":[2, 2000],
    "Antártica":[5,200],
    "Buenos Aires":[3,500]}

print(promocao_viagens(ranking_destinos))