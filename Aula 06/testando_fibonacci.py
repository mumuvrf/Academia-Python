def eh_fibonacci(numeros):
    if(len(numeros) < 3): return False
    else:
        i = 2
        while(i < len(numeros)):
            if(numeros[i] != (numeros[i-1]+numeros[i-2])): return False
            i+=1
        return True