import math

def quadrados_no_intervalo(a, b):
    num_quadrados = 0
    raiz_a = int(math.sqrt(a))
    if((math.sqrt(a)-int(math.sqrt(a))) == 0):
        num_quadrados = 1

    raiz_b = int(math.sqrt(b))

    #print(abs(raiz_b-raiz_a))
    num_quadrados += abs(raiz_b-raiz_a)
    return num_quadrados

#print(quadrados_no_intervalo(1, 4))