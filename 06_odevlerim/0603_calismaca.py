"""
i=0
while i<5:
    i+=1
    print("Kargo 24 saatte kapıda !", sep = "-", end=" ")
    


i=0
while i<5:
    i+=1
    print("AOOOOOOOOOOOOOOOAAAAAAAAAAAAAA")
    



i=5
devamMi=True
while devamMi==True:
    print(i)
    if i==2:
        devamMi==False
        break
    i-=1


eb = -999999
sayi = int(input("Lütfen sayı giriniz, çıkmak için -1:"))
while sayi!=-1:
    if sayi>eb:
        eb = sayi
    sayi = int(input("Lütfen sayı giriniz, çıkmak için -1:"))
print(f"Girdiğiniz sayılardan en büyüğü {eb}")



tekSayilarinAdedi, ciftSayilarinAdedi = 0, 0
sayi = int(input("Lütfen sayı giriniz, çıkmak için 0:"))
while sayi!=0:
    if sayi%2==1:
        tekSayilarinAdedi+=1
    else:
        ciftSayilarinAdedi+=1
    sayi = int(input("Lütfen sayı giriniz, çıkmak için 0:"))
print(f"Girdiğiniz tek sayıların adedi {tekSayilarinAdedi}, çift sayıların adedi {ciftSayilarinAdedi}")"""

"""
i = 0
j = 0
carpimTablosu = i*j
while i<5:
    while j<5:
        j+=1
        print(f"{i} x {j} = {carpimTablosu}")
    i += 1
    j=0



i=0
j=0
while i<10:
    while j<10:
        print(" * ", end = " ")
        j+=1
    print()
    i+=1
    j=0

i, j = 0, 0
while i<10:
    while j<10:
        if i%2==0:
            print("*", end=" ")
        else:
            print("$", end=" ")
        j+=1
    i+=1
    j=0
    print()"""    



