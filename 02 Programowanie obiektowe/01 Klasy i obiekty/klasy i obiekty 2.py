
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


def wypisz_zamowienie(zamowienie):
    print("=" * 20)
    print(f"Zamówienie złożone przez {zamowienie.imie} {zamowienie.nazwisko}")
    print(f"o łącznej wartości {zamowienie.total_cena} PLN")
    print("zamówione produkty:")
    for produkty in zamowienie.lista_produktow:
        print("\t", end="")
        wypisz_zamowienie(produkty)
    print("=" *20)
    print()


def run_homework():
    ciasteczka = Produkt(nazwa="Ciasteczka", kategoria="Jedzenie", cena=4)
    puste_zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cybulski")
    zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cybulski", lista_produktow=[ciasteczka, ciasteczka, ciasteczka])

    wypisz_zamowienie(puste_zamowienie)
    wypisz_zamowienie(zamowienie)


if __name__== '__main__':
    run_homework()


