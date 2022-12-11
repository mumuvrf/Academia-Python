def raiz_quadrada(n):
    if(n == 0): return 0

    impar_atual = 1
    valor_raiz = 0

    while(impar_atual <= n):
        n -= impar_atual
        valor_raiz += 1
        impar_atual += 2

    return valor_raiz

#print(raiz_quadrada(169))