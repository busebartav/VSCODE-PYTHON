"""
BREAK-CONTINUE
FOR
LAB
"""

"""
i=1
print("a")
while i<11:
    if i==5:
        print("b")
        break   
    print(f"{i}. döngü")
    i+=1
print("c")


i=1
print("a")
while i<100:
    if i%7==0:
        i+=1
        continue           #7 ve katlarını atlayacak
    elif i%15==0:
        break              #15in katına geldiğinde döngü duracak !!!
    print(f"{i}. döngüdeyim.")
    i+=1
print("b")


eb, say = 0, 0
while True:
    sayi =int(input("Lütfen sayı giriniz, çıkmak için -1 giriniz:"))
    if sayi == -1:
        break
    say+=1
    if sayi>eb:
        eb=sayi
        continue
if say:
    print(f"Girdiğiniz sayılardan en büyüğü {eb}'dir.")
else:
    print("Hiçbir sayı girmediniz :(")


while True:
    a = int(input("Lütfen sayı giriniz, çıkmak için -1:"))
    if a == -1:
        break
    if a%2!=1:
        print("Lütfen tek sayı giriniz !!!")
        continue
    tekSayilarToplami += a
print(f"Girdiğiniz tek sayıların toplamı {tekSayilarToplami}")


for i in range(10):
    print(i+1)



sayiDizisi = list(range(5, 15, 2))
print(sayiDizisi)


for i in range(1,11):
    if i!= 5:
        print(f"{i}. öğrenci")


for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        print(f"{i} x {j} =", i*j, end="\t")
    print()


obeb = 0
s1 = int(input("1.sayıyı giriniz:"))
s2 = int(input("2.sayıyı giriniz:"))
for i in range(1, min(s1,s2)+1):
    if s1%i==0:
        if s2%i==0:
            obeb = i
print(obeb)

sayac=0
sayi=int(input("Lütfen sayı giriniz:"))
for i in range(1, sayi + 1):
    if sayi%i==0:
        sayac+=1
if sayi%sayac==0:
    print(f"{sayi} TAUDUR.")
else:
        print("TAU DEĞİLDİR.")"""

