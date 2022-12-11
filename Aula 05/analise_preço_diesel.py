dias = int(input("Quantos dias você gostaria de analisar? "))

if(dias >= 1):
    preco_dia = float(input())
    menor_preco = preco_dia
    maior_preco = preco_dia
    soma = preco_dia
    melhor_dia = 1
    pior_dia = 1

i=2
while(i <= dias):
    preco_dia = float(input())

    soma += preco_dia
    if(preco_dia < menor_preco):
        menor_preco = preco_dia
        melhor_dia = i
    elif(maior_preco < preco_dia):
        maior_preco = preco_dia
        pior_dia = i

    i+=1

if(dias != 0): media = soma/dias

print(f"O dia {melhor_dia} foi o melhor dia para compra")
print(f"O dia {pior_dia} foi o pior dia para compra")
print(f"O preço médio cobrado foi de {media:.2f}")