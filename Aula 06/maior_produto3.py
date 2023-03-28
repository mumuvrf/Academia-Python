# Solução com funções embutidas

# def maior_produto3(lista):
#     lista.sort()
#     poss1 = lista[len(lista)-1]*lista[0]*lista[1]
#     poss2 = lista[len(lista)-1]*lista[len(lista)-2]*lista[len(lista)-3]

#     return max(poss1, poss2)



# Solução sem funções embutidas

from math import inf

def maior_produto3(lista):
    maior = 0
    segundo_maior = 0
    terceiro_maior = 0
    menor = inf
    segundo_menor = inf

    i=0
    while i < len(lista):
        if lista[i] > maior:
            terceiro_maior = segundo_maior
            segundo_maior = maior
            maior = lista[i]
        elif lista[i] > segundo_maior:
            terceiro_maior = segundo_maior
            segundo_maior = lista[i]
        elif lista[i] > terceiro_maior:
            terceiro_maior = lista[i]

        if lista[i] < menor:
            segundo_menor = menor
            menor = lista[i]
        elif lista[i] < segundo_menor:
            segundo_menor = lista[i]
        i+=1
    
    prod1 = maior*segundo_maior*terceiro_maior
    prod2 = maior*menor*segundo_menor

    return max(prod1, prod2)

print(maior_produto3([1,2,3,4,5,6]))