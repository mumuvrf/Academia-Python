def produz_um_dois_insper(inicial, final, multiplo):
    umdoisinsper = []
    i = inicial
    while(i <= final):
        if(i%multiplo == 0): umdoisinsper.append('Insper')
        else: umdoisinsper.append(i)
        i+=1
    return umdoisinsper

print(produz_um_dois_insper(2, 13, 3))