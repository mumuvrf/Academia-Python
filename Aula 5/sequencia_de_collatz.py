def collatz(n, contador):
    if(n%2 == 0): return collatz(n/2, contador+1)
    elif(n%2 != 0 and n != 1): return collatz(3*n + 1, contador+1)
    else: return contador

i = 1
maior_contagem = 0
num_maior_contagem = 0
contagem_atual = 0

while(i < 1000):
    contagem_atual = collatz(i, 1)

    if(contagem_atual > maior_contagem):
        maior_contagem = contagem_atual
        num_maior_contagem = i

    i += 1

print(num_maior_contagem)