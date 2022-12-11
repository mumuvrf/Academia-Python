# Questão "Empréstimo bancário"

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos_a_pagar = int(input('Em quantos anos você precisa pagar? '))

prestacao = valor_casa/(anos_a_pagar*12)

if(prestacao > 0.30*salario): print('Empréstimo não aprovado')
else: print('Empréstimo aprovado')