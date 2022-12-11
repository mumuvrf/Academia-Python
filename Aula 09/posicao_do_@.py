def pos_arroba(email):
    for i, letra in enumerate(email):
        if letra == '@':
            return i
    return None

print(pos_arroba('viniciusrf2@al.insper.edu.br'))