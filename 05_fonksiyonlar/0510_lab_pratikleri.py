#region ornek_1 ***
"""
req:
1.parametre olarak girilen değerin mutlak değerini ekrana yazsın
2.kullanıcı sadece sayısal değer girsin
3.parametre gönderilmediğinde -1'in mutlak değerini alsın


def mutlakDeger(a=-1):
    if str(a).lstrip("-").isdigit():
        a=int(a)
        if a<0: 
            a*=-1
        print(a)
    else:
        print("ben ancak sayısal değerin mutlak işlemini yapabilirim")

a = input("lütfen m.d. alınacak sayı giriniz: ")
if a=="":
    mutlakDeger()
else:
    mutlakDeger(a)
"""

#endregion

#region ornek_2
"""
req:
1.parametreler girilecek, parametre adedi 3, fonk. adı kayitOl ++
2.tcKimlik, ad, email ++
3.mail argümanı gelmez ise ekrana @ yazılacak ++
4.ad argümanı gelmez ise ekrana noname yazılacak++
5.tcKimlik zorunlu++
"""
def kayitOl(tcKimlik, ad="noname", email="@"):
    print(f"Kimlik numarası ={tcKimlik}, İsim={ad}, email={email}")

kayitOl(1111)
kayitOl(23456789, "Buse")
kayitOl(99999, "Hasan", "hasan@gmail.com")
