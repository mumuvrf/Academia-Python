def valida_exp(expressao):
    soma_esq = 0
    soma_dir = 0
    num_atual = 0
    igual = False
    multiplica = False
    for caracter in expressao:
        if caracter == 'I': num_atual += 1
        elif caracter in ['*', '+', '=']:
            if multiplica:
                if igual: soma_dir *= num_atual
                else: soma_esq *= num_atual
            else:
                if igual: soma_dir += num_atual
                else: soma_esq += num_atual
            num_atual = 0
            
            if caracter == '*': multiplica = True
            elif caracter == '+': multiplica = False
            elif caracter == '=':
                multiplica = False
                igual = True

    if not igual: return False
    else:
        if multiplica: soma_dir *= num_atual
        else: soma_dir += num_atual
        
    return soma_esq == soma_dir

print(valida_exp('I*I *I * II + I= III'))