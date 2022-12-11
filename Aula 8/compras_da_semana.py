def compras_da_semana(livro_receitas, pratos):
    ingredientes = {}
    for receita in pratos:
        for ingrediente in livro_receitas[receita].keys():
            if(ingrediente in ingredientes): ingredientes[ingrediente] += livro_receitas[receita][ingrediente]
            else: ingredientes[ingrediente] = livro_receitas[receita][ingrediente]

    return ingredientes

# livro_receitas = {
#         'Bolo de chocolate': {
#         'Leite': 0.25,
#         'Óleo': 0.25,
#         'Ovo': 2.0,
#         'Farinha': 0.5,
#         'Açúcar': 0.2,
#         'Achocolatado': 0.3
#     },
#     'Bolinho de chuva': {
#         'Óleo': 1.0,
#         'Leite': 0.3,
#         'Ovo': 3.0,
#         'Farinha': 0.6,
#         'Açúcar': 0.3
#     },
#     'Mingau': {
#         'Açúcar': 0.1,
#         'Maizena': 0.1,
#         'Leite': 0.25
#     }
# }

# pratos = ['Bolinho de chuva', 'Bolo de chocolate', 'Bolinho de chuva']
# print(compras_da_semana(livro_receitas, pratos))