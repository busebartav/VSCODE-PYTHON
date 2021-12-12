#region ornek_1
"""
Listeye 
sonsuz döngü içinde öğrenci ekleyeceğiz

ogrenciListesi = []
while True:
    ogrenci = input("listeye eklenecek öğrenci, çıkmak için ç:")
    if ogrenci == "ç":
        break
    ogrenciListesi.append(ogrenci)
for i in ogrenciListesi:
    print(i)
    """
#endregion

#region ornek_2
"""
Benzer örneği bu kez
Ekle-Sil-Listele menüsü ile genişletelim

ogrenciListesi = []
print("""
        #[1]     Ekle
        #[2]     Sil
        #[3]     Listele
        #[4]     Çık 
""")
while True:
    secim = int(input("tercihinizi giriniz:"))
    if secim == 1:
        ogrenci = input("listeye eklenecek öğrenci:")
        ogrenciListesi.append(ogrenci)
        continue
    elif secim == 2:
        ogrenci = input("listeden çıkarılacak öğrenci:")
        ogrenciListesi.remove(ogrenci)
        continue
    elif secim == 3:
        for i in ogrenciListesi:
            print(i)
    elif secim == 4:
        break
    else:
        print("hatalı seçim")
"""
#endregion

# region ornek_3
"""
İki basamaklı sayıyı → metne dönüştüren uygulama yapalım
Örn; 95
doksan beş
birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
sayi = 95
print(f"{onlar[sayi//10]} {birler[sayi%10]}")
"""
# endregion

