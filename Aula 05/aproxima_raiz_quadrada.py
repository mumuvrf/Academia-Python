import math

def aproxima_raiz(n):
    raiz_menor = int(math.sqrt(n))
    raiz_maior = raiz_menor+1

    if((n - raiz_menor*raiz_menor) > (raiz_maior*raiz_maior - n)): return raiz_maior
    elif((raiz_maior*raiz_maior - n) > (n - raiz_menor*raiz_menor)): return raiz_menor

#print(aproxima_raiz(120))