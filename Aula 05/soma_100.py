import math

soma = 0
i = 0

while(i < 100):
    soma += math.pow(2, -i)
    i += 1

print(soma)