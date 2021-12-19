# region list_arguments_giris
"""
Argüman olarak → int, float, string, gönderebiliyorum, peki
Argüman olarak → list gönderebilir miyim? Cevabı, Evet
"""
# endregion

# region ornek
"""
def ortalama(liste):
    print(type(liste))
    tekAdet = 0
    for i in liste:
        if i%2==1:
            tekAdet+=1
    print(f"listede {tekAdet} tane tek sayı vardır.")
    print(f"tüm listenin elemanları toplamı → {sum(liste)}")

#invoke
ortalama([3, 5, 9, 15, 16])
"""
# endregion

#region ornek_2

"""import time
from datetime import datetime
cTime = time.time()
print(cTime) #1639902382.6234386
# epoch time
# 1/1/1970 → unix → linux → macOS → windows
print(datetime.now())
print(datetime.now().timestamp())
print(datetime.fromisoformat("2000-12-30").timestamp())"""
"""
import time
from datetime import datetime
def urunTarihKontrol(liste):
    for i in liste:
        cTime=time.time()
        pTime=datetime.fromisoformat(i).timestamp()
        if round((cTime-pTime)/86400)>60:
            print(i)


tarihListesi = [
    "2021-10-18",
    "2021-10-19",
    "2021-10-20",
    "2021-10-21",
]

urunTarihKontrol(tarihListesi)
"""