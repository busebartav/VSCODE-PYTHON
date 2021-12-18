""" karşılama fonksiyonunda ad alalım



def saatKac(ad):
    import datetime
    saat = datetime.datetime.now().hour
    if saat < 12:
        print(f"Günaydın {ad}")
    else:
        print(f"Merhaba {ad}")


saatKac("Buse")

"""

