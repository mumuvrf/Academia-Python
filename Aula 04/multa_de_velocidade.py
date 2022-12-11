# Questão "Multa de velocidade"

velocidade = float(input("Qual a velocidade reportada? "))

if(velocidade > 80):
    multa = (velocidade-80)*5
    print("{0:.2f}".format(multa))
else: print("Não foi multado")
