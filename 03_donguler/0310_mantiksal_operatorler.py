"""
1→ ve       and
2→ veya     or
3→ değil    not
"""

#print(5==5 and 3>6)
#print(5!=5 or 3>6)
"""
u="guest"
print(u!="admin")
"""

# ay bilgisi alalım
# 36-68 ay arası ise anaokuluna gitsin
# değil ise gidemez :(
"""
x = int(input("Lütfen çocuğunuzun kaç aylık olduğunu giriniz ="))
if x>=36 and x<=68:
    print("Çocuğunuz anaokuluna gidebilir :)")
else:
    print("Çocuğunuz anaokulu için fazla büyük ya da fazla küçük :(")
    """


"""
kilo=int(input("Kilonuz\t="))
boy=float(input("Boyunuz\t="))
vki=kilo/boy**2

if vki<18.49:
    print("İdeal kilonun altında")
elif vki>18.5 and vki<29.99:
    print("İdeal kilo")
elif vki>30:
    print("İdeal kilonun altında")
"""

for i in range(2,19+1):
    for j in range(2, i):
        if i % j == 0:
            print(f"{i} sayısı asal değildir.")
            break
    else:
         print(f"{i} sayısı asaldır.")

