#region ornek_1 1. Öğrenci,  2. Öğrenci, 3. Öğrenci  ... 10. Öğrenci
"""
for i in range (1, 11):
    print(f"{i}. Öğrenci", end =", ")

    """
#endregion

#region ornek_2 ÇARPIM TABLOSU
"""
for i in range(1,6):
    for j in range(1,6):
        print(f"{i} x {j}", "\t=", i*j, end = "\t ")
    print()
"""
#endregion

#region ornek_3 #-1 girene kadar sayı iste listedeki tek sayıların toplamı
"""
tekToplam = 0
while True:
    x = int(input("Lütfen sayı giriniz, çıkmak için -1 basınız:"))
    if x!=-1:
        if x%2!=0:
            tekToplam+=x
        else:
            print("Lütfen tek sayı giriniz.")
            continue

    else:
        break
print(tekToplam)
"""
#endregion

#region ornek_4 
"""
lütfen sayı giriniz sayı giriniz: 30
1 2 3 5 6 10 15 30


x = int(input("Lütfen sayı giriniz \t:"))
for i in range(1, x+1):
    if x%i==0:
        print(f"{i}", end = " ")
        
"""