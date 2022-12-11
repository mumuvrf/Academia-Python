def PiWallis(n):
    pi = 4
    numerador = 2
    denominador = 1
    i = 1
    while(i < n):
        if(i%2 == 0): numerador+=2
        else: denominador+=2
        pi = pi*(numerador/denominador)
        i+=1

    return pi

# print(PiWallis(300))