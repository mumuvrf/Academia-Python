data_tsv = open('Aula 10/dados.tsv', 'w')

with open('Aula 10/dados.csv') as data_csv:
    lines = data_csv.readlines()
    for line in lines:
        words = line.split(',')
        for i in range(0, len(words)-1):
            data_tsv.write(words[i]+'\t')
        data_tsv.write(words[-1])

data_tsv.close()