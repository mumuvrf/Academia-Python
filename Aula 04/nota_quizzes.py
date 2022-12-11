def compara_valores(x, y):
    if(x > y): return y
    else: return x

def nota_quizzes(q1, q2, q3, q4, q5):
    if(q1 < 0 or q1 > 10): return 0
    elif (q2 < 0 or q2 > 10): return 0
    elif (q3 < 0 or q3 > 10): return 0
    elif (q4 < 0 or q4 > 10): return 0
    elif (q5 < 0 or q5 > 10): return 0

    menor = compara_valores(q1, q2)
    menor = compara_valores(menor, q3)
    menor = compara_valores(menor, q4)
    menor = compara_valores(menor, q5)

    media = (q1+q2+q3+q4+q5-menor)/4
    return media

#print(nota_quizzes(4.5, 7.9, 5.8, 9.2, 10.3))