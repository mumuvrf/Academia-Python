import math

def mdc(a, b):
    while(a != 0 and b != 0):
        if(a >= b): a = a%b
        elif(b > a): b = b%a

    if(a == 0): return b
    elif(b == 0): return a

def eh_primo(n):
    if(n == 0 or n == 1): return False
    raiz_n = int(math.sqrt(n))
    i = 2

    while(i <= raiz_n):
        if(mdc(n, i) > 1): return False
        i += 1

    return True

def maior_fator_primo(n):
    raiz_n = math.sqrt(n)
    maior_primo = 1
    i = 2

    while(i < raiz_n):
        if(n%i == 0):
            if(eh_primo(n/i)): return n/i
            elif(eh_primo(i)): maior_primo = max(i, maior_primo)
        
        i+=1

    if(maior_primo == 1): return n
    else: return maior_primo

#print(maior_fator_primo(2147483647))