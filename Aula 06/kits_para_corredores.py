def organiza_filas(pessoas):
    filas = [
        [],
        [],
        [],
        []
    ]
    for pessoa in pessoas:
        if(pessoa[1] <= 20):
            filas[0].append(pessoa[0])
        elif(pessoa[1] <= 40):
            filas[1].append(pessoa[0])
        elif(pessoa[1] <= 60):
            filas[2].append(pessoa[0])
        else:
            filas[3].append(pessoa[0])
    return filas

pessoas = [
	['João',20],['Maria',18],['Mario',35],['Dario',43],
	['Joana',60],['Lucas',27],['Alice',56],['Sofia',32],
	['Bruno',19],['Melissa',61],['Frida',27],['Felipe',30]
]
print(organiza_filas(pessoas))