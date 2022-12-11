cigarros_por_dia = int(input('Quantos cigarros fuma por dia? '))
anos_fumante = int(input('Há quanto tempo você fuma? '))

dias_perdidos = ((cigarros_por_dia*(365*anos_fumante))*10)/(60*24)

print(dias_perdidos)