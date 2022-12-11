def valida_cpf(d1, d2, d3, d4, d5, d6, d7, d8, d9, v1, v2):
    if(max(d1, d2, d3, d4, d5, d6, d7, d8, d9, v1, v2) == min(d1, d2, d3, d4, d5, d6, d7, d8, d9, v1, v2)): return False

    v1_real = (((d1*10+d2*9+d3*8+d4*7+d5*6+d6*5+d7*4+d8*3+d9*2)*10)%11)%10
    v2_real = (((d1*11+d2*10+d3*9+d4*8+d5*7+d6*6+d7*5+d8*4+d9*3+v1*2)*10)%11)%10

    if(v1_real == v1 and v2_real == v2): return True
    else: return False

#print(valida_cpf(5, 2, 9, 9, 8, 2, 2, 4, 7, 2, 5))