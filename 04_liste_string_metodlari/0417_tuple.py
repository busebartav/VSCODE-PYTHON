# region tuples_tiyuples
"""
1→ list
2→ tuple
3→ dictionary
1-) list özellikleri
→ tek bir değişken adında birden fazla eleman saklama
→ sıralı index özelliği
→ zero based’dir. İlk eleman [0], ikinci eleman [1]
→ duplicate eleman saklamaya izin vermesi
→ eleman değerlerinin değiştirilebilmesi
→ tanımlama anında, köşeli parantez [ ] kullanılması

2-) tuple özellikleri
→ tek bir değişken adında birden fazla eleman saklama
→ sıralı index özelliği. 
→ zero based’dir. İlk eleman [0], ikinci eleman [1]
→ duplicate eleman saklamaya izin vermesi
→ eleman değerlerinin değiştirilememesi
→ tanımlama anında, aç kapa parantez ( ) kullanılması
"""
# endregion

"""
meyveler = ("elma", "armut", "ayva")
print(meyveler)
print(meyveler[1])

for i in meyveler:
    if not i=="armut":
        print(i)
"""

#def. koleksiyon tuple'dır, o yüzden () kullanmayabilirsin
tupleListem = 3, 6, 7, 9, 11
#print(tupleListem)
aradiginizDeger = int(input("aradığınız değer:"))
print(f"{aradiginizDeger}, {tupleListem.count(int(aradiginizDeger))} adettir.")