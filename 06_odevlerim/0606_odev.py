"""
    - Kullanıcıdan bir sayı alınır.
        - Pozitifse karesini yazdırın.
        - Negatifse karekökünü yazdırın.
        - 0'sa sıfır yazsın
"""
x=int(input("Bir sayı yazınız:"))
if x>0:
    y=x**2
    print(f"{y}")
elif x==0:
    print(f"{x}")
else:
    y=x**0.5
    print(f"{y}")