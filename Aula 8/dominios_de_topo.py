def usuarios_por_pais(emails, dominios):
    paises = {}
    for endereco in emails:
        sufixo_pais = endereco[-2]+endereco[-1]
        username = ''

        i=0
        while(endereco[i] != '@'):
            username+=endereco[i]
            i+=1
        
        if dominios[sufixo_pais] not in paises:
            paises[dominios[sufixo_pais]] = [username]
        else:
            paises[dominios[sufixo_pais]].append(username)

    return paises

emails = ['.@edu.br', 'usuario2@uma.pt', 'usuario3@kth.se', 'usuario4@usp.br']
dominios = {
    'pt': 'Portugal',
    'br': 'Brasil',
    'se': 'Suécia'
}
print(usuarios_por_pais(emails, dominios))