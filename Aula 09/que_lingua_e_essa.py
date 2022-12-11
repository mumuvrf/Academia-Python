def separa_palavras(texto):
    pontuacoes = ['!', '?', ',', ';', '.', ':', ')', '}', ']', '(', '[', '{']
    palavras = []
    palavra_atual = ''
    for letra in texto:
        if letra == ' ' or letra == '\n':
            if palavra_atual != '':
                palavras.append(palavra_atual)
                palavra_atual = ''
        elif letra not in pontuacoes and letra != ' ':
            palavra_atual += letra
    if palavra_atual != '': palavras.append(palavra_atual.strip('\n'))
    return palavras

def predizer_lingua(linguas, texto):
    lingua_palavra = {}
    frac_linguas = {}
    for lingua in linguas.keys():
        frac_linguas[lingua] = 0
        for palavra in linguas[lingua]:
            lingua_palavra[palavra] = lingua

    palavras = separa_palavras(texto)
    qnt_palavras = len(palavras)
    maior_frac = 0
    for palavra in palavras:
        if palavra.lower() in lingua_palavra.keys():
            frac_linguas[lingua_palavra[palavra.lower()]] += 1/qnt_palavras
            maior_frac = max(frac_linguas[lingua_palavra[palavra.lower()]], maior_frac)

    paises_mf = []
    for lingua in frac_linguas:
        if frac_linguas[lingua] == maior_frac:
            paises_mf.append(lingua)

    if len(paises_mf) > 1 or len(paises_mf) == 0:
        frac_linguas['palpite'] = 'DESCONHECIDA'
    elif len(paises_mf) == 1: frac_linguas['palpite'] = paises_mf[0]
    return frac_linguas

linguas = {'ge': ['liebe', 'sprachschule', 'waschmaschine', 'zimmerservice', 'hund', 'haustürschlüssel', 'superwetter'], 'asm': [], 'en': ['bath', 'now', 'phone', 'sound', 'where', 'is', 'hello'], 'fr': ['revoir', 'belle', 'au', 'jour', 'fille']}
texto = '( } enchanté beau : [ au chien oui ) chien : ! ( rien rien belle : ) fille ] , connaître enchanté pardon . au beaucoup ? ! ! enchanté oui revoir ] rien revoir merci : au rien chien ) [ bonjour chat enchanté . beaucoup revoir ; ..'
print(predizer_lingua(linguas, texto))