def esta_na_lista(pais, lista):
    i = 0
    while(i < len(lista)):
        if(pais in lista[i]): return True
        i += 1
    
    return False

#print(esta_na_lista("brasil", [["libia", 3678], ['egito', 5008], ['india', 9919], ['japao', 13836]]))