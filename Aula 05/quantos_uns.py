def quantos_uns(n):
    num = str(n)
    qnt_uns = 0

    i = 0
    while(i < len(num)):
        if(num[i] == '1'): qnt_uns += 1
        i += 1

    return qnt_uns

#print(quantos_uns(1030110641))