numeros = []
numeros_invertido = []

valor = int(input("Digite um inteiro positivo: "))
while(valor > 0):
    numeros.append(valor)
    valor = int(input("Digite um inteiro positivo: "))

i=1
while(i <= len(numeros)):
    numeros_invertido.append(numeros[-i])
    i += 1

print(numeros_invertido)