def pet_pode_viajar(pet_info, lim_comp, pas_vend):
    if(pet_info[5] == 'N'): return False
    #Problema do atestado resolvido
    
    peso_pet = pet_info[2]
    peso_caixinha = pet_info[3]
    lim_peso = lim_comp[1]
    if(lim_peso < peso_pet+peso_caixinha): return False
    #Problema do peso resolvido

    dim_caixinha = pet_info[4] 
    lim_dimensoes = lim_comp[2]
    i = 0
    while(i < len(dim_caixinha)):
        if(dim_caixinha[i] > lim_dimensoes[i]): return False
        i+=1
    #Problema do tamanho resolvido

    lim_qnt = lim_comp[0]
    qnt = 0
    for passagem in pas_vend:
        if('pet_cabine' in passagem[1]): qnt+=1
    if(qnt >= lim_qnt): return False
    #Problema da quantidade resolvido
    
    return True

# pet_info = ['Totó', 'cachorro', 5.5, 1.0, [20.0, 30.0, 40.0], 'S']

# lim_comp = [3, 7.0, [20.0, 35.0, 45.0]]

# pas_vend = [
#     ['1A', []],
#     ['5C', ['alergia', 'pet_cabine']],
#     ['6D', []],
#     ['7A', []],
#     ['7A', ['cadeira_rodas']],
#     ['9B', ['pet_cabine']]
# ]

# print(pet_pode_viajar(pet_info, lim_comp, pas_vend))