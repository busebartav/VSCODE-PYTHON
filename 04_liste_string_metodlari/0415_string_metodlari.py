# region string_metodlari
"""
upper() lower() title() capatilize()
count() replace()   swapcase()
startswith()    endswith()
strip() lstrip()    rstrip()
isdigit()   isalpha()
isalphanum()    isspace()   istitle()   isidentifier()
split() index() find() format()
"""

# upper() küçük karakterleri büyütür
"""
ogrenciAdi = "Ege Bartu"
print(ogrenciAdi.upper())
"""

# lower() büyük karakterleri küçültür
"""
ogrenciAdi = "EGE BARTU"
print(ogrenciAdi.lower())
"""

# title() baş harfleri büyük yapar
"""
ogrenciAdi = "EGE BARTU"
print(ogrenciAdi.title())
"""

# capatalize()
"""
ogrenciAdi = "ege bartu"
print(ogrenciAdi.capitalize())
"""

# count()
"""
ogrenciAdi = "ege bartu"
print(ogrenciAdi.count("e"))
"""

# replace()
"""
url = "www.azizbektas.edu.tr"
print(url.replace("edu.tr", "com"))
"""

# swapcase()
"""
ogrenciAdiSoyadi = "EgE BaRtU"
print(ogrenciAdiSoyadi.swapcase())
"""

# startswith()
"""
url = input("url adresinizi giriniz:")
isValid = url.startswith("www")
if isValid:
    print("url adresi doğru")
else:
    print("url adresi geçersiz")
"""

# endswith()
"""
url ="http://www.azizbektas.com.tr" 
gecerliMi = url.endswith("edu.tr")
print(gecerliMi)
"""

# strip()
"""
url = input("url adresinizi giriniz:")
print(url.strip().strip("."))
"""

# isdigit()
"""
value = "kırk"
print(value.isdigit())
"""

# split()

wh = "boşlukları gördün mü"
print(wh.split(" "))