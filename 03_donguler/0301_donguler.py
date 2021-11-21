"""
indirimOrani= 5
print(f"Ekstra %{indirimOrani} İndirim Orani")
print(f"Ekstra %{indirimOrani} İndirim Orani")
print(f"Ekstra %{indirimOrani} İndirim Orani")




indirimOrani=5
while True:
    print(f"Ekstra ½{indirimOrani} İndirim Orani")

i = 1
print("x")
while i<3:
    print("Ekstra %5 indirim orani")
    i+=1
    print("y")
print("z")


i=5
while i!=0:
    print(f"{i}")
    i-=1

yas = int(input("Lütfen yaş bilgisi giriniz ="))
if yas:
    print("Yaş bilgisi sıfır olamaz.")
else:
    print(yas)
    

eb = -999999999
sayi = int(input("lütfen sayı giriziniz, çıkmak için -1 yazınız : "))
while sayi != -1:
    sayi = int(input("lütfen sayı giriziniz, çıkmak için -1 yazınız : "))
    if sayi>eb:
        eb = sayi
print(eb)
"""


# region ornek_1
"""
i = 1
print("a")
while i<=3:
    print("b")
    i += 1
print("c")
"""
# endregion

# region ornek_2
"""
sayac = 1
while sayac<=5:
    print(sayac)
    sayac += 1
"""
# endregion

# region ornek_3
"""
sayac = 5
while sayac:       #yada sayac != 0:
    print(sayac)
    sayac -= 1
# def. da siz koşulu int bir tam sayıya bağlı olarak yazarsanız
# tam sayı 0 olduğunda döngü kırılır
"""


sayac = 5
devamMi = True
while devamMi: 
    print(sayac)
    if sayac==2:
        devamMi=False
    sayac -= 1


# endregion


