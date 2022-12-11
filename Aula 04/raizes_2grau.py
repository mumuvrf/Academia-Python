def quantia_de_raizes(a, b, c):
    delta = b - 4*a*c
    if(delta > 0): return 2
    elif(delta == 0): return 1
    else: return 0

#print(quantia_de_raizes(1, 4, 1))