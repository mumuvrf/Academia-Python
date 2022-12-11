def concentracao_nociva(amostra):
    gases = {'O': 0}
    gases_nocivos = {}
    tam_atm = 0

    for linha_analise in amostra:
        for amostra_linha in linha_analise:
            for gas in amostra_linha:
                tam_atm += 1

                if gas not in gases:
                    gases[gas] = 0
                gases[gas]+=1
    
    for gas in gases.keys():
        gases[gas] = gases[gas]/tam_atm

        pouco_ox = gas == 'O' and gases[gas] < 0.2
        muito_n = gas == 'N' and gases[gas] > 0.7
        conc_alta = gas not in ['O', 'N'] and gases[gas] > 0.02
        
        if pouco_ox or muito_n or conc_alta:
            gases_nocivos[gas] = 100*gases[gas]
    
    return gases_nocivos

atmosfera = [
    [ ['P' , 'N' , 'He'],['Ar', 'P', 'He'],['Uuo', 'P', 'P' ] ],
    [ ['H' , 'C' , 'B' ],['P', 'Ar'],['F'  , 'S', 'P', 'He' ] ],
    [ ['Ar', 'Ga', 'Al'],['Ar', 'P', 'Ne'],['P', 'Se'] ]
]
print(concentracao_nociva(atmosfera))