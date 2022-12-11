import math

def mdc(a, b):
    while(a != 0 and b != 0):
        if(a >= b): a = a%b
        elif(b > a): b = b%a

    if(a == 0): return b
    elif(b == 0): return a

def eh_primo(n):
    if(n <= 1): return False
    raiz_n = int(math.sqrt(n))
    i = 2

    while(i <= raiz_n):
        if(mdc(n, i) > 1): return False
        i += 1

    return True

def maior_primo_menor_que(n):
    i = 0
    while(n-i >= 2):
        if(eh_primo(n-i)): return n-i
        i += 1

    return -1

#print(maior_primo_menor_que(2))