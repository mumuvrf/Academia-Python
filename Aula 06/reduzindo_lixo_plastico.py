def contabilizar(volume, garrafas):
    enchido = 0
    for i in range(0, len(garrafas)):
        enchido+= garrafas[i][0]*garrafas[i][1]
    return enchido//volume

print(contabilizar(600,[[500,3],[650,2],[750,2]]))