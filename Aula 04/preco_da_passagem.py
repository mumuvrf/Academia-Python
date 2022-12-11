# Questão "Preço da passagem"

distancia = int(input('Qual distância deseja percorrer (em km)? '))

if (distancia <= 200):
    preco = distancia*0.50
else:
    preco = 100 + (distancia-200)*0.45

print('{0:.2f}'.format(preco))