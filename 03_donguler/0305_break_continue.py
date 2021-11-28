"""
i = 1
x = int(input("aradığınız stok id :"))
while i<10:
    print(i, end = " ")
    if i==x:
        break
    i+=1
    """


""" kullanıcı -1 basana kadar sayı giricek en büyük olanı ekrana bas"""

eb=0
while True:
    x=int(input("Lütfen bir sayı giriniz, çıkmak için -1'e basınız:"))
    if x==-1:
        break
    if x>eb:
        eb=x
if eb==0:
    print("Hiç Bir Sayı Girmediniz")
else:
    print(f"{eb}")
