"""rakam = int(input("Lütfen bir rakam giriniz\t :"))
print(str(rakam) + "Girdiğiniz rakamın 1 fazlası =" + str(rakam+1))
"""

"""rakam = int(input("Lütfen bir rakam giriniz\t :"))
print(" {} rakamının 1 fazlası {}".format(rakam, rakam+1))"""

#region yontem_fstring
"""
rakam = int(input("Lütfen bir rakam giriniz\t :"))
print(f"{rakam} rakamının bir fazlası {rakam+1}")


s1 = int(input("1.sayıyı giriniz\t :"))
s2 = int(input("2.sayıyı giriniz\t :"))
s3 = int(input("3.sayıyı giriniz\t :"))
ort = (s1+s2+s3)/3

print(f"{s1}, {s2}, {s3} sayı değerlerinin ortalaması\t: {ort}")"""
#endregion

#Lütfen Ağırlık Bilgisi Giriniz: 75
#Lütfen Boy Bilgisi Giriniz (mt) : 178
#75 kg. ve 1.78 metre değerine göre VKİ sonucu : 23

"""agirlik = int(input("Lütfen Ağırlık Bilgisi Giriniz\t:"))
boy = float(input("Lütfen Boy Bilgisi Giriniz(mt)\t:"))
vki = agirlik/boy**2
print(f"Vücut Kitle Endeksi {vki}")"""

yariCap = int(input("Lütfen yarıçapı giriniz\t:"))
cevre = 2*3.14*yariCap
alan = 3.14*yariCap**2
print(f"{yariCap} yarı çaplı dairenin çevresi {cevre} ve alanı {alan}")