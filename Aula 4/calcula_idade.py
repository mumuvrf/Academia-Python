#Não há necessidade de usar condicional!

def calcula_idade(dn, mn, an, dd, md, ad):
    dias_de_vida = dd + md*30 + ad*365 - dn - mn*30 - an*365
    idade = dias_de_vida//365
    return idade

#print(calcula_idade(15,7,2000,20,9,2021))