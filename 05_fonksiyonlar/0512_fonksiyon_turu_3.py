# region fonksiyon_turu_3_parametre_almayan_deger_donduren
"""
Fonksiyon tanımlama anında argüman almaz, değer döndürür
a = round(123.666, 3)
print(a)
print(round(333.9859684, 2))
"""
# endregion

#region ornek_1
"""
def topla():
    s1, s2= int(input("Lütfen 1.değer giriniz:")), int(input("Lütfen 2.değer giriniz:"))
    return f"{s1} + {s2} = {s1+s2}"

sonuc = topla()
print(sonuc)
"""
#endregion

#region ornek_2
"""
def ciftMi():
    s = int(input("Lütfen bir sayı giriniz:"))
    if s%2==0:
        return True
    else:
        return False

if ciftMi():
    print("sayı çifttir")
else:
    print("sayı tektir")
"""
#endregion

