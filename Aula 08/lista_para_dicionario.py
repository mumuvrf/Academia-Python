def monta_dicionario(primeira_lista, segunda_lista):
    dicionario = {}
    i = 0
    while i<len(primeira_lista):
        dicionario[primeira_lista[i]] = segunda_lista[i]
        i+=1
    return dicionario

# esquizos = ['LC', 'Miojo', 'Markin', 'Léo', 'Thiago']
# adjetivos = ['preto', 'gado', 'anão', 'gordo', 'viado']
# print(monta_dicionario(esquizos, adjetivos))