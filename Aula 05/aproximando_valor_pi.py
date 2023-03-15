def aproxima(n):
    impar = 1
    threepot = 1
    const = 12**(1/2)
    soma = 0

    i = 0
    while(i < n):
        soma += ((-1)**i)/(impar*threepot)
        threepot *= 3
        impar += 2
        i += 1
    return const*soma

print(aproxima(185))