def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    nome_junto = [ ]
    while(i < len(nome)):
        nome_junto.append(nome[i]+' '+sobrenome[i])
        i += 1

    return nome_junto

#names = ['jose', 'james', 'mary', 'margarida']
#surnames = ['martinez', 'stifler', 'bolton', 'smith']

#print(junta_nome_sobrenome(names, surnames))
