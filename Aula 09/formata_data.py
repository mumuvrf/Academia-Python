def formata_data(data, formato):
    data_texto = {}
    num_atual = ''

    i=0
    while(data[i] != formato[1]):
        num_atual += data[i]
        i+=1
    data_texto[formato[0]] = num_atual
    num_atual = ''

    i+=1
    while(data[i] != formato[3]):
        num_atual += data[i]
        i+=1
    data_texto[formato[2]] = num_atual
    num_atual = ''

    i+=1
    while(i < len(data)):
        num_atual += data[i]
        i+=1
    data_texto[formato[4]] = num_atual

    data_texto['d'] = int(data_texto['d'])
    data_texto['d'] = f"{data_texto['d']:0>2}"
    data_texto['m'] = int(data_texto['m'])
    data_texto['m'] = f"{data_texto['m']:0>2}"

    if len(data_texto['a']) < 3:
        data_texto['a'] = int(data_texto['a'])
        data_texto['a'] += 2000

    return f"{data_texto['a']}-{data_texto['m']}-{data_texto['d']}"

print(formata_data('11/1/21','m/d/a'))