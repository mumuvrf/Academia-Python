def filtra_positivos(numeros):
    positivos = []

    for valor in numeros:
        if(valor > 0): positivos.append(valor)

    return positivos