import math

def calcula_pi(n):
    pi_quadrado = 0
    i = 1

    while(i <= n):
        pi_quadrado += 6/(math.pow(i, 2))
        i += 1

    return math.sqrt(pi_quadrado)

#print(calcula_pi(1))