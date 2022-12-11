numero_bananas = 0

with open("Aula 10/macacos-me-mordam.txt") as macacada:
    linhas = macacada.readlines()
    for linha in linhas:
        palavras = linha.split()
        for palavra in palavras:
            if(palavra.lower() == 'banana'): numero_bananas += 1

print(numero_bananas)