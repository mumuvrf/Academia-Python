def calcula_segredo(numero):
    a = numero%10
    b = (numero%100)//10
    c = numero//100

    if(numero < 100 or numero > 999): return -1
    else: return a+b+c

#print(calcula_segredo(82))