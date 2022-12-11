def calcula_overbooking(capacidade, lista):
    excesso = 0
    for pass_voo in lista:
        excesso += max(0, pass_voo-capacidade)

    return excesso

capacidade = 136
lista = [90, 165, 137, 0, 147, 150]
print(calcula_overbooking(capacidade, lista))