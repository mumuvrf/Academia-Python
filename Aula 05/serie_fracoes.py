import math

def calcula_serie(a, b, n):
    soma = 1
    i = b

    while(i <= (n-1)*b):
        soma += math.pow(a, -i)
        i += b

    return soma

#print(calcula_serie(2, 1, 100))