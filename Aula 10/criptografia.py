descodificado = []
codigo = {'s':'z', 'a':'e', 'r':'b', 'b':'r', 'e':'a', 'z':'s'}

with open("Aula 10/criptografado.txt", 'r') as criptografado:
    linhas_cripto = criptografado.readlines()
    for i in range(0, len(linhas_cripto)):
        descodificado.append('')
        for letra in linhas_cripto[i]:
            if letra in codigo.keys():
                descodificado[i] += codigo[letra]
            else:
                descodificado[i] += letra

# with open("Aula 10/criptografado.txt", 'w') as criptografado:
#     criptografado.writelines(descodificado)

for linha in descodificado:
    print(linha)