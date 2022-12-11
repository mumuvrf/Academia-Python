def decimal_para_binario(n):
    if(n < 0): return "Negativo"

    binario_aux = ''

    while(n > 0):
        resto = n%2
        if(resto == 0): binario_aux += '0'
        else: binario_aux += '1'
        n = n//2

        if(n == 1):
            binario_aux += '1'
            n = 0

    binario = ''
    tamanho = len(binario_aux)

    i = 1
    while(i <= tamanho):
        binario += binario_aux[tamanho-i]
        i += 1
    
    return binario

#print(decimal_para_binario(100))