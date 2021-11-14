#region ornek_1
"""havaYagisliMi = True
havaSogukMu = True
if havaYagisliMi:
    if havaSogukMu:
        print("Şemsiye alacağız, kalın giyineceğiz.")
    else:
        print("Şemsiye alacağız, tişört giyeneceğiz.")
else:
    if havaSogukMu:
        print("Şemsiyeye gerek yok, kalın giyineceğiz.")
    else:
        print("Şemsiyeye gerek yok, tişört giyinebiliriz.")"""
#endregion

x=int(input("Lütfen sayı giriniz\t:"))
if x>0:
    if x<100:
        print(f"{x} sayısı 100den küçük ve pozitiftir.")
    elif x==100:
        pass
    if x>100:
        print(f"{x} sayısı 100'den büyük ve pozitiftir.")


else:
    print("0 ya da negatif değer girmemelisiniz")