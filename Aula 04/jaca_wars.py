import math

velocidade = float(input("Com que velocidade você lançará sua jaca? "))
angulo = float((input("Qual o ângulo do lançamento? ")))

g = 9.8

distancia = (math.pow(velocidade, 2)*math.sin(2*math.radians(angulo)))/g

#print(distancia)

if(distancia < 98): print('Muito perto')
elif(distancia > 102): print('Muito longe')
else: print('Acertou!')