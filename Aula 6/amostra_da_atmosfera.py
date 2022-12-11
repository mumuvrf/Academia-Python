def eh_respiravel(amostra):
    num_oxigenio = 0
    tam_atm = 0
    for fat_amostra in amostra:
        num_oxigenio += fat_amostra.count('O')
        tam_atm += len(fat_amostra)
    percentual_oxigenio = num_oxigenio/tam_atm
    return percentual_oxigenio >= 0.2

amostra = [
    ['O', 'N', 'N', 'Rn'],
    ['Ar', 'Ar', 'He', 'N'],
    ['O', 'Ar', 'N', 'N']
]
print(eh_respiravel(amostra))