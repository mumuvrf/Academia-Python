import math

dens_agua = 0.997

def will_it_float(P, R, r):
    volume = 2*math.pow(math.pi, 2)*R*math.pow(r, 2)

    if(P*1000/volume <= 0.997): return True
    else: return False