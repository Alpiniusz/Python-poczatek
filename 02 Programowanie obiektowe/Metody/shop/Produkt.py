class Produkt:
    def __init__(self, nazwa, kategoria, cena):
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.cena = cena

    def wypisz_produkt(self):
        print(f"Nazwa {self.nazwa}, Kategoria {self.kategoria}, Cena {self.cena}")