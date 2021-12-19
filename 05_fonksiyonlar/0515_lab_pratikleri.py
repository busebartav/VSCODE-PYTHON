# region ornek_1
"""
gunler = ["", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
aylar = ["",
         "ocak", "şubat", "mart",
         "nisan", "mayıs", "haziran",
         "temmuz", "ağustos", "eylül",
         "ekim", "kasım", "aralık"
         ]


def ayKontrol(a, g):    #4, 31
    if a>12:
        print("ocak...aralık arası 12 ay vardır")
        return False
    if gunler[a]<g:
        print(f"{aylar[a]} ayı {g} gün çekmez")
        return False
    else:
        return True



while True:
    gun = int(input("lütfen d. gününüzü giriniz : "))
    ay = int(input("lütfen d. ay giriniz : "))
    #print("bilgi amaçlı", gun, ay)  #casting → java, jscript, flutter, unity
    if not ayKontrol(a=ay, g=gun):   #4, 31
        continue
    yil = int(input("lütfen d. yil giriniz : "))
    break

print(gun,"/", ay,"/", yil)
"""
# endregion
"""
1→ sonuc() isimli fonk. olacak+
2→ sonuc() isimli fonk. içinde s1, s2 değerleri alınacak+
3→ koşula göre değer döndürecek+
4→ s1 s2'den büyük ise toplam geriye dönecek, küçük ise çıkarma,
eşit ise eşitlik geriye dönecek
"""

"""
def sonuc():
    s1, s2 = input("1. sayıyı giriniz:"), input("1. sayıyı giriniz:")
    if s1.isdigit() and s2.isdigit():
        s1, s2 = int(s1), int(s2)
        if s1 > s2:
            return s1+s2
        if s2 > s1:
            return s2-s1
        else:
            return s1, s2
    else:
        return "Lütfen sayısal değer girin"


print(sonuc())
"""
"""
1→ birlestir isimli fonk. olacak
2→ birlestir() isimli fonk. iki ifadeyi birleştirecek
3→ birleştirirken de İlk harfleri büyük şekilde birleştirecek
	Örn: 	ali kemal
		Ali Kemal
"""
"""
def birlestir(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return (a.capitalize(), b.capitalize())

print(birlestir("buse","berfin"))
"""
#region ornek
"""
1→ 10 adet çift sayı üretmek istiyoruz

2→ ciftSayiUret()
"""

"""
def ciftSayiUret():
    tekilListe=[]
    while True:
        import random
        s = random.randint(1, 99)
        if s%2==1:
            continue
        else:
            return s

for i in range(1,11):
    print(ciftSayiUret())
"""

"""def yaziTura():
    import random
    s = random.randint(1,2)
    if s==1:
        print("yazı")
    else:
        print("tura")

def skorBoard(o, p):
    print(f"Sonuc:")

oyuncuSkor, pcSkor = 0, 0

while True:
    yt = input("yazı için y, tura için t, çıkmak için ç...")
    if yt.lower() == "ç":
        break
    if yt.lower() == "y":
        if yaziTura()=="yazı":
            oyuncuSkor+=1
        else:
            pcSkor+=1
    for i in range(1,11):
        print(yaziTura())"""