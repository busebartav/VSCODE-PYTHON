# region args_giris
"""
fonksiyondaki argüman sayısı ile çağırırken kullandığım argüman sayısı
aynı olmalı

def topla(a, b, c=0):
    print(f"{a} + {b} + {c} = {a+b+c}")

topla(2, 3)
"""
# endregion

# region args*

"""
def topla(*args):
    counter = 0
    sonuc = 0
    #print(type(args))
    for i in args:
        if i%2==1:
            counter += 1
            sonuc += i
    print(f"Tek sayıların ortalama değer → {sonuc/counter}")

topla(2, 3, 5, 8, 16, 2, 7, 9)"""

"""
def topla(*args):
    tekOlanlar= []
    #print(type(args))
    for i in args:
        if i%2==1:
            tekOlanlar.append(i)
    print(f"Ortalama değer → {sum(tekOlanlar)/len(tekOlanlar)}")

topla(2, 3, 5, 8, 16, 2, 7, 9)
"""

#endregion

