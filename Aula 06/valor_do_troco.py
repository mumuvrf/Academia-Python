def calcula_troco(compra, dinheiro, notas):
    valor_troco = dinheiro - compra
    troco = [ ]

    cont_notas = 0
    
    while(valor_troco > 0):
        i = 0
        while(i < len(notas)):
            if(valor_troco > 2): moeda = "nota(s)"
            else: moeda = "moeda(s)"

            while(valor_troco >= notas[i]):
                valor_troco -= notas[i]
                cont_notas += 1
            if(cont_notas != 0): troco.append(f"{cont_notas} {moeda} de R$ {notas[i]}")
            cont_notas = 0
            
            i+=1   

    return troco

# notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]
# print(calcula_troco(4.5, 10, notas))