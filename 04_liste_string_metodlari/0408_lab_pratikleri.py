# region siralama
# orjinal liste     9, 7, 5, 1, 3, 4, 2, 6, 8
# 1. Sıralamada     7, 5, 1, 3, 4, 2, 6, 8, 9
# 2. Sıralamada     5, 1, 3, 4, 2, 6, 7, 8, 9
# 3. Sıralamada     1, 3, 4, 2, 5, 6, 7, 8, 9
# ...
"""
liste =  [9, 7, 5, 1, 3, 4, 2, 6, 8]
while True:
    siraliMi = True
    for i in range(len(liste)-1):
        if liste[i]>liste[i+1]:
            liste[i], liste[i+1] = liste[i+1], liste[i]
            siraliMi = False
    if siraliMi:
        break
print(liste)
"""