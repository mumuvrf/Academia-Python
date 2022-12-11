def fatorial(n):
    produto = 1
    while(n > 0):
        produto = produto*n
        n-=1

    return produto

#print(fatorial(3))