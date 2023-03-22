def bussola(xm, ym, xj, yj):
    if [xm, ym] == [xj, yj]:
        return "achou"
    else:
        dif_x = xm - xj
        dif_y = ym - yj

        if((abs(dif_x) < abs(dif_y) and dif_x != 0) or dif_y == 0):
            if dif_x < 0: return 'leste'
            else: return 'oeste'
        else:
            if dif_y < 0: return 'sul'
            else: return 'norte'

#print(bussola(1, 1, 1, 4))