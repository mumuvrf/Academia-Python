import math

def calcula_extensao(coord_x, coord_y):
    extensao = 0
    i = 1

    while(i < len(coord_x)):
        extensao += math.sqrt(math.pow((coord_x[i]-coord_x[i-1]), 2)+math.pow((coord_y[i]-coord_y[i-1]), 2))
        i += 1

    return extensao

# x = [275, 290, 310, 390, 480]
# y = [75, 180, 120, 110, 150]

# print(calcula_extensao(x, y))