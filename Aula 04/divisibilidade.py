# Questão "Divisibilidade"

def divisivel(numero):
    def checa_divisibilidade(variavel, divisor):
        return variavel%divisor == 0

    frase = ''

    if checa_divisibilidade(numero, 2):
        frase += 'Ins'

    if checa_divisibilidade(numero, 3):
        frase += 'per'

    if frase != '': return frase
    elif frase == '': return numero