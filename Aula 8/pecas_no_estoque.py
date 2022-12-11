def tem_estoque(pecas_necessarias, estoque):
    for peca in pecas_necessarias.keys():
        if peca not in estoque.keys():
            return False
        elif pecas_necessarias[peca] > estoque[peca]:
            return False
    return True