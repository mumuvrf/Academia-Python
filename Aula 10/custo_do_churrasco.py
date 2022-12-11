custo_churras = 0

with open("Aula 10/churras.txt") as valores_itens:
    linhas = valores_itens.readlines()
    for linha in linhas:
        nome, quantidade, valor = linha.split(',')
        quantidade = int(quantidade)
        valor = float(valor)

        custo_churras += quantidade*valor

print(custo_churras)