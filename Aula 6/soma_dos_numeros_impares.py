def soma_impares(numeros):
    soma = 0

    i = 0
    while(i < len(numeros)):
        if(numeros[i]%2 != 0): soma+=numeros[i]
        i+=1

    return soma