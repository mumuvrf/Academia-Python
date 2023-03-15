def soma(x, y): return x+y
def produto(x,y): return x*y
def subtracao(x,y): return x-y
def divisao(x,y): return x/y

num = int(input())
operador = input()

while(operador not in set(['+', '-', '*', '/', '='])):
    print("Deveria ser um dos seguintes operadores: + - / * ou o =")
    operador = input()

while operador != '=':
    novo_num = int(input())
    
    if(operador == '+'):
        num = soma(num, novo_num)
    elif(operador == '-'):
        num = subtracao(num, novo_num)
    elif(operador == '*'):
        num = produto(num, novo_num)
    elif(operador == '/'):
        num = divisao(num, novo_num)

    operador = input()
    while(operador not in set(['+', '-', '*', '/', '='])):
        print("Deveria ser um dos seguintes operadores: + - / * ou o =")
        operador = input()

print(num)