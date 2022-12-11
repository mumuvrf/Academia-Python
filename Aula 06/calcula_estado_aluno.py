def calcula_estado(registro):
    status = []
    for aluno in registro:
        nota_quizzes = (sum(aluno[1]) - min(aluno[1]))/4
        nota_final = 0.1*nota_quizzes+0.4*aluno[2][0]+0.5*aluno[2][1]
        if nota_final >= 5:
            status.append([aluno[0], 'A'])
        else:
            status.append([aluno[0], 'R'])
    return status

registro = [
    ['Maria', [5.0, 10.0, 0.0, 10.0, 10.0], [6.7, 8.0]],
    ['Joao', [0.0, 10.0, 10.0, 10.0, 0.0], [6.7, 2.0]],
    ['Joana', [10.0, 0.0, 10.0, 0.0, 10.0], [6.7, 8.0]]
]
print(calcula_estado(registro))