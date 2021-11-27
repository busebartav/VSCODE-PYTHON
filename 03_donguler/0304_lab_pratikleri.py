# region ornek_1
"""
a=input("Metni giriniz=")
i=int(input("Kaç kere tekrar etmesini istediğinizi giriniz="))
x=0
while x < i:
    print(a)
    x+=1 
"""


# region ornek_2 * * * * * * * * * *
"""
i=1
while i<=10:
    i+=1
    print("*", end=" ")
 """

# region ornek_3 * $ * $ * $ * $ * $
"""
i=0
while i<10:
    i+=1
    if i%2==0:
        print("$", end=" ")
    else:
        print("*", end=" ")

"""

# region ornek_4

i = 0
j = 0
while i<10:
    while j<10:
        print("hayat çuk zor", end=" ")
        j+=1
    i+=1
    j=0
    print()

    

# region ornek_5
""" rom _typeshed import SupportsItemAccess
import time as t
i = 1
while i<11:
    print(f"\r{i}", end=" ")
    i+=1
    t.sleep(1)
"""


# region ornek_6
"""
Açıl … Açıl. Lütfen Tamamlayınız :  kalem
heheheheh ne oldu çıkamadın mı
Tamamlayınız : defter
çıkamadın mı
Tamamlayınız : susam
başardın!!!


print("Açıl ...... Açıl.")
secret=input("Lütfen Tamamlayınız = ")
while secret != "susam":
    print("heheheheh ne oldu çıkamadın mı")
    secret=input("Lütfen Tamamlayınız = ")
print("Başardın!!!")

"""

# region ornek_7
"""
Sayı Giriniz : 5
5 x 1 = 5
5 x 2 = 10
5 X 3 = 15
5 X 4 = 40
5 X 5 = 25


x=int(input("Sayı giriniz = "))
i=0
while i<5:
    i+=1
    print(f"{x} x {i} = {i*x}")
"""


# region ornek_8
""" 1'den 99'a kadar olan tek sayılar

i=1
while i<100:
    if i%2==1:
        print(f"{i}", end=" ")
    i+=1
"""

"""
i=1
x=1
while i<100:
    if i%2==1:
        print(f"{i}", end =" ")
        x+=1
    if x>10:
        print()   
        print(end="\n")
    i+=1
"""

# region ornek_9
"""
*
* *
* * *
* * * *
* * * * *
"""
# 5x5 tablo
"""
i=0
j=0
while i<5:
    while j<5:
        j+=1
        print("*", end=" ")
    i+=1
    j=0 #İçerideki döngüye tekrar girmesini sağladık.
    print()
"""
# 1-2-3-4-5 diye giden
"""
i=0
j=0
while i<5:
    while j<=i:
        j+=1
        print(" * ", end=" ")
    i+=1
    j=0
    print()

"""

# region ornek_10
""" 
* * * * * 
* * * * 
* * * 
* * 
*

i = 0
j = 5
while i < 5:
    while j > 0:
        j -= 1
        print(" * ", end=" ")
    i += 1
    j = 5-i
    print()
***
i=0
j=5
while i<5:
    while j>i:
        j-=1
        print(" * ", end=" ")
    i+=1
    j=5
    print()
"""



#region ornek_11
"""
* * * * *
  * * * *
    * * *
      * *
        *


i = 0
j = 0
b = 0
while i < 5:
    while j < 5:
        if b < i:
            print("   ", end=" ")

        else:
            print(" * ", end=" ")
        j += 1
        b += 1
    i += 1
    j=0
    b = 0
    print()

"""

#region ornek_12
"""
i = 0
j = 0
while i < 10:
    while j < 10:
        if i%2==1:
            if j%2==0:
                print(" # ", end=" ")
            else:
                print(" $ ", end=" ")
        else:
            if j%2==0:
                print(" $ ", end=" ")
            else:
                print(" # ", end=" ")
        j += 1 
    i += 1
    j = 0
    print ()
"""