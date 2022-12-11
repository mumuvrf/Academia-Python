# Questão "Valida data"

def valida_data(dia, mes, ano):
    if(mes <= 0 or mes > 12): return False

    if(mes == 2):
        if(dia < 28): return True
        elif(dia == 29):
            if(ano%400 == 0): return True
            elif(ano%100 == 0): return False
            elif(ano%4 == 0): return True
            else: return False
        else: return False
    elif(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if(dia <= 31): return True
        else: return False
    else:
        if(dia <= 30): return True
        else: return False

#print(valida_data(29, 2, 1904))
