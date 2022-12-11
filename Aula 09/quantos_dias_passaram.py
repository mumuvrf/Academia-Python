def dias_do_ano(data):
    meses = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    d, m, a = [int(x) for x in data.split('/')]
    dias_passados = d-1
    m -= 1
    while(m > 0):
        dias_passados += meses[m]
        m -= 1
    return dias_passados

print(dias_do_ano('15/03/2022'))