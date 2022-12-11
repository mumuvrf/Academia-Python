def pedra_papel_tesoura(primeiro, segundo):
    if(primeiro == "papel"):
        if(segundo == "tesoura"): return "dois"
        elif(segundo == "pedra"): return "um"
        elif(segundo == "papel"): return "empate"
        else: return "Escolha pedra, papel ou tesoura para jogar"
    elif(primeiro == "tesoura"):
        if(segundo == "tesoura"): return "empate"
        elif(segundo == "pedra"): return "dois"
        elif(segundo == "papel"): return "um"
        else: return "Escolha pedra, papel ou tesoura para jogar"
    elif(primeiro == "pedra"):
        if(segundo == "tesoura"): return "um"
        elif(segundo == "pedra"): return "empate"
        elif(segundo == "papel"): return "dois"
        else: return "Escolha pedra, papel ou tesoura para jogar"
    else: return "Escolha pedra, papel ou tesoura para jogar"

#print(pedra_papel_tesoura("spock", "lagarto"))