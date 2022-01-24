
class Produkt:
    def __init__(self, nazwa, kategoria, cena):
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.cena = cena

class Zamowienia:
    def __init__(self, imie, nazwisko, lista_produktow=None):
        self.imie = imie
        self.nazwisko = nazwisko
        if lista_produktow is None:
            lista_produktow = []
        self.lista_produktow = lista_produktow

        total_cena = 0
        for produkt in lista_produktow:
            total_cena += produkt.cena
        self.total_cena = total_cena

class Jablka:

    def __init__(self, nazwa_gatunku, wielkosc, cena):
        self.nazwa_gatunku = nazwa_gatunku
        self.wielkosc = wielkosc
        self.cena = cena




class Ziemniaki:
    def __init__(self, nazwa_gatunku, wielkosc, cena):
        self.nazwa_gatunku = nazwa_gatunku
        self.wielkosc = wielkosc
        self.cena = cena

def run_homework():
    zielone_jablka = Jablka(nazwa_gatunku="Zielone", wielkosc="M", cena=3.5)
    czerwon_jablka = Jablka(nazwa_gatunku="Czerwone", wielkosc="S", cena=2.8)
    print(zielone_jablka.nazwa_gatunku, zielone_jablka)
    print(czerwon_jablka.nazwa_gatunku, czerwon_jablka)

    stare_ziemniaki = Ziemniaki(nazwa_gatunku="Stare ziemniaki", wielkosc="S", cena=1.55)
    print(stare_ziemniaki.nazwa_gatunku, stare_ziemniaki)

    ciasteczka = Produkt(nazwa="Ciasteczka", kategoria="Jedzenie", cena=4)
    puste_zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cybulski")
    zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cybulski", lista_produktow=[ciasteczka])

    print(ciasteczka)
    print(puste_zamowienie)
    print(zamowienie)



if __name__== '__main__':
    run_homework()


# ziemniak_1 = Ziemniaki()
# ziemniak_2 = Ziemniaki()
# jablko = Jablka()
# produkt = Produkt()
#
# print("ziemniak_1 ", type(ziemniak_1))
# print("ziemniak_2 ", type(ziemniak_2))
# print("jablko", type(jablko))
# print("produkt", type(produkt))
#
# Zamowienia1 = [Zamowienia(), Zamowienia(), Zamowienia()]
#
# print(Zamowienia1)
#
# Produkty = {
#     "ziemniak_1": Produkt(),
#     "ziemniak_2": Produkt(),
#     "jablko": Jablka(),
# }
#
# print(Produkty)