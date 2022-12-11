def calcula_fibonacci(n):
    fibonacci = [1]
    if(n > 1): fibonacci.append(1)

    i = 2
    while(i < n):
        fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
        i+= 1
    
    return fibonacci

#print(calcula_fibonacci(10))