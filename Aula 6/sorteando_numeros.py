from random import choice

def distribuir(n, lista_numeros):
    cartela = []
    for i in range(0, n):
        novo_numero = choice(lista_numeros)
        while novo_numero in cartela:
            novo_numero = choice(lista_numeros)
        cartela.append(novo_numero)
    return cartela

lista_numeros = [10, 1, 5, 6, 9, 15, 2]
print(distribuir(4, lista_numeros))