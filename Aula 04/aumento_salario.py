# Questão "Cálculo de aumento de salário"

def calcula_aumento(salario_atual):
    if (salario_atual <= 1250.00):
        aumento_salario = salario_atual*0.15
    else:
        aumento_salario = salario_atual*0.10

    return aumento_salario