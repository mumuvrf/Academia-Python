# Questão "Preço do Frete de um Pedido"

def calcula_frete(valor_total, quantidade_itens, sao_frageis, distancia):
    valor_base = 12.75
    frete_km = 1.82
    aliquota_fragil = 0.0175
    aliquota_padrao = 0.008
    
    numero_caixas = quantidade_itens//40
    if(quantidade_itens%40 != 0): numero_caixas += 1

    valor_frete = valor_base + numero_caixas*frete_km*distancia

    if(sao_frageis.upper() == "S"): valor_frete += valor_total*aliquota_fragil
    else: valor_frete += valor_total*aliquota_padrao

    return valor_frete

#print(calcula_frete(50, 121, "S", 150))