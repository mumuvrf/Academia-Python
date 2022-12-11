# Questão "Reflexão interna total"

import math

def reflexao_total_interna(n1, n2, angulo):
    seno = n2*math.sin(math.radians(angulo))/n1

    if(seno > 1): return True
    else: return False