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

def wypisz_zamowienie(zamowienia):
    print("=" * 20)
    print(f"Zamówienie złożone przez {zamowienia.imie} {zamowienia.nazwisko}")
    print(f"o łącznej wartości {zamowienia.total_cena} PLN")
    print("zamówione produkty:")
    for produkty in zamowienia.lista_produktow:
        print("\t", end="")
        wypisz_produkt(produkty)
    print("=" *20)
    print()
