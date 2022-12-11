def calcula_escola(desempenho_escola):
    soma = 0
    for quesito in desempenho_escola:
        soma+= sum(quesito)-min(quesito)
    return soma