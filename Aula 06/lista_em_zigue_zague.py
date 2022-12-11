def lista_em_zigue_zague(lista):
    ultimo_menor = False
    ultimo_maior = False
    for i in range(1, len(lista)):
        if(lista[i] < lista[i-1] and ultimo_menor):
            return False
        elif(lista[i] > lista[i-1] and ultimo_maior):
            return False
        elif(lista[i] < lista[i-1]):
            ultimo_menor = True
            ultimo_maior = False
        elif(lista[i] > lista[i-1]):
            ultimo_maior = True
            ultimo_menor = False
        else: return False
    return True

print(lista_em_zigue_zague([50, 3]))