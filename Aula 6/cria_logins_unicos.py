def login_disponivel(login, lista_logins):
    if login in lista_logins:
        i = 1
        while(True):
            if login+str(i) not in lista_logins:
                return login+str(i)
            i+=1
    else: return login

lista_logins = []
while(True):
    login = input()
    if(login == 'fim'): break

    lista_logins.append(login_disponivel(login, lista_logins))
    print(lista_logins[-1])