import math

i = 0
maior_dif = 0
maior_index = 0

while(i <= 90):
    aprox_sin = (4*i*(180-i))/(40500 - i*(180-i))
    dif_sin = abs(aprox_sin - math.sin(math.radians(i)))

    if(dif_sin > maior_dif):
        maior_dif = dif_sin
        maior_index = i

    i+=1

print(maior_index)