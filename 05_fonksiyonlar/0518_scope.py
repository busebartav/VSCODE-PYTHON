# region scope_kapsam_giris
"""
1→ python main fonksiyon ile yani main kısmı ile fonksiyon arasında değişken aktarımları, 
2→ main deki değişkeni fonksiyon görebilecek mi değiştirebilecek mi? evet
3→ fonksiyondaki değişkene main kısmından erişim yapabilecek miyim? evet
4→ fonksiyondaki değişkenin içeriğini değiştirdiğimde, maindeki de değişecek mi? hayır
not→ değişkeni her ne kadar fonksiyonda tanımlasak da, fonksiyon scope’undan çıktığı anda değişken silinir
"""
# endregion

# region ornek_1
"""
def fonk():
    a = 34
    print(a)

fonk()
# print(a)  #hafızadan sildik 
"""
"""
def ciftSayiUret():
    global tekilListe
    while True:
        import random
        s = random.randint(1, 99)
        if s%2==1:
            continue
        else:
            if s in tekilListe:
                continue
            else:
                tekilListe.append(s)
                break
tekilListe=[]        
for i in range(1,30):
    ciftSayiUret()
print(tekilListe)
"""