import Produkt
import random






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

    def wypisz_zamowienie(self):
        print("=" * 20)
        print(f"Zamówienie złożone przez {self.imie} {self.nazwisko}")
        print(f"o łącznej wartości {self.total_cena} PLN")
        print("zamówione produkty:")
        for produkty in self.lista_produktow:
            print("\t", end="")
            produkty.wypisz_produkt(produkty)
        print("=" *20)
        print()

def generuj_zamowienie():
    ilosc_produktow = random.randint(1,10)
    produkty = []
    for nr_produktu in range(ilosc_produktow):
        nazwa_produktu = f"Produkt - {nr_produktu}"
        kategoria = "inne"
        cena = random.randint(1, 30)
        produkt = Produkt(nazwa_produktu, kategoria, cena)
        produkt.append(produkt)

    zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cubulski", lista_produktow=produkty)
    return zamowienie
