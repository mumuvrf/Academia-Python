def seleciona_candidatos(candidatos, criterios):
    aptos = []
    for candidato in candidatos:
        for i in range(0, len(criterios)):
            if len(candidato[2]) != len(criterios): break
            if candidato[2][i] < criterios[i]: break
        else:
            aptos.append([candidato[0], candidato[1]])
    return aptos

candidatos = [
    ['Julia WA.', '6780-9', [10.0, 9.5, 7.5]],
    ['Bruna QS.', '3423-1', [10.0, 9.2, 7.4, 9.5]],
    ['Camila A.', '7621-5', [9.00, 8.0, 8.3]],
    ['Vizeu BA.', '4040-4', [9.00, 9.1]],
    ['Hamil KS.', '2362-0', [9.00, 8.1, 8.0]],
    ['Igor VGS.', '7877-1', [4.90, 8.1, 8.0]],
]
criterios = [5.0, 8.0, 7.0]
print(seleciona_candidatos(candidatos, criterios))