def soma_multiplos(a, b):
    i = 0
    soma = 0

    while(i <= max(a, b)*10):
        if(i%a == 0): soma += i
        elif(i%b == 0): soma += i
        i += 1

    return soma

#print(soma_multiplos(7, 4))