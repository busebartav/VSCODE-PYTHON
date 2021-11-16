"""
    - Klavyeden iki tane fiyat verisi alınır.
    - Eğer bu fiyat verileri düzgünse;
        - Eğer ödenecek tutar 200TL den fazlaysa, ikinci ürüne
            %25 indirim yapılacaktır.
        - Değilse bişey yapılmayacak.
    - 150,300 -> Ürünlerin fiyatı .. TL ve .. TL'dir. İkinci ürüne
     .. TL indirim yapılmıştır. Borcunuz : ..TL'dir.
"""


print("Alınan veriler sıfırdan büyük olmalıdır.")
x, y = int(input("İlk fiyat\t=")), int(input("İkinci fiyat\t="))
odenecekTutar=x+y
if odenecekTutar>200:
    avantajliTutar=x+y*0.75
    x, y = y, x
    print(f"Ödeyeceğiniz tutar={avantajliTutar}")
else:
    print(f"Ödeyeceğiniz tutar = {odenecekTutar}")
