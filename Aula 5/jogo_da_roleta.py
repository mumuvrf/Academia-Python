import random as rnd

dinheiro = 100

while(dinheiro > 0):
    print(f"Você tem {dinheiro} $ disponíveis")
    aposta = int(input("Quanto você gostaria de apostar? "))

    if(aposta == 0): break

    tipo_aposta = input("Qual a modalidade de aposta? [p/n] ")
    num_sorteado = rnd.randint(0, 36)

    if(tipo_aposta.lower() == 'n'):
        numero = int(input("Digite um número de 1 a 36: "))
        if(numero == num_sorteado):
            dinheiro += aposta*35
        else:
            dinheiro -= aposta
    if(tipo_aposta.lower() == 'p'):
        tipo_aposta = input("Par (p) ou ímpar (i)? ")
        if(tipo_aposta.lower() == 'p'):
            if(num_sorteado > 0 and num_sorteado%2 == 0): dinheiro += aposta
            else: dinheiro -= aposta
        elif(tipo_aposta.lower() == 'i'):
            if(num_sorteado%2 != 0): dinheiro += aposta
            else: dinheiro -= aposta