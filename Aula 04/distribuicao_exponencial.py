# Questão "Cumulativa da distribuição exponencial"

import math

taxa = float(input("Qual a taxa (λ)? "))
x = float(input("Qual x, para calcular F(λ, x)? "))

probabilidade = 1 - math.exp(-taxa*x)
print("{0:.4f}".format(probabilidade))