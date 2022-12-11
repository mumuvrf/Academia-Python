catalogo = ['stranger things', 'mad men', 'the circle', 'friends', 'brasileirao', 'champions']

plano = input("Qual seu plano? ")
serie = input("Qual série quer assistir? ")

while(serie.lower() != "sair"):
    if(plano.lower() == 'premium'):
        if(serie.lower() in catalogo): print("Ok, reproduzindo!")
        else: print("Serie inexistente!")
    elif(plano.lower() == 'padrao'):
        if(serie.lower() in catalogo):
            if(serie != 'brasileirao' and serie != 'champions'):
                print("Ok, reproduzindo!")
            else: print("Precisa comprar novo plano!")
        else: print("Serie inexistente!")
    elif(plano.lower() == 'novo'):
        if(serie.lower() in catalogo):
            if(serie == 'mad men' or serie == 'the circle'):
                print("Ok, reproduzindo!")
                print("Num oferecimento de DesSoft!")
            else: print("Precisa comprar novo plano!")
        else: print("Serie inexistente!")

    serie = input("Qual série quer assistir? ")

print("Ok, tchau!")