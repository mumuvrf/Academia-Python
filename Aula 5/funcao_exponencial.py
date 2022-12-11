def fatorial(valor):
    j = 1
    fat = valor
    while(j < valor):
        fat = fat*j
        j += 1
    return fat

def calcula_euler(x, n):
    exp = 1
    i = 1

    while(i < n):
        exp += pow(x, i)/fatorial(i)
        i+= 1

    return exp

#print(calcula_euler(5, 5))