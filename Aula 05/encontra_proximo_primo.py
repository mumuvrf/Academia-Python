from math import sqrt

def mdc(x, y):
    if(x >= y): a, b = x, y
    else: a, b = y, x

    if(b != 0):
        return mdc(b, a%b)
    else:
        return a
    
def eh_primo(n):
    i = 1
    while(i <= sqrt(n)):
        if mdc(n, i) != 1:
            return False
        i+=1
    return True

def proximo_primo(n):
    k = n+1
    if n == 0: return 2
    while True:
        if eh_primo(k):
            return k
        k+=1
