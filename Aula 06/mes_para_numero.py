meses = [
    'janeiro', 'fevereiro', 'março', 'abril',
    'maio', 'junho', 'julho', 'agosto', 'setembro',
    'outubro', 'novembro', 'dezembro'
]

mes = input("Qual o nome do mês? ")

i = 0
while(i < len(meses)):
    if (mes == meses[i]): numero = i+1
    i+=1

print(numero)