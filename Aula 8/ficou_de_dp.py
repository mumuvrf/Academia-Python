def notas_dp(notas):
    dp = []
    for aluno in notas:
        media = (aluno['PF']+aluno['PI'])/2
        if(media < 5): dp.append(aluno['matricula'])

    return dp

notas = [
    {'matricula' : 123, 'PI' : 7, 'PF': 3},

    {'matricula' : 456, 'PI': 4, 'PF': 8},

    {'matricula' : 789, 'PI': 5, 'PF': 1}
]

print(notas_dp(notas))