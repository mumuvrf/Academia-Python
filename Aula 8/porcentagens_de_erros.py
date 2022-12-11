def calcula_porcentagens(erros):
    soma_erros = 0
    for qnt in erros.values(): soma_erros+=qnt
    
    percentual_erros = { }
    for tipo_erro in erros.keys():
        percentual_erros[tipo_erro] = erros[tipo_erro]*100/soma_erros

    return percentual_erros


# erros = {
#     'Erro de indentação': 493,
#     'Erro de parênteses': 1102,
#     'Variável inexistente': 405,
# }
# print(calcula_porcentagens(erros))