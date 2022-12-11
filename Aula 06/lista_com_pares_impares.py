def verifica_lista(lista):
    so_pares = True
    so_impares = True

    for numero in lista:
        if(numero%2 == 0): so_impares = False
        else: so_pares = False

    if (so_pares and so_impares): return 'misturado'
    elif so_pares: return 'par'
    elif so_impares: return 'ímpar'
    else: return 'misturado'

# lista = [1, 3, 5, 7]
# print(verifica_lista(lista))