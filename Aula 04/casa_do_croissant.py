from math import ceil

dia = input("Qual o dia da semana?[2/3/4/5/6/sabado/domingo]")
salgados = int(input("Quantos croissants salgados você deseja?"))
doces = int(input("Quantos croissants doces você deseja? "))
viagem = input("Vai levar para viagem? [s/n]")

preco = 0
if(viagem.lower() == 's'):
    preco += 3.90*ceil((salgados+doces)/4)

if(dia == '2' or dia == '4'):
    brindes = salgados//4
    if(doces >= brindes):
        doces -= brindes
    else:
        salgados -= (salgados - 4*doces)//5
        doces = 0

preco += salgados*9.0 + doces*5.0
print(f"{preco:.2f}")