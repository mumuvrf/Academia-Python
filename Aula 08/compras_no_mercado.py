def valor_a_devolver(prateleiras, caixa, compras):
    soma_min = 0
    soma_caixa = 0
    for produto in compras:
        custo_prateleiras = prateleiras[produto[0]][produto[1]]
        custo_caixa = caixa[produto[0]][produto[1]]
        soma_min += (min(custo_prateleiras, custo_caixa))*produto[2]
        soma_caixa += custo_caixa*produto[2]


    return soma_caixa-soma_min

prateleiras = {
    'requeijão': {
        'Minas': 5,
        'Buritis': 6,
        'Queijinho': 7 
    },
    'sabão': {
        'Pura Espuma': 10,
        'Lavagem Perfeita': 12.5,
        'Cromo': 15.7
    },
    'arroz': {
        'Prato Fundo': 20,
        'Tio José': 23,
        'Cadez': 25
    },
    'macarrão': {
        'Sandra': 2,
        'Massa Nobre': 4,
        'Urbano': 5.3
    }
}
caixa = {
    'requeijão': {
        'Minas': 5,
        'Buritis': 7,
        'Queijinho': 7 
    },
    'sabão': {
        'Pura Espuma': 10.5,
        'Lavagem Perfeita': 12.8,
        'Cromo': 15.7
    },
    'arroz': {
        'Prato Fundo': 20,
        'Tio José': 23,
        'Cadez': 26
    },
    'macarrão': {
        'Sandra': 2,
        'Massa Nobre': 4.5,
        'Urbano': 5.3
    }
}
compras = [
    ['arroz','Prato Fundo',1],
    ['requeijão','Buritis',2],
    ['requeijão','Queijinho',1],
    ['sabão','Pura Espuma',3]
]
print(valor_a_devolver(prateleiras, caixa, compras))