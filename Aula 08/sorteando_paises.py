from random import choice

def sorteia_pais(info_paises):
    lista_chaves = [x for x in info_paises.keys()]
    pais = choice(lista_chaves)
    return pais

info_paises = {
    'brasil': 'penta',
    'frança': 'tri',
    'alemanha': 'tetra',
    'inglaterra': 'KKKKKKKK'
}
print(sorteia_pais(info_paises))