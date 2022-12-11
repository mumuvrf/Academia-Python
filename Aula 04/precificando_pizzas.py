# Questão "Precificando Pizzas"

tamanho = input("Tamanho [P/M/G]? ")
if(tamanho.upper() == "P"): preco_base = 50.0
elif(tamanho.upper() == "M"): preco_base = 70.0
else: preco_base = 90.0

preco = preco_base

borda_recheada = input("Borda recheada [S/N]? ")
if(borda_recheada.upper() == "S"): preco += preco_base*0.15

adicional_queijo = input("Adicional de queijo [S/N]? ")
if(adicional_queijo.upper() == "S"): preco += preco_base*0.10

refrigerante = input("Refrigerante [S/N]? ")
if(refrigerante.upper() == "S"): preco += 12

sobremesa = input("Sobremesa [S/N]? ")
if(sobremesa.upper() == "S"):
    preco += 20
    if(tamanho.upper() == "G"): preco -= preco*0.07

print("{0:.2f}".format(preco))