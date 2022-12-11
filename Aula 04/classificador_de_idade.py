# Questão "Classificador de idade"

def classifica_idade(idade):
    if(idade <= 11): return 'crianca'
    elif(idade < 18): return 'adolescente'
    else: return 'adulto'