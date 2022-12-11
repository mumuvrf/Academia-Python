def maximo_divisor_comum(a, b):
    if(b == 0): return a
    elif(a == 0): return b

    if(a >= b): return maximo_divisor_comum(b, a-b)
    elif(b > a): return maximo_divisor_comum(a, b-a)

#print(maximo_divisor_comum(40, 45))