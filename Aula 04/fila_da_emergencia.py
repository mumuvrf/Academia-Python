# Questão "Fila da Emergência"

classificacao = input("Classificação? (V/A/L)")
numero_vermelhos = int(input("Quantos Vermelhos estão aguardando?"))
tempo = numero_vermelhos*7

numero_laranjas = int(input("Quantos Laranjas estão aguardando?"))
if(classificacao.upper() != "V"): tempo += numero_laranjas*5

numero_azuis = int(input("Quantos Azuis estão aguardando?"))
if(classificacao.upper() == "A"): tempo += numero_azuis*5

print(tempo)