#region ornek_1
"""
x , y = int(input("Birinci sınav notunu giriniz:")), int(input("İkinci sınav notunu giriniz:"))
ort=(x+y)/2
if ort>=85:
    print(f"Ortalamanız {ort} ise Pekiyi")
elif ort>=70:
    print(f"Ortalamanız {ort} ise İyi")
elif ort>=55:
    print(f"Ortalamanız {ort} ise Orta")
elif ort>=45:
    print(f"Ortalamanız {ort} ise Geçer")
else:
    print("Kaldınız.")
    """
#endregion

#region ornek_2
"""
x, y = int(input("İlk sayıyı giriniz:")), int(input("İkinci sayıyı giriniz:"))
if x>y:
    print(f"{x} sayısı, {y} sayısından büyüktür.")
elif x==y:
    print(f"{x} ve {y} eşit sayılardır.")
else:
    print(f"{x} sayısı, {y} sayısından küçüktür.")
    """
#endregion

#region ornek_3
"""
kullaniciAdi, password =str(input("Kullanıcı adı\t:")), str(input("Şifre\t:"))
if kullaniciAdi=="admin":
     if password=="123":
        print("Giriş Başarılı!")
     else:
        print("Şifre hatalı.")
else:
    print("Kullanıcı adı hatalı.")
    """
#endregion

#region ornek_4
"""
s1, s2, s3 = int(input("s1 girin:")), int(
    input("s2 girin:")), int(input("s3 girin:"))
if s1 < s2:
    s1, s2 = s2, s1
if s1 < s3:
    s1, s3 = s3, s1
if s2 < s3:
    s2, s3 = s3, s2
print(f"{s1}>{s2}>{s3}")
"""
#endregion

#region ornek_5
"""
print("Dörtgenin her kenarı 90 derecedir.")

a, b = int(input("Dörtgenin A kenarını giriniz=")), int(input("Dörtgenin B kenarını giriniz="))
alan=a*b
if a==b:
    print(f"Karenin alanı = {alan} ")
else:
    print(f"Dikdörtgenin alanı = {alan}")
    """
#endregion

