# Questão "Classificador de triângulos"

def classifica_triangulo(a, b, c):
    if(a == b and b == c): return "equilátero"
    elif(a == b or b == c or a == c): return "isósceles"
    else: return "escaleno"