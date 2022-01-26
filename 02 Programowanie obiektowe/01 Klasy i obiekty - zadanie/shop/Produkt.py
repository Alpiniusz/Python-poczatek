class Produkt:
    def __init__(self, nazwa, kategoria, cena):
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.cena = cena

def wypisz_produkt(produkt):
    print(f"Nazwa {produkt.nazwa}, Kategoria {produkt.kategoria}, Cena {produkt.cena}")