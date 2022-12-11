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

def nota_final(Q, AI, AF, EP1, EP2, PF):
    if(min(Q, AI, AF, EP1, EP2, PF) < 0 or max(Q, AI, AF, EP1, EP2, PF) > 10): return 0
    
    NI = 0.4*AI + 0.5*AF + 0.1*Q
    NG = 0.1*EP1 + 0.2*EP2 + 0.7*PF

    if(min(NI, NG) >= 5): NF = (NI + NG)/2
    else: NF = min(NI, NG)

    return NF


soma_notas = 0
num_alunos = 0
aprovados = 0
reprovados = 0
nova_entrada = input("Deseja adicionar as notas de mais um aluno? [sim/não] ")

while(nova_entrada.lower() != "não"):
    num_alunos += 1

    q1 = float(input("Nota do Quizz 1: "))
    q2 = float(input("Nota do Quizz 2: "))
    q3 = float(input("Nota do Quizz 3: "))
    q4 = float(input("Nota do Quizz 4: "))
    q5 = float(input("Nota do Quizz 5: "))
    AI = float(input("Nota da Avaliação Intermediária: "))
    AF = float(input("Nota da Avaliação Final: "))
    EP1 = float(input("Nota do EP1: "))
    EP2 = float(input("Nota do EP2: "))
    PF = float(input("Nota do Projeto Final: "))

    Q = nota_quizzes(q1, q2, q3, q4, q5)
    NF_aluno = nota_final(Q, AI, AF, EP1, EP2, PF)
    soma_notas += NF_aluno

    if(NF_aluno >= 5): aprovados += 1
    else: reprovados += 1

    print(f"Nota final do aluno: {NF_aluno:.2f}")
    nova_entrada = input("Deseja adicionar as notas de mais um aluno? [sim/não] ")

if(num_alunos == 0):
    num_alunos = 1 #apenas para não dividir por zero

media_sala = soma_notas/num_alunos
print(f"Média da sala: {media_sala:.2f}")
print(f"Aprovados: {(aprovados*100/num_alunos):.2f}%")
print(f"Reprovados: {(reprovados*100/num_alunos):.2f}%")