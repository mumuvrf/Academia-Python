# Questão "EP1 - Nota Final"

def nota_final(Q, AI, AF, EP1, EP2, PF):
    if(min(Q, AI, AF, EP1, EP2, PF) < 0 or max(Q, AI, AF, EP1, EP2, PF) > 10): return 0
    
    NI = 0.4*AI + 0.5*AF + 0.1*Q
    NG = 0.1*EP1 + 0.2*EP2 + 0.7*PF

    if(min(NI, NG) >= 5): NF = (NI + NG)/2
    else: NF = min(NI, NG)

    return NF

#print(nota_final(9.0, 8.0, 5.0, 7.5, 6.0, 8.2))