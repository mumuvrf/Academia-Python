numero_palavras = 0

with open('Aula 10/texto.txt') as texto:
    linhas = texto.readlines()
    for linha in linhas:
        palavras = linha.split()
        numero_palavras += len(palavras)

print(numero_palavras)