import math

def calcula_investimento(invest_inicial, meses, nome_ativo):
    if(nome_ativo == "LCI"):
        valor = invest_inicial*math.pow(1.016, meses)
    elif(nome_ativo == "LCA"):
        i = 1
        valor = invest_inicial
        while(i <= meses):
            valor = valor*1.0145
            if(i%4 == 0): valor = valor*1.01
            i += 1
    elif(nome_ativo == "CDB"):
        i = 1
        valor = invest_inicial
        while(i <= meses):
            valor = valor*1.013
            if(i%6 == 0): valor = valor*1.012
            i += 1

    return valor

#print(calcula_investimento(1000, 7, 'LCA'))