def questao_para_texto(questao, numero):
    cabecalho = f'----------------------------------------\nQUESTAO {numero}\n\n{questao["titulo"]}\n\nRESPOSTAS:\n'

    opcoes = ''
    for letra in questao['opcoes'].keys():
        opcoes += f'{letra}: {questao["opcoes"][letra]}\n'
    questao_formatada = cabecalho+opcoes
    
    return questao_formatada

questao = {
    "titulo": "Qual destes parques não se localiza em São Paulo?!",
    "nivel": "facil",
    "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
    },
    "correta": "D"
}
numero = 5
print(questao_para_texto(questao, numero))