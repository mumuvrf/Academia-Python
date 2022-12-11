def melhor_valor(partes, inventario):
    gastos = 0
    for serial in partes:
        menor_preco = None
        for item in inventario:
            if item['serial'] == serial or serial in item['equivalente']:
                if menor_preco == None:
                    menor_preco = item['valor']
                else: menor_preco = min(menor_preco, item['valor'])
        if menor_preco != None: gastos += menor_preco

    return gastos

partes = ['X1D', 'A3B']
inventario = [
    {'serial': 'A3B', 'valor': 198.7, 'equivalente': []},
    {'serial': 'XP2', 'valor': 190.9, 'equivalente': ['Z3Z', 'A3D']},
    {'serial': 'XP1', 'valor':   5.1, 'equivalente': ['TH5', 'TH6', 'X3D', 'X1D']}
]
print(melhor_valor(partes, inventario))