dias = int(input('Quantos dias? '))
horas = int(input('Quantas horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos? '))

tempo = ((dias*24 + horas)*60 + minutos)*60 + segundos

print(tempo)