tamanho = input()
orcamento = int(input())

if tamanho == 'XP':
    preco = 5
elif tamanho == 'P':
    preco = 7
elif tamanho == 'M':
    preco = 20
elif tamanho == 'G':
    preco = 31
elif tamanho == 'XG':
    preco = 50

bolos = orcamento//preco
troco = orcamento - bolos*preco

if(troco > 0):
    if(bolos > 4):
        if troco//2 > 0:
            print(f"{troco//2} cupcake")
        if troco%2 != 0:
            print(f"{troco%2} banoffee")
    else:
        if troco//2 > 0:
            print(f"{troco//2} cheesecake")
        if troco%2 != 0:
            print(f"{troco%2} brownie")
else:
    print("sem acompanhamento")