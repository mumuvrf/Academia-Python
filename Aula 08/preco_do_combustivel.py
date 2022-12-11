def contabiliza_combustivel(gastos_dia):
    info_comb = {}
    custos_comb = {}
    for dia in gastos_dia.keys():
        tipo = gastos_dia[dia]['tipo']
        if tipo not in info_comb:
            info_comb[tipo] = {
                'total litros': 0,
                'custo por litro': 0
            }
        info_comb[tipo]['total litros'] += gastos_dia[dia]['litros']

        if tipo not in custos_comb:
            custos_comb[tipo] = 0
        custos_comb[tipo] += gastos_dia[dia]['custo']
    
    for tipo in info_comb.keys():
        info_comb[tipo]['custo por litro'] = custos_comb[tipo]/info_comb[tipo]['total litros']
    return info_comb


gastos_dia = {
    'dia 3': {
        'tipo': 'Ar',
        'litros': 100,
        'custo': 20.0
    },
    'dia 5': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 175.0
    },
    'dia 20': {
        'tipo': 'Ar',
        'litros': 50,
        'custo': 10.0
    }
}
print(contabiliza_combustivel(gastos_dia))