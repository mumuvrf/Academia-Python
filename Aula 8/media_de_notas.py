def calcula_media(lista_alunos):
    soma = 0
    n_alunos = 0
    for turma in lista_alunos:
        for nota in turma.values():
            soma += nota
            n_alunos+=1

    return soma/n_alunos

# lista_alunos = [{"aluno1": 5, "aluno2": 8}, {"aluno3": 5}]
# print(calcula_media(lista_alunos))