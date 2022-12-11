def mais_populoso(estados):
    emp = ['cidade', 0]

    for estado in estados.keys():
        pop_estado = 0
        for cidade in estados[estado].keys():
            pop_estado += estados[estado][cidade]
        if(pop_estado > emp[1]):
            emp[0] = estado
            emp[1] = pop_estado

    return emp[0]