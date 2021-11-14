"""a=int(input("Lütfen birinci notu giriniz:"))
b=int(input("Lütfen ikinci notu giriniz:"))
c=int(input("Lütfen üçüncü notu giriniz:"))
ort=(a+b+c)/3
if ort>=50:
    print("Dersi geçtiniz.") 

    ###
x=int(input("Lütfen bir sayı giriniz:"))
if x<0:
    y =x * -1
print(f"{x} sayının mutlak değeri [{y}]")
"""


bakiyeBilgisi = int(input("Lütfen bakiye bilgisi giriniz:"))
hesabinBulunduguBanka = str(input("Hesabınızın bulunduğu bankayı giriniz:"))
paraGidecekBanka = str(input("EFT yapacağınız hesabın banka ismini giriniz:"))
gidecekPara = int(input("Lütfen transfer edilecek EFT tutarını giriniz:"))
if hesabinBulunduguBanka != paraGidecekBanka :
    hesaptanEksilenToplamTutar=gidecekPara*1.1
    kalanPara= bakiyeBilgisi-hesaptanEksilenToplamTutar
    print(f"Hesapta kalan miktar {kalanPara}")