dias = int(input("Quantos dias você quer analisar? "))
dias_chuva = 0
dias_frio = 0
dias_gc = 0
dias_csc = 0

i=0
while(i < dias):
    choveu = input("Choveu [S/N]? ")
    Tmin = float(input("Temperatura mínima (em Celsius)? "))
    guarda_chuva = input("Tinha guarda-chuva [S/N]? ")
    casaco = input("Tinha casaco [S/N]? ")

    if(choveu.upper() == "S"):
        dias_chuva += 1
        if(guarda_chuva.upper() == "S"): dias_gc += 1

    if(Tmin < 20):
        dias_frio += 1
        if(casaco.upper() == "S"): dias_csc += 1

    i += 1

print(f"Choveu em {dias_chuva} de {dias} dias")
print(f"Fez frio em {dias_frio} de {dias} dias")
print(f"Usou guarda-chuva em {dias_gc} de {dias_chuva} dias de chuva")
print(f"Usou casaco em {dias_csc} de {dias_frio} dias de frio")