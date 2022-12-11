n_dias = int(input())

soma = 0
i = 0

while(i < n_dias):
    preco_atual = float(input())
    soma += preco_atual
    i += 1

media = soma/n_dias

print("O preço médio cobrado foi de {0:.2f}".format(media))