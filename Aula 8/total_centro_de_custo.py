def total_centro_custo(gastos_funcionarios):
    gastos_centro = {}
    for funcionario in gastos_funcionarios.keys():
        centro_de_custo = gastos_funcionarios[funcionario]['centro de custo']
        if centro_de_custo not in gastos_centro:
            gastos_centro[centro_de_custo] = 0
        gastos_centro[centro_de_custo] += gastos_funcionarios[funcionario]['valor']
    return gastos_centro

gastos_funcionarios = {
    'Joao Silva': {
        'descricao': 'passagem para auditoria em filial',
        'centro de custo': 'tesouraria',
        'valor': 3000,
    },
    'Silvio Costa': {
        'descricao': 'alimentacao em processo de auditoria',
        'centro de custo': 'tesouraria',
        'valor': 1340.50,
    },
    'Maria Conceicao': {
        'descricao': 'inscricao em congresso internacional',
        'centro de custo': 'presidencia',
        'valor': 7200.00,
    },
    'Marcio Macedo': {
        'descricao': 'copias de memorando',
        'centro de custo': 'producao',
        'valor': 30.80,
    },
    'Marisa Monte Verde': {
        'descricao': 'curso em complaince',
        'centro de custo': 'presidencia',
        'valor': 17800.00,
    }
}
print(total_centro_custo(gastos_funcionarios))