import math

def mdc(a, b):
    if(a == 0): return b
    elif(b == 0): return a

    if(a >= b): return mdc(b, a-b)
    elif(b > a): return mdc(a, b-a)

def eh_primo(n):
    if(n == 0 or n == 1): return False
    i = 2
    raiz_n = int(math.sqrt(n))

    while(i <= raiz_n):
        if(mdc(n, i) > 1): return False
        i+=1

    return True

#print(eh_primo(2))
