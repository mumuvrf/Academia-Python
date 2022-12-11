def eh_valida(expressao):
    pares_chaves = {
        "{":"}", "(":")", "[":"]"
    }
    abrem = ['{', '[', '(']
    fecham = ['}', ']', ')']
    esperado = []

    for caractere in expressao:
        if caractere in abrem:
            esperado.append(pares_chaves[caractere])
        elif caractere in fecham:
            if len(esperado) == 0:
                return False
            elif esperado[-1] != caractere:
                return False
            else:
                esperado.pop()
    if len(esperado) > 0: return False

    return True

print(eh_valida("4 + 2("))