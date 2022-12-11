# Questão "IRRF"

salario_bruto = float(input("Informe seu salário bruto: "))
dependentes = int(input("Qual o número de dependentes? "))

if(salario_bruto <= 1045): contribuicao_inss = salario_bruto*0.075
elif(salario_bruto <= 2089.60): contribuicao_inss = salario_bruto*0.09
elif(salario_bruto <= 3134.40): contribuicao_inss = salario_bruto*0.12
elif(salario_bruto <= 6101.06): contribuicao_inss = salario_bruto*0.14
else: contribuicao_inss = 671.12

base_calculo = salario_bruto - contribuicao_inss - dependentes*189.59

if(base_calculo <= 1903.98): irrf = 0
elif(base_calculo <= 2826.65): irrf = base_calculo*0.075 - 142.80
elif(base_calculo <= 3751.05): irrf = base_calculo*0.15 - 354.80
elif(base_calculo <= 4664.68): irrf = base_calculo*0.225 - 636.13
else: irrf = base_calculo*0.275 - 869.36

print(irrf)
