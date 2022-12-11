def soma_valor_ativos(empresa, info_empresas):
    valor_ativos = 0
    for ativo in info_empresas[empresa]['ativos'].keys():
        pct_invest = info_empresas[empresa]['ativos'][ativo]
        valor_de_mercado = info_empresas[ativo]['valor de mercado']
        valor_ativos += valor_de_mercado*(pct_invest/100)
        valor_ativos += soma_valor_ativos(ativo, info_empresas)*(pct_invest/100)
    return valor_ativos

def soma_investimento(info_empresas):
    info_investidores = {}
    nome_empresas = set([x for x in info_empresas.keys()])

    for empresa in info_empresas.keys():
        if 'ativos' not in info_empresas[empresa]:
            info_empresas[empresa]['ativos'] = {}
        for associado in info_empresas[empresa]['associados'].keys():
            if associado in nome_empresas:
                if 'ativos' not in info_empresas[associado]:
                    info_empresas[associado]['ativos'] = {}
                info_empresas[associado]['ativos'][empresa] = info_empresas[empresa]['associados'][associado]

    for empresa in info_empresas.keys():
        valor_de_mercado = info_empresas[empresa]['valor de mercado']
        for pessoa in info_empresas[empresa]['associados'].keys():
            if pessoa not in nome_empresas:
                pct_invest = info_empresas[empresa]['associados'][pessoa]

                if pessoa not in info_investidores: info_investidores[pessoa] = 0
                info_investidores[pessoa] += valor_de_mercado*(pct_invest/100)
                valor_ativos = soma_valor_ativos(empresa, info_empresas)
                info_investidores[pessoa] += valor_ativos*(pct_invest/100)

    return info_investidores

info_empresas = {
    'acme corporation inc': {
        'valor de mercado': 4560000.00,
        'associados': {
            'joao silva matoso': 30,   # 30% da empresa
            'maria santana alves': 70  # 70% da empresa
        }
    },
    'insper solid investiment': {
        'valor de mercado': 8950000.00,
        'associados': {
            'maciel fina pessoa': 10,  # 10% da empresa
            'insper junior ltda': 80,  # 80% da empresa
            'marcio massado': 5,       # 5% da empresa
            'jair designa broncado': 5 # 5% da empresa
        }
    },
    'insper junior ltda':  {
        'valor de mercado': 40200100.00,
        'associados': {
            'maciel fina pessoa': 20, # 20% da empresa
            'joao silva matoso': 30,  # 30% da empresa
            'dario finado': 40,       # 40% da empresa
            'acme corporation inc': 10 # 10% da empresa
        }
    }
}
print(soma_investimento(info_empresas))