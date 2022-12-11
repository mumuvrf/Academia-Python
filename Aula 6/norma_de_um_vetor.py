from math import *

def calcula_norma(vetor):
    norma2 = 0
    for dimensao in vetor:
        norma2 += dimensao**2
    return sqrt(norma2)