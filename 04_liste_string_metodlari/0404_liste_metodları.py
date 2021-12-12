#append -> listenin sonuna ekleme yapar
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
print(f"{meyveler} listemizin ilk hali")
meyveler.append("karpuz")
print(f"{meyveler} listemizin son hali")
"""
#insert -> istediğiniz indekse ekleme yapar
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
print(f"{meyveler} listemizin ilk hali")
meyveler.insert(2, "çilek")
print(f"{meyveler} listemizin son hali")
"""
#remove -> listeden çıkarma yapar
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
print(f"{meyveler} listemizin ilk hali")
meyveler.remove("muz")
print(f"{meyveler} listemizin son hali")
"""
#pop -> listeden siler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
print(f"{meyveler} listemizin ilk hali")
# print(meyveler.pop()) belirtmez isek son elemanı siler
print(meyveler.pop(2)) #indekslenen elemanı siler
print(f"{meyveler} listemizin son hali")
"""

# region clear→listeyi_temizler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
meyveler.clear()
print(meyveler)
del meyveler
print(f"listemizin son hali → {meyveler}")
"""
# copy-> listeyi kopyalar
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
print(f"{meyveler} listemizin ilk hali")
meyveTabagi = meyveler.copy()
print(f"{meyveTabagi} listemizin son hali")
"""

# count ->eleman sayısı

"""
listedekiRakamlar = [1, 4, 7, 9, 11, 36, 9,71, 9]
arananEleman = 9
elemanAdedi = listedekiRakamlar.count(arananEleman)
print(f"listemizdeki {arananEleman} eleman adedi ->{elemanAdedi}")
"""

# sort_reverse → sirala_tersten sirala
"""
listeRakamlar = [2, 5, 6, 1, 4, 9, 3, 8, 7]
print(f"listemizin ilk hali → {listeRakamlar}")
listeRakamlar.sort()
print(f"listemizin son hali → {listeRakamlar}")
listeRakamlar.reverse()
print(f"listemizin son hali → {listeRakamlar}")
"""
# index→arama_indeks_dondurme
"""
listeRakamlar = [2, 5, 6, 1, 9, 7]
print(listeRakamlar.index(1))
"""

