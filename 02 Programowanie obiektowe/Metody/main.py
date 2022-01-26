from shop.Jablka import Jablka
from shop.Ziemniaki import Ziemniaki
from shop.Zamowienia import Zamowienia
from shop.Produkt import Produkt





def run_homework():
    ciasteczka = Produkt(nazwa="Ciasteczka", kategoria="Jedzenie", cena=4)
    puste_zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cybulski")
    zamowienie = Zamowienia(imie="Zbyszek", nazwisko="Cybulski", lista_produktow=[ciasteczka, ciasteczka, ciasteczka])

    # zamowienie.wypisz_zamowienie(self=puste_zamowienie)
    zamowienie.wypisz_zamowienie(self)


if __name__== '__main__':
    run_homework()

