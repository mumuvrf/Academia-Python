def busca_restaurantes(restaurantes, categoria, valor):
    if categoria == 'culinaria':
        posicao = 1
    elif categoria == 'ambiente':
        posicao = 2
    elif categoria == 'preco':
        posicao = 3

    resultados = []


    i = 0
    while i < len(restaurantes):
        eh_valor_cat = posicao != 3 and restaurantes[i][posicao] == valor
        eh_valor_preco = posicao == 3 and restaurantes[i][posicao] <= valor

        if eh_valor_cat or eh_valor_preco:
            resultados.append(restaurantes[i][0])
        i += 1
    return resultados

# restaurantes = [
#     ["Ristorante Italiano", "Italiano", "Elegante", 80],
#     ["Cantina Mexicana", "Mexicano", "Descontraído", 50],
#     ["Sushi Bar Japonês", "Japonês", "Sofisticado", 120],
#     ["Comida Vegana", "Vegano", "Alternativo", 60],
#     ["Lanchonete do Zé", "Fast-food", "Popular", 20]
# ]
# busca_por = 'preco'
# valor = 50
# print(busca_restaurantes(restaurantes, busca_por, valor))