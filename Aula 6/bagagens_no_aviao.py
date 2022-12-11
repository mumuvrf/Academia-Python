def filtra_bagagens(bagagens, a, l, p):
    limite = [a, l, p]
    excedente = 0
    for dimensoes in bagagens:
        for i in range(0, len(limite)):
            if dimensoes[i] > limite[i]:
                excedente += 1
                break
    return excedente
    
bagagens = [[43.2, 30.5, 20.1], [60.0, 20.0, 20.0], [10.0, 10.0, 10.0], [50.3, 30.2, 30.0], [54.0, 30.2, 22.1]]
a = 55
l = 35
p = 25
print(filtra_bagagens(bagagens, a, l, p))