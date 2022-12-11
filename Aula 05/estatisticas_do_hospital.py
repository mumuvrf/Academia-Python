criancas = 0
adolescentes = 0
jovens_adultos = 0
adultos = 0
meia_idade = 0
idosos = 0
total = 0

idade_atual = int(input())

while(idade_atual >= 0):
    total += 1
    if(idade_atual < 12): criancas += 1
    elif(idade_atual < 18): adolescentes += 1
    elif(idade_atual <= 25): jovens_adultos += 1
    elif(idade_atual <= 35): adultos += 1
    elif(idade_atual < 60): meia_idade += 1
    else: idosos += 1

    idade_atual = int(input())

print("0-11 anos: {:.2f} %".format((criancas/total)*100))
print("12-17 anos: {:.2f} %".format((adolescentes/total)*100))
print(f"18-25 anos: {(jovens_adultos/total)*100:.2f} %")
print(f"26-35 anos: {(adultos/total)*100:.2f} %")
print(f"36-59 anos: {(meia_idade/total)*100:.2f} %")
print(f"Acima de 60 anos: {(idosos/total)*100:.2f} %")