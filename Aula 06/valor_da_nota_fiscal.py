def calcula_total_da_nota(precos, qnt):
    valor = 0
    for i in range(0, len(precos)):
        valor += precos[i]*qnt[i]
    return valor