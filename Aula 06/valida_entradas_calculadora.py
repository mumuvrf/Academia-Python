def valida_entradas(entradas):
    sinais = ['+', '-', '*', '/', '**', '//', '%']

    if len(entradas) < 2 or entradas[-1] != '=':
        return False

    i = 1
    while i < len(entradas)-1:
        k = 0
        eh_sinal = False
        while k < len(sinais):
            if entradas[i] == sinais[k]:
                eh_sinal = True
            k+=1
        if not eh_sinal:
            return False
        i+=2
    return True