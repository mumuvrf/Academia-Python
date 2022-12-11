import math

def mdc(a, b):
    if(a%b == 0): return b
    else: return mdc(max(a, b), min(a%b, b%a))

def eh_primo(numero):
    if(numero < 2): return False

    i = 2
    while(i <= math.sqrt(numero)):
        if(mdc(numero, i) > 1): return False
        i+=1
    return True

def verifica_primos(lista):
    primoounao = {}
    for numero in lista:
        primoounao[numero] = eh_primo(numero)
    return primoounao

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]
# print(verifica_primos(numeros))