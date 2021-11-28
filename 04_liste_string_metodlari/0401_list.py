
"""
devamsizlikOraniYuksekGunler = [ "cuma", "pazartesi", "çarşamba" ]
print(devamsizlikOraniYuksekGunler)
"""

"""
sayilar = [3, 55, 63, 99, 1, 12, 74]
#sayilar[3], sayilar[1]=sayilar[1], sayilar[3]
#del sayilar[3]

print(sayilar)
"""

"""
sayilar = [3, 55, 63, 99, 1, 12, 74]
for i in range(len(sayilar)):
    if sayilar[i]>=50:
        print(f"{i+1}. öğrencinin notu: ", sayilar[i])
"""

"""
x=0
sayilar = [11, 5, 36, 78, 99, 2]
# aranan eleman : 99
# aradığınız 99 elemanı listestenin 4. indisli elemanıdır
s = int(input("Lütfen aradığınız elemanı giriniz="))
for i in sayilar:
    if s==i:
        print(f"Aradığınız {s} elemanı listenin {x+1}. elemanıdır")
        break
    x+=1
else:
    print("Bulamadım :(")
"""

""" 
isminizi giriniz : BUSE
B
U
S
E
"""

isim=str(input("İsminizi giriniz :"))
"""print(isim[0])
print(isim[1])
print(isim[2])
print(isim[3])"""

for i in range(len(isim)):
    print(isim[i])