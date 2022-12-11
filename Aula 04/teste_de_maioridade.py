# Questão "Teste de maioridade"

def verifica_idade(idade):
    if(idade < 18): return("Não está liberado")
    elif(idade < 21): return("Liberado BRASIL")
    else: return("Liberado EUA e BRASIL")